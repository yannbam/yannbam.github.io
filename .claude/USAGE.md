# Claude Optimization Layer Usage Guide

## Purpose
This document explains how to use the Claude optimization layer to work more efficiently with this codebase.

## Directory Structure

The `.claude` directory contains metadata and structured information specifically designed to help Claude work more efficiently with this codebase:

- `metadata/`: Normalized information about code structure including dependency graphs and monologue structure
- `code_index/`: Semantic code relationships with function dependencies and data flow
- `debug_history/`: Log of debugging sessions with detailed error-solution pairs
- `patterns/`: Canonical implementation patterns for monologue creation and website updates
- `cheatsheets/`: Quick-reference guides for common operations and potential pitfalls
- `qa/`: Database of previous issues and their solutions
- `delta/`: Semantic change logs documenting project evolution

## Memory Anchors

Memory anchors are special comments in key files that provide reference points for Claude to quickly locate and understand important sections of code. They use UUIDs for precise referencing and are structured as:

```
<!-- CLAUDE-ANCHOR: anchor-name [uuid] -->
```

Example anchors in the codebase:

- `website-main-document [e4f5a6b7-c8d9-e0f1-a2b3-c4d5e6f7a8b9]` in index.html
- `website-navigation [f5a6b7c8-d9e0-f1a2-b3c4-d5e6f7a8b9c0]` in index.html
- `website-content-loader [a6b7c8d9-e0f1-a2b3-c4d5-e6f7-a8b9-c0d1]` in index.html
- `monologue-structure-doc [1d2e3f4a-5b6c-7d8e-9f0a-1b2c3d4e5f6a]` in metadata/monologue_structure.md

Use these anchors in your prompts to direct Claude to specific parts of the codebase.

## Best Practices

### For Git Operations
Use commit patterns documented in `.claude/metadata/git/commit_patterns.json` to maintain consistency with the project's commit history.

### For Monologue Creation
Reference the patterns in `.claude/patterns/monologue_creation.md` when asking Claude to create new monologues or modify existing ones.

### For Website Updates
Use the cheatsheet in `.claude/cheatsheets/website_update.md` to guide Claude in making website updates or troubleshooting website issues.

### For Troubleshooting
Direct Claude to check `.claude/debug_history/` and `.claude/qa/` for solutions to common issues.

## Example Prompts

### Using Memory Anchors
```
Please update the website navigation at the memory anchor "website-navigation" to include a new entry for the AI Ethics monologue.
```

### Using Semantic Metadata
```
Using the component structure described in .claude/metadata/component_graph.json, please explain how the update_index.py script interacts with the monologue files.
```

### Using Patterns Documentation
```
Create a new monologue about "Cryptographic Algorithms" following the patterns documented in .claude/patterns/monologue_creation.md.
```

## Keeping Optimizations Current

When making significant changes to the codebase:

1. Update component graphs in `.claude/metadata/`
2. Add relevant memory anchors to new key files
3. Document any new patterns in `.claude/patterns/`
4. Track debugging sessions in `.claude/debug_history/`
5. Add semantic delta summaries to `.claude/delta/`

This ensures that the Claude optimization layer remains useful and accurate as the project evolves.