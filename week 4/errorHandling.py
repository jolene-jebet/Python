#!/usr/bin/env python3
import os
from pathlib import Path

def modify_content(text):
    """Add line numbers and convert to title case"""
    lines = text.splitlines()
    modified = []
    
    for i, line in enumerate(lines, 1):
        if line.strip():
            modified.append(f"{i:03d}: {line.title()}")
        else:
            modified.append(f"{i:03d}: ")
    
    return "\n".join(modified)

def process_file():
    """Main file processing function"""
    while True:
        filename = input("\nEnter filename (or 'quit'): ").strip()
        
        if filename.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            # Check if file exists
            if not os.path.exists(filename):
                print(f"Error: '{filename}' not found!")
                continue
            
            # Read file
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.strip():
                print("Warning: File is empty!")
                continue
            
            # Modify content
            modified_content = modify_content(content)
            
            # Create output filename
            base_name = Path(filename).stem
            extension = Path(filename).suffix
            output_file = f"{base_name}_modified{extension}"
            
            # Write modified file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            
            print(f"Success! Created '{output_file}'")
            
        except PermissionError:
            print("Error: Permission denied - file may be open elsewhere")
        except UnicodeDecodeError:
            print("Error: Cannot read file - may be binary or wrong encoding")
        except Exception as e:
            print(f"Unexpected error: {e}")

def create_sample():
    """Create a test file"""
    sample_text = """hello world
this is a test file
it has multiple lines

and this is the end"""
    
    with open("sample.txt", "w") as f:
        f.write(sample_text)
    print("Created 'sample.txt' for testing!")

if __name__ == "__main__":
    print("File Processor")
    print("=" * 20)
    
    if input("Create sample file? (y/n): ").lower() == 'y':
        create_sample()
    
    process_file()