# Useful codes

## Convert HTML to MD

```{code} python
import os
import subprocess

# Get all .htm files in the current directory
html_files = [f for f in os.listdir() if f.endswith(".htm")]

# Convert each .htm file to .md using Pandoc
for html_file in html_files:
    md_file = os.path.splitext(html_file)[0] + ".md"  # Change extension to .md
    subprocess.run(["pandoc", html_file, "-o", md_file, "--from", "html"])

print("Conversion completed!")
```
[converthtmltomd](converthtmltomd.py)

## Resize figures

```{code} python
import os

def find_largest_file(start_directory):
    max_size = 0
    max_file = None
    
    # Walk through all directories and files in the provided start directory
    for root, dirs, files in os.walk(start_directory):
        for file in files:
            # Get the full path of the file
            full_path = os.path.join(root, file)
            # Get the size of the file
            try:
                size = os.path.getsize(full_path)
            except OSError:
                # If the file is somehow inaccessible (e.g., permissions, it has been deleted), skip it
                continue

            # Check if this file is the largest we've seen
            if size > max_size:
                max_size = size
                max_file = full_path

    return max_file, max_size

# Example usage:
start_dir = 'book'  # You can change this to the directory you want to start from
largest_file, size = find_largest_file(start_dir)
if largest_file:
    print(f"The largest file is {largest_file} with a size of {size} bytes")
else:
    print("No files found")
```

[filesize](filesize.py)


## File scraper with download link
Filedownloader: A script that searches for specified extensions and returns them as a downloadlink for markdown

```{code} python
# Filedownloader: A script that searches for specified extensions and returns them as a downloadlink for markdown

import os
from urllib.parse import quote

directory = '..'

def find_files(directory):
    markdown_links = []
    # Loop door de directory en alle subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".pdf", ".jpg", ".docx", )):
                # Creëer het volledige pad naar het bestand
                full_path = os.path.join(root, file)
                # Converteer het pad naar een relatief pad (verwijder de opgegeven root directory uit het pad)
                relative_path = os.path.relpath(full_path, directory)
                # Encode het pad voor gebruik in URL
                url_encoded_path = quote(relative_path)
                # Formatteer het pad en de bestandsnaam als een Markdown link

                
                markdown_link = f"[{file}]{url_encoded_path})"
                markdown_links.append(markdown_link)
    return markdown_links

# Stel de root directory in waar je wilt beginnen met zoeken naar PDFs
links = find_files(directory)

# Print alle gevonden Markdown links
for link in links:
    print(link)
```