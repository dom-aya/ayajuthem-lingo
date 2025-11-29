import os
import json

# Configuration
LESSONS_DIR = os.path.join("assets", "lessons")
MANIFEST_FILE = "manifest.json"

def generate_manifest():
    manifest = []
    
    if not os.path.exists(LESSONS_DIR):
        print(f"Error: Directory '{LESSONS_DIR}' not found.")
        return

    # List all CSV files in the directory
    files = [f for f in os.listdir(LESSONS_DIR) if f.endswith('.csv')]
    files.sort() # Ensure they are in order

    print(f"Found {len(files)} lesson files.")

    for filename in files:
        # Create a readable title from filename
        # Example: "01_Greetings.csv" -> "Greetings"
        title = filename.replace('.csv', '')
        # Remove leading numbers and underscores (e.g. 01_)
        if '_' in title:
            parts = title.split('_')
            # If first part is a number, drop it
            if parts[0].isdigit():
                parts.pop(0)
            title = ' '.join(parts)
        
        # Add to manifest list
        entry = {
            "file": os.path.join(LESSONS_DIR, filename).replace("\\", "/"), # Ensure web-friendly slashes
            "title": title
        }
        manifest.append(entry)
        print(f" - Added: {title}")

    # Write to JSON file
    with open(MANIFEST_FILE, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\nSuccess! '{MANIFEST_FILE}' has been updated.")

if __name__ == "__main__":
    generate_manifest()
    input("Press Enter to exit...")