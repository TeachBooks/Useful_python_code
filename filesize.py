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
