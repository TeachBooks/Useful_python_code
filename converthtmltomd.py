import os
import subprocess

# Get all .htm files in the current directory
html_files = [f for f in os.listdir() if f.endswith(".htm")]

# Convert each .htm file to .md using Pandoc
for html_file in html_files:
    md_file = os.path.splitext(html_file)[0] + ".md"  # Change extension to .md
    subprocess.run(["pandoc", html_file, "-o", md_file, "--from", "html"])

print("Conversion completed!")