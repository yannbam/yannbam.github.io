# Website Update Cheatsheet

## Quick Reference

### Adding a New Monologue to Website
```bash
# 1. Create new monologue file in project root
# 2. Run update script to refresh website
python update_index.py
```

## Common Operations

### Extract Title from Monologue
```python
import re

def extract_title(filename):
    with open(filename, 'r') as f:
        content = f.read()
        title_match = re.search(r"\*Claude's Internal Monologue: (.*?)\*", content)
        if title_match:
            return title_match.group(1)
    return os.path.splitext(filename)[0].replace('_', ' ').title()
```

### Extract Description from Monologue
```python
def extract_description(filename):
    with open(filename, 'r') as f:
        content = f.read()
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if i > 0 and i < 5 and '*[' in line and ']' in line:
                description = line.strip('*[] \n')
                return description
    return "A monologue about technical concepts with unique personalities."
```

### Generate HTML ID from Filename
```python
import re
import os

def get_id_from_filename(filename):
    base = os.path.splitext(filename)[0]
    return re.sub(r'[^a-z0-9]', '-', base.lower())
```

## Gotchas and Pitfalls

### BeautifulSoup Dependency
The website update process requires BeautifulSoup. If not installed:
```bash
pip install beautifulsoup4
```

### HTML Structure Requirements
The index.html file must contain:
- A `<nav>` element with a `<ul>` for navigation
- A `<div class="content-box">` with an `<h2>` containing "Available Monologues"
- This div should also contain a `<ul>` for the monologue list

### JavaScript Dynamic Loading
The script dynamically inserts JavaScript to load monologue content, using:
```javascript
async function loadTextContent(file, targetSelector) {
    try {
        const response = await fetch(file);
        if (!response.ok) throw new Error(`Failed to load ${file}`);
        const text = await response.text();
        const formattedText = text.replace(/\n/g, '<br>');
        document.querySelector(targetSelector).innerHTML = formattedText;
    } catch (error) {
        console.error(error);
        document.querySelector(targetSelector).innerHTML = 
            `<p>Error loading content: ${error.message}</p>`;
    }
}
```

### Common Errors

#### No Monologues Found
If no .txt files are found in the current directory, the script will report "No monologue files found."

#### Missing index.html
If index.html is not in the current directory, the script will report "Error: index.html not found in the current directory."

#### BeautifulSoup Not Installed
If BeautifulSoup is not installed, the script will instruct the user to install it with `pip install beautifulsoup4`.

## Tips for Robust Updates

1. Always run from the project root directory
2. Verify monologue files have the correct formatting before updating
3. Check that monologue titles follow the pattern `*Claude's Internal Monologue: [TITLE]*`
4. After updating, verify that the navigation menu and content areas are correctly populated