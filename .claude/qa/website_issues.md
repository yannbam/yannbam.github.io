# Website Issues and Solutions

## Content Loading Errors

### Issue: Monologue Text Not Loading in Browser
**Error Message**: `Error loading content: Failed to load [filename]`

**Context**:
- Browser console shows CORS policy errors
- Content areas display error messages instead of monologue text

**Solution**:
```
This is typically caused by opening the HTML file directly in a browser without a web server.
The solution is to serve the files with a local web server:

python -m http.server

Then access the site at http://localhost:8000/
```

**Reasoning**:
Browsers enforce security restrictions that prevent loading local files via JavaScript's fetch API when a page is opened directly from the filesystem. Serving the files through a web server circumvents this restriction.

### Issue: Monologue Formatting Lost
**Error Message**: None, but monologue text appears without proper formatting

**Context**:
- Markdown-style formatting in monologues appears as raw text
- Bold and italic formatting not rendered

**Solution**:
```
Modify the JavaScript loading function to convert Markdown-style formatting to HTML:

async function loadTextContent(file, targetSelector) {
    try {
        const response = await fetch(file);
        if (!response.ok) throw new Error(`Failed to load ${file}`);
        const text = await response.text();
        
        // Convert basic Markdown to HTML
        let formattedText = text.replace(/\\n/g, '<br>');
        formattedText = formattedText.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
        formattedText = formattedText.replace(/\*([^*]+)\*/g, '<em>$1</em>');
        
        document.querySelector(targetSelector).innerHTML = formattedText;
    } catch (error) {
        console.error(error);
        document.querySelector(targetSelector).innerHTML = 
            `<p>Error loading content: ${error.message}</p>`;
    }
}
```

**Reasoning**:
The original implementation only handles line breaks but not other Markdown formatting. The updated function uses regular expressions to convert bold and italic formatting from Markdown to HTML.

## Navigation Issues

### Issue: Navigation Links Not Working
**Error Message**: None, but clicking navigation links doesn't scroll to content

**Context**:
- Navigation menu appears correctly
- Links have proper href attributes with IDs
- Clicking links doesn't navigate to the corresponding section

**Solution**:
```
Add smooth scrolling behavior to the CSS:

html {
  scroll-behavior: smooth;
}

And ensure all content sections have the correct IDs:

<div id="section-id" class="content-box">...</div>

Verify that navigation links use the correct format:

<a href="#section-id">Link Text</a>
```

**Reasoning**:
This issue is typically caused by either missing/mismatched IDs between navigation links and content sections, or by the default abrupt scrolling behavior that can make it seem like nothing happened, especially in long documents.

## Update Script Issues

### Issue: No Monologues Found
**Error Message**: `No monologue files found.`

**Context**:
- update_index.py script run successfully
- No errors, but reports no monologues found

**Solution**:
```
1. Verify that you're running the script from the correct directory containing .txt files
2. Check that the monologue files have .txt extension
3. If needed, modify the function to search recursively or in specific directories:

def get_monologue_files():
    """Get all monologue text files in the specified directories."""
    # Search in current directory and specific subdirectories
    files = []
    files.extend(glob.glob("*.txt"))
    files.extend(glob.glob("monologues/*.txt"))
    return files
```

**Reasoning**:
The script only searches for .txt files in the current directory. If files are in subdirectories or have different extensions, they won't be found.

### Issue: BeautifulSoup Not Installed
**Error Message**: `Error: BeautifulSoup is not installed.`

**Context**:
- Script fails immediately with dependency error

**Solution**:
```
Install the required dependency:

pip install beautifulsoup4
```

**Reasoning**:
The update_index.py script depends on BeautifulSoup for HTML parsing. This error occurs when the dependency is not installed in the current Python environment.