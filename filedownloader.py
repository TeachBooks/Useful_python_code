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