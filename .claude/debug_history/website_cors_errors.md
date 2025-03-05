# Debug Session: Website CORS Errors

## Error Information
- **Component**: Website Content Loading
- **Error Type**: CORS Policy Violation
- **Date First Observed**: 2025-03-05
- **Context**: Users opening index.html directly from filesystem
- **Error Message**: `Failed to load [filename]: Cross origin requests are only supported for HTTP protocols`

## Detailed Analysis

### Error Context
When users try to open the index.html file directly from their filesystem (using a file:// protocol), the browser's JavaScript fetch API is unable to load the monologue text files due to security restrictions. This results in the content areas displaying error messages instead of the monologue text.

### Browser Console Errors
```
Access to fetch at 'file:///path/to/sorting_monologue.txt' from origin 'null' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, data, isolated-app, chrome-extension, chrome, https, chrome-untrusted.
```

### Root Cause
Modern browsers implement a security feature called Same-Origin Policy, which prevents JavaScript from making requests to resources from different origins. When accessing files via the file:// protocol, there isn't a proper origin defined, causing the browser to block attempts to load other local files.

## Solution

### Immediate Fix
The solution is to serve the files using a local web server instead of opening them directly from the filesystem:

```bash
# Using Python's built-in HTTP server
python -m http.server

# Or using Node.js with http-server package
npx http-server
```

Then access the site by navigating to http://localhost:8000/ in a web browser.

### Long-term Fix
1. Added a prominent warning in the README.md file explaining that the website must be accessed through a web server
2. Modified the error handling in the loadTextContent function to provide a more descriptive error message that includes instructions for setting up a local server
3. Added a fallback mechanism that attempts to load content using an alternative method when fetch fails

### Modified Code
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
            `<p>Error loading content: ${error.message}</p>
             <p class="error-help">If you're seeing this error, you may be opening the file directly from your filesystem. 
             Try serving the files using a local web server instead:</p>
             <pre>python -m http.server</pre>
             <p>Then navigate to <a href="http://localhost:8000">http://localhost:8000</a></p>`;
    }
}
```

## Verification
- Tested by opening index.html directly from filesystem, confirmed the improved error message appeared
- Tested by serving with Python's http.server, confirmed all content loaded correctly
- Tested by serving with Node.js http-server, confirmed all content loaded correctly
- Verified all content areas on the page showed the monologue text when accessed via http://localhost:8000

## Outcome
- **Resolution Status**: Resolved with improved error handling
- **Implementation Date**: 2025-03-05
- **Side Effects**: None observed
- **Documentation Updated**: Yes, added to both README.md and website_issues.md in the qa directory