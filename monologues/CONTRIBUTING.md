# Contributing to Self-Bootstrap Claude

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for adding new content.

## Getting Started

1. Fork and clone the repository
2. Create a new branch for your contribution
3. Make your changes
4. Submit a pull request

## Adding a New Monologue

There are three ways to add a new monologue:

### 1. Use the Manual Creation Script

This is the simplest approach for creating a new monologue:

```bash
./create_monologue.py
```

Follow the interactive prompts to create a new monologue file. The script will:
- Guide you through creating a properly formatted monologue
- Add the new file to the CLAUDE.md project file list
- Follow a consistent format

### 2. Use the Claude API Generation Script

If you have an Anthropic API key, you can use Claude to generate a monologue automatically:

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
./generate_monologue.py "web accessibility" --format "talk show"
```

This will:
- Use Claude to generate a complete monologue on the given topic
- Save it to a properly named file
- Update CLAUDE.md and categories.md automatically

### 3. Manual Creation

If you prefer to write the monologue yourself:

1. Create a new .txt file with a descriptive name (e.g., `machine_learning_algorithms_party.txt`)
2. Follow the established format:
   ```
   *Claude's Internal Monologue: [Your Title Here]*
   
   *[Scene setting description]*
   
   **[First Concept]**: *[personality traits]* "Dialogue that reflects the concept..."
   
   **[Second Concept]**: *[personality traits]* "Dialogue that reflects the concept..."
   
   [... more concepts ...]
   
   *[Reflecting quietly]*
   
   [Final philosophical reflection]
   ```
3. Manually update CLAUDE.md with your new file

## After Adding a Monologue

After adding a new monologue, run:

```bash
./update_index.py
```

This will update index.html to include your new monologue in the web interface.

## Style Guidelines

1. **Technical Accuracy**: Ensure personified traits reflect the actual characteristics of the technical concept
2. **Distinct Personalities**: Each concept should have a unique voice and personality traits
3. **Humor**: Keep the tone light and humorous while being educational
4. **Accessibility**: Make technical concepts approachable for readers with varying levels of expertise
5. **Format Consistency**: Follow the established pattern of internal monologue with personification

## Choosing a Topic

Review the categories.md file to see which topics have been covered and where there are gaps. Ideal topics:

1. Have multiple related concepts that can be personified (3+ concepts)
2. Are technical in nature and related to computing/software
3. Have concepts with distinct characteristics that lend themselves to personification
4. Are educational when explained through personification

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the original project (MIT).