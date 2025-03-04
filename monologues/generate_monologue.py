#!/usr/bin/env python3
"""
Script to generate a new technical monologue by calling the Claude API.
This requires an Anthropic API key to be set as ANTHROPIC_API_KEY environment variable.
"""

import os
import argparse
import json
import sys
import re
import time
from datetime import datetime

try:
    import anthropic
    from anthropic import Anthropic
except ImportError:
    print("Error: Anthropic Python SDK not installed.")
    print("Please install it with: pip install anthropic")
    sys.exit(1)

def get_api_key():
    """Get the Anthropic API key from environment variables."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Please set it with: export ANTHROPIC_API_KEY='your-api-key'")
        sys.exit(1)
    return api_key

def create_prompt(category, format_type):
    """Create a prompt for Claude to generate a monologue."""
    
    prompt = f"""Generate a humorous creative monologue where {category} concepts are personified as characters with distinct personalities.

The format should be similar to a {format_type}, where each {category} concept speaks with a unique voice reflecting its characteristics and trade-offs.

Use the following structure:
1. Start with "*Claude's Internal Monologue: [TITLE]*"
2. Add a scene-setting description in italics
3. For each personified concept:
   - Include the name in bold: "**[CONCEPT NAME]**"
   - Add personality traits in italics inside brackets: "*[trait description]*"
   - Add dialogue in quotes that reflects the concept's unique characteristics
4. End with "*[Reflecting quietly]*" and a final philosophical reflection

Make it technically accurate while being entertaining and educational. Each personified concept should embody the actual characteristics, advantages, and limitations of the real technical concept.

Here's an example structure (but use {category} concepts instead):

*Claude's Internal Monologue: [Title]*

*[Scene description]*

**[First Concept]**: *[personality traits]* "Dialogue that reflects the concept's characteristics..."

**[Second Concept]**: *[personality traits]* "Dialogue that reflects the concept's characteristics..."

*[Reflecting quietly]*

[Final philosophical reflection on the concepts]
"""
    return prompt

def generate_monologue(prompt, max_tokens=4000):
    """Generate a monologue using the Anthropic Claude API."""
    client = Anthropic(api_key=get_api_key())
    
    print("Generating monologue with Claude... (this may take a moment)")
    
    try:
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=max_tokens,
            temperature=0.7,
            system="You are Claude, an AI assistant that specializes in creating humorous monologues that personify technical concepts. You excel at adding distinct personalities to technical concepts that reflect their real characteristics.",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return message.content[0].text
    except Exception as e:
        print(f"Error calling Claude API: {e}")
        sys.exit(1)

def sanitize_filename(title):
    """Convert the title to a valid filename."""
    # Remove special characters and replace spaces with underscores
    filename = re.sub(r'[^\w\s-]', '', title.lower())
    filename = re.sub(r'[\s-]+', '_', filename)
    return filename + ".txt"

def extract_title(text):
    """Extract the title from the generated monologue."""
    title_match = re.search(r"\*Claude's Internal Monologue: (.*?)\*", text)
    if title_match:
        return title_match.group(1)
    else:
        return "Untitled Monologue"

def save_monologue(text, category):
    """Save the generated monologue to a file."""
    title = extract_title(text)
    filename = sanitize_filename(title)
    
    # Save to file
    with open(filename, 'w') as f:
        f.write(text)
    
    print(f"Monologue saved to: {filename}")
    
    # Update CLAUDE.md
    update_claude_md(filename, title, category)
    
    # Update categories.md
    update_categories_md(filename, title, category)
    
    return filename, title

def update_claude_md(filename, title, category):
    """Update CLAUDE.md with the new monologue."""
    claude_md_path = "CLAUDE.md"
    if os.path.exists(claude_md_path):
        with open(claude_md_path, 'r') as f:
            content = f.read()
        
        # Find the Project Files section and add the new file
        if '## Project Files' in content:
            description = f"A monologue about {category} concepts with distinct personalities"
            new_line = f"- {filename}: {description}"
            
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('## Project Files'):
                    # Find the end of the list
                    j = i + 1
                    while j < len(lines) and lines[j].startswith('- '):
                        j += 1
                    lines.insert(j, new_line)
                    break
            
            with open(claude_md_path, 'w') as f:
                f.write('\n'.join(lines))
            print(f"Updated CLAUDE.md with new monologue entry")

def update_categories_md(filename, title, category):
    """Update categories.md with the new monologue."""
    categories_md_path = "categories.md"
    if os.path.exists(categories_md_path):
        with open(categories_md_path, 'r') as f:
            content = f.read()
        
        # Extract characters from the file
        with open(filename, 'r') as f:
            monologue_text = f.read()
        
        # Extract personalities using regex
        personalities = re.findall(r'\*\*([^*]+)\*\*', monologue_text)
        personalities = [p.strip() for p in personalities if not p.strip().startswith('[')]
        
        # Create the personalities string
        personalities_str = ", ".join(personalities[:5])
        if len(personalities) > 5:
            personalities_str += ", and others"
        
        # Create the new entry
        new_entry = f"- **{title}**: {filename}  \n  *Personalities: {personalities_str}*"
        
        # Try to find a category section to add it to
        category_lower = category.lower()
        section_found = False
        
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('##') and category_lower in line.lower():
                # Find where to insert (after the last entry in this section)
                j = i + 1
                while j < len(lines) and not lines[j].startswith('##'):
                    j += 1
                lines.insert(j, new_entry)
                section_found = True
                break
        
        # If no matching section, add to "Potential Future Categories"
        if not section_found:
            for i, line in enumerate(lines):
                if line.startswith('## Potential Future Categories'):
                    # Create a new category section
                    new_section = [
                        f"### {category}",
                        new_entry,
                        ""
                    ]
                    lines[i:i] = new_section
                    break
        
        with open(categories_md_path, 'w') as f:
            f.write('\n'.join(lines))
        print(f"Updated categories.md with new monologue entry")

def main():
    """Main function to parse arguments and generate monologue."""
    parser = argparse.ArgumentParser(description="Generate a new technical monologue using Claude.")
    parser.add_argument("category", help="Technical category to personify (e.g., 'cloud services', 'ML algorithms')")
    parser.add_argument("--format", "-f", default="group conversation", 
                        help="Format for the monologue (e.g., 'therapy session', 'debate', 'dinner party')")
    
    args = parser.parse_args()
    
    prompt = create_prompt(args.category, args.format)
    response = generate_monologue(prompt)
    filename, title = save_monologue(response, args.category)
    
    print("\nGeneration complete!")
    print(f"Title: {title}")
    print(f"File: {filename}")
    print("\nTo view the monologue: cat", filename)
    print("Remember to update index.html to include this new monologue in the web interface!")

if __name__ == "__main__":
    main()