import re
import os

def clean_markdown_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Regular expression to remove everything after ) including the {}
            cleaned_content = re.sub(r'\)\{.*?\}', ')', content)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_content)

# Example usage
directory = '.'  # Replace with your actual directory path
clean_markdown_files(directory)
