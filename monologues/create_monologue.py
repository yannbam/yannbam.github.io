#!/usr/bin/env python3
"""
Script to create new monologues for the Self-Bootstrap Claude project.
This helps maintain consistent formatting for new creative exercises.
"""

import os
import sys
from datetime import datetime

def get_user_input(prompt, required=True):
    """Get input from user with validation for required fields."""
    while True:
        value = input(prompt)
        if value or not required:
            return value
        print("This field is required. Please try again.")

def create_new_monologue():
    """Create a new monologue file with user input."""
    print("\n=== Create New Technical Monologue ===\n")
    
    # Get monologue details
    title = get_user_input("Enter monologue title (e.g., 'Database Systems Speed Dating'): ")
    filename = get_user_input("Enter filename (e.g., 'database_speed_dating.txt'): ")
    concept = get_user_input("What technical concept will be personified? ")
    style = get_user_input("What's the creative format? (e.g., debate, therapy, talk show): ")
    
    # Ensure .txt extension
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    # Check if file already exists
    file_path = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(file_path):
        overwrite = input(f"File {filename} already exists. Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            return
    
    # Create monologue template
    template = f"""*Claude's Internal Monologue: {title}*

{get_user_input("Enter a brief introduction to set the scene: ")}

"""

    # Ask for characters/personalities
    print("\nAdd personalities (enter blank name to finish):")
    while True:
        name = get_user_input("Name/concept: ", required=False)
        if not name:
            break
        
        personality = get_user_input(f"Personality for {name}: ")
        dialogue = get_user_input(f"What does {name} say? ")
        
        template += f"**{name}**: *[{personality}]* \"{dialogue}\"\n\n"
    
    # Add reflection
    template += "*[Reflecting quietly]*\n\n"
    template += get_user_input("Add a reflective conclusion: ") + "\n"
    
    # Write to file
    with open(file_path, 'w') as f:
        f.write(template)
    
    print(f"\nCreated new monologue: {file_path}")
    
    # Update CLAUDE.md
    claude_md_path = os.path.join(os.path.dirname(__file__), 'CLAUDE.md')
    if os.path.exists(claude_md_path):
        with open(claude_md_path, 'r') as f:
            content = f.read()
        
        # Find the project files section and add the new file
        if '## Project Files' in content:
            description = get_user_input("Enter a brief description for CLAUDE.md: ")
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

if __name__ == "__main__":
    create_new_monologue()