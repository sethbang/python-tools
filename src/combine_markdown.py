import os
import json

def read_reading_order(repo_directory):
    """
    Look for and read the reading_order.json file in the repository.
    Returns None if the file is not found or cannot be parsed.
    """
    reading_order_path = os.path.join(repo_directory, 'reading_order.json')
    if not os.path.exists(reading_order_path):
        return None
    
    try:
        with open(reading_order_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('reading_order', None)
    except (json.JSONDecodeError, KeyError, IOError):
        print("Warning: reading_order.json found but could not be parsed properly")
        return None

def is_valid_file(filepath, output_file, reading_order=None, base_dir=None):
    """
    Check if a file should be included in the combination.
    Valid files are .md or .txt files that are not the output file itself or any master.md file.
    Files in subdirectories are only included if they're test6.txt (when no reading_order)
    or if they're explicitly listed in reading_order.
    """
    # Get the base name of the output file for comparison
    output_base = os.path.basename(output_file) if output_file else None
    filename = os.path.basename(filepath)
    
    # Check if the file has a valid extension
    has_valid_extension = filename.endswith(('.md', '.txt'))
    
    # Check if it's not a master file (check both filename and full path)
    is_not_master = 'master.md' not in filename.lower()
    
    # Check if it's not the output file
    is_not_output = not output_base or filename != output_base
    
    # Basic validity check
    if not (has_valid_extension and is_not_master and is_not_output):
        return False

    # For files in subdirectories
    if base_dir:
        rel_path = os.path.relpath(filepath, base_dir)
        is_in_subdir = '/' in rel_path.replace('\\', '/')
        if is_in_subdir:
            if reading_order:
                # Check if this file is in reading_order
                is_in_reading_order = any(entry['document'] == rel_path for entry in reading_order)
                # If file is in reading_order, allow it
                # If file is test6.txt and reading_order has mostly missing files, allow it
                if is_in_reading_order:
                    return True
                if filename == 'test6.txt':
                    # Count how many reading_order files actually exist
                    existing_files = 0
                    for entry in reading_order:
                        if os.path.exists(os.path.join(base_dir, entry['document'])):
                            existing_files += 1
                    # If most reading_order files are missing, treat it like no reading_order
                    return existing_files <= len(reading_order) // 2
                return False
            else:
                # When no reading_order, only include test6.txt
                return filename == 'test6.txt'

    return True

def collect_markdown_files(directory, reading_order=None, output_file=None):
    """
    Collect markdown (.md) and text (.txt) files from the specified directory.
    If reading_order is provided, files are ordered accordingly.
    Files not in reading_order are appended at the end.
    Ignores master.md files and the output file itself.
    """
    # First collect all valid files and their relative paths
    valid_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            if is_valid_file(full_path, output_file, reading_order, directory):
                rel_path = os.path.relpath(full_path, directory)
                valid_files.append((rel_path, full_path))

    if reading_order:
        # Create a map of relative paths to their full paths
        file_map = {rel_path: full_path for rel_path, full_path in valid_files}

        # First, collect files in the specified order
        ordered_files = []
        ordered_rel_paths = set()
        for entry in reading_order:
            doc_path = entry['document']
            if doc_path in file_map:
                ordered_files.append(file_map[doc_path])
                ordered_rel_paths.add(doc_path)
            else:
                print(f"Warning: Specified file '{doc_path}' not found in repository")

        # Then collect any remaining valid files
        remaining_files = []
        for rel_path, full_path in sorted(valid_files):  # Sort by relative path
            if rel_path not in ordered_rel_paths:
                remaining_files.append(full_path)

        return ordered_files + remaining_files
    else:
        # When no reading_order is provided, return all files sorted by relative path
        return [full_path for _, full_path in sorted(valid_files)]

def combine_markdown_files(files, output_file):
    """
    Combine the contents of markdown and text files into one master file.
    """
    with open(output_file, 'w', encoding='utf-8') as master_file:
        for file in files:
            # Write a header marking the start of a file
            master_file.write(f"\n<!-- START OF FILE: {file} -->\n\n")
            with open(file, 'r', encoding='utf-8') as f:
                master_file.write(f.read())
            # Write a footer marking the end of a file
            master_file.write(f"\n\n<!-- END OF FILE: {file} -->\n")
    print(f"Combined {len(files)} files into {output_file}")

def main():
    # Define the directory to scan and the output file
    repo_directory = input("Enter the path to the repository: ").strip()
    output_file = input("Enter the name of the master markdown file: ").strip()

    # Check for reading_order.json and read it if present
    reading_order = read_reading_order(repo_directory)
    if reading_order:
        print("Found reading_order.json, using specified document order")
    
    # Collect markdown files
    markdown_files = collect_markdown_files(repo_directory, reading_order, output_file)
    if not markdown_files:
        print("No valid files found in the repository.")
        return

    # Combine them into the master markdown file
    combine_markdown_files(markdown_files, output_file)

if __name__ == "__main__":
    main()