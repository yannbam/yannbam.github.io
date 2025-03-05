#!/usr/bin/env python3
"""
Script to update index.html with new monologues.
This should be run after adding new monologue files to keep the web interface in sync.
"""

import os
import re
import glob
from bs4 import BeautifulSoup

def get_monologue_files():
    """Get all monologue text files in the current directory."""
    return glob.glob("*.txt")

def extract_title(filename):
    """Extract the title from a monologue file."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            title_match = re.search(r"\*Claude's Internal Monologue: (.*?)\*", content)
            if title_match:
                return title_match.group(1)
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    
    # Fallback: use the filename
    return os.path.splitext(filename)[0].replace('_', ' ').title()

def extract_description(filename):
    """Extract a brief description from a monologue file."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            # Look for the scene description which is usually in the second line with italics
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if i > 0 and i < 5 and '*[' in line and ']' in line:
                    description = line.strip('*[] \n')
                    return description
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    
    # Fallback
    return "A monologue about technical concepts with unique personalities."

def get_id_from_filename(filename):
    """Convert a filename to an ID suitable for HTML."""
    base = os.path.splitext(filename)[0]
    # Convert to lowercase, replace underscores and spaces with hyphens
    return re.sub(r'[^a-z0-9]', '-', base.lower())

def update_index_html():
    """Update the index.html file with all monologue files."""
    if not os.path.exists('index.html'):
        print("Error: index.html not found in the current directory.")
        return False
    
    # Get all monologue files
    monologue_files = get_monologue_files()
    if not monologue_files:
        print("No monologue files found.")
        return False
    
    # Read the current index.html
    with open('index.html', 'r') as f:
        html_content = f.read()
    
    # Parse with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Update the navigation menu
    nav_ul = soup.find('nav').find('ul')
    nav_ul.clear()  # Remove current items
    
    # Update the content sections
    content_div = None
    content_list = None
    for div in soup.find_all('div', {'class': 'content-box'}):
        if div.find('h2') and div.find('h2').text == 'Available Monologues':
            content_div = div
            content_list = div.find('ul')
            if content_list:
                content_list.clear()  # Remove current items
            break
    
    # Get or create the script section
    script_tag = soup.find('script')
    if not script_tag:
        script_tag = soup.new_tag('script')
        soup.body.append(script_tag)
    
    # Get the DOMContentLoaded event listener function
    script_content = script_tag.string
    load_content_calls = []
    
    # Remove all current monologue divs
    for div in soup.find_all('div', {'class': 'content-box', 'id': True}):
        if div.get('id') != 'available-monologues':  # Keep the list of available monologues
            div.decompose()
    
    # Process all monologue files
    for filename in sorted(monologue_files):
        title = extract_title(filename)
        description = extract_description(filename)
        file_id = get_id_from_filename(filename)
        
        # Add to navigation
        nav_item = soup.new_tag('li')
        nav_link = soup.new_tag('a', href=f'#{file_id}')
        short_title = title.split(':')[-1].strip() if ':' in title else title
        nav_link.string = short_title
        nav_item.append(nav_link)
        nav_ul.append(nav_item)
        
        # Add to content list
        if content_div and content_list:
            list_item = soup.new_tag('li')
            list_link = soup.new_tag('a', href=f'#{file_id}')
            list_link.string = title
            list_item.append(list_link)
            content_list.append(list_item)
        
        # Create content box
        content_box = soup.new_tag('div', id=file_id, **{'class': 'content-box'})
        
        # Add header
        header = soup.new_tag('h2')
        header.string = title
        content_box.append(header)
        
        # Add description
        desc_p = soup.new_tag('p')
        desc_p.string = description
        content_box.append(desc_p)
        
        # Add monologue div
        monologue_div = soup.new_tag('div', **{'class': 'monologue'})
        loading_p = soup.new_tag('p')
        loading_em = soup.new_tag('em')
        loading_em.string = 'Loading content...'
        loading_p.append(loading_em)
        monologue_div.append(loading_p)
        content_box.append(monologue_div)
        
        # Add view raw link
        link_p = soup.new_tag('p')
        raw_link = soup.new_tag('a', href=filename)
        raw_link.string = 'View raw text'
        link_p.append(raw_link)
        content_box.append(link_p)
        
        # Add to document
        soup.body.append(content_box)
        
        # Add to script
        load_content_calls.append(f"loadTextContent('{filename}', '#{file_id} .monologue');")
    
    # Update the script with new loadTextContent calls
    if 'window.addEventListener' in script_content:
        # Replace the existing event listener content
        script_content = re.sub(
            r'window\.addEventListener\([^{]+{([^}]+)}[^}]+\);',
            f"window.addEventListener('DOMContentLoaded', () => {{\n        {chr(10).join('        ' + call for call in load_content_calls)}\n    }});",
            script_content
        )
    else:
        # Create a new event listener
        script_content = f"""
        // Simple function to load text files into the page
        async function loadTextContent(file, targetSelector) {{
            try {{
                const response = await fetch(file);
                if (!response.ok) throw new Error(`Failed to load ${{file}}`);
                const text = await response.text();
                const formattedText = text.replace(/\\n/g, '<br>');
                document.querySelector(targetSelector).innerHTML = formattedText;
            }} catch (error) {{
                console.error(error);
                document.querySelector(targetSelector).innerHTML = 
                    `<p>Error loading content: ${{error.message}}</p>`;
            }}
        }}

        // Load all content when the page loads
        window.addEventListener('DOMContentLoaded', () => {{
            {chr(10).join('        ' + call for call in load_content_calls)}
        }});
        """
    
    script_tag.string = script_content
    
    # Write the updated HTML
    with open('index.html', 'w') as f:
        f.write(str(soup.prettify()))
    
    print(f"Updated index.html with {len(monologue_files)} monologues.")
    return True

if __name__ == "__main__":
    try:
        import bs4
    except ImportError:
        print("Error: BeautifulSoup is not installed.")
        print("Please install it with: pip install beautifulsoup4")
        exit(1)
        
    update_index_html()