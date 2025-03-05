# Monologue Structure Documentation

## Purpose
This document defines the standard structure for monologue files in this project, which present technical concepts as personified characters engaged in dialogue. The structure provides a consistent format for creative exploration of technical topics through character interactions.

## Schema
Each monologue follows this general structure:
```
*Claude's Internal Monologue: [TOPIC]*

*[Scene setting and context]*

**[Technical Concept 1]** *(personality traits)*: "Dialogue representing concept's perspective"

**[Technical Concept 2]** *(personality traits)*: "Dialogue representing another perspective"

*[Transitional narrative or stage direction]*

... [Additional character dialogues] ...

*[Concluding reflection]*
```

## Patterns

### Title Pattern
- Format: `*Claude's Internal Monologue: [TOPIC]*`
- Example: `*Claude's Internal Monologue: Sorting Algorithms*`
- UUID: 9a3f7d81-5c24-4b18-8e70-7f3ad2e28c49

### Scene Setting Pattern
- Format: `*[Description of setting and context]*`
- Example: `*[In Claude's mind, various sorting algorithms have gathered for their weekly debate club meeting. The atmosphere is charged with computational complexity.]*`
- UUID: b2c5e6f7-8d9a-4b1c-9e3f-1a2b3c4d5e6f

### Character Introduction Pattern
- Format: `**[Technical Concept]** *(personality traits)*: "Initial dialogue"`
- Example: `**Bubble Sort** *(nervous, apologetic)*: "I know I'm not the fastest, but I'm really simple to understand!"`
- UUID: 3e4f5a6b-7c8d-9e0f-1a2b-3c4d5e6f7a8b

### Dialogue Continuation Pattern
- Format: `**[Technical Concept]** *(personality traits)*: "Follow-up dialogue"`
- Example: `**Quick Sort** *(confident, slightly arrogant)*: "Why use something slow when you could use me? I'm generally O(n log n) and I work in-place!"`
- UUID: 5c6d7e8f-9a0b-1c2d-3e4f-5a6b7c8d9e0f

### Transitional Narrative Pattern
- Format: `*[Description of action or transition]*`
- Example: `*[The algorithms shift uncomfortably as the debate heats up]*`
- UUID: 7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b

### Conclusion Pattern
- Format: `*[Reflective observation or humorous conclusion]*`
- Example: `*[Claude sighs, realizing that even my own thoughts can't escape the inevitable complexity analysis puns.]*`
- UUID: 9a0b1c2d-3e4f-5a6b-7c8d-9e0f-1a2b3c4d

## Interfaces
Monologue files are plain text files (.txt) which serve as:
1. Stand-alone creative content
2. Source material for the website interface
3. Reference material for new monologue creation

## Invariants
The following must remain true for all monologues:
1. Technical accuracy of concept descriptions
2. Personality traits that metaphorically align with technical characteristics
3. Maintenance of the standardized formatting structure
4. Clear distinction between character dialogue and narrative text
5. Inclusion of a title that follows the pattern

## Error States
Possible errors in monologue structure:
1. Missing title or incorrectly formatted title
2. Inconsistent character personalities
3. Technical inaccuracies in concept descriptions
4. Missing formatting elements (bold characters, italic narrative)
5. Insufficient character interaction or progression

## Memory Anchors
<!-- CLAUDE-ANCHOR: monologue-structure-doc [1d2e3f4a-5b6c-7d8e-9f0a-1b2c3d4e5f6a] -->
<!-- CLAUDE-ANCHOR: monologue-structure-schema [2e3f4a5b-6c7d-8e9f-0a1b-2c3d4e5f6a7b] -->
<!-- CLAUDE-ANCHOR: monologue-formatting-rules [3f4a5b6c-7d8e-9f0a-1b2c-3d4e5f6a7b8c] -->