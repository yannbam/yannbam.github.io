# Claude-Optimized Repository Structure

This directory contains metadata and structured information specifically designed to help Claude (and future versions) work more efficiently with this codebase.

## Directory Structure

- `metadata/`: Normalized information about the codebase including component dependencies and file classifications
- `code_index/`: Semantic code relationships including call graphs and interface implementations
- `debug_history/`: Log of debugging sessions with error-solution pairs
- `patterns/`: Canonical implementation patterns with examples
- `cheatsheets/`: Quick-reference guides for components including common operations and pitfalls
- `qa/`: Database of previous solved problems
- `delta/`: Semantic change logs between versions

## Purpose

This structure creates a Claude-optimized layer on top of the standard repository, enabling more efficient assistance by:
- Providing machine-readable metadata about code structure and intent
- Maintaining history of solutions and patterns
- Creating explicit memory anchors with semantic structure
- Documenting relationships that might be difficult to infer from code alone