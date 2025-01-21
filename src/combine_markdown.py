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

def is_valid_file(filepath, output_file):
    """
    Check if a file should be included in the combination.
    Valid files are .md or .txt files that are not the output file itself or any master.md file.
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
    
    return has_valid_extension and is_not_master and is_not_output

def collect_markdown_files(directory, reading_order=None, output_file=None):
    """
    Collect markdown (.md) and text (.txt) files from the specified directory.
    If reading_order is provided, files are ordered accordingly.
    Files not in reading_order are appended at the end.
    Ignores master.md files and the output file itself.
    """
    if reading_order:
        # Create a map of filenames to their full paths
        file_map = {}
        for root, _, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                if is_valid_file(full_path, output_file):
                    file_map[file] = full_path
                    # Also map the relative path
                    rel_path = os.path.relpath(full_path, directory)
                    file_map[rel_path] = full_path

        # First, collect files in the specified order
        ordered_files = []
        for entry in reading_order:
            doc_path = entry['document']
            if doc_path in file_map:
                ordered_files.append(file_map[doc_path])
            else:
                print(f"Warning: Specified file '{doc_path}' not found in repository")

        # Then collect any remaining valid files
        remaining_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                if is_valid_file(full_path, output_file) and full_path not in ordered_files:
                    remaining_files.append(full_path)

        return ordered_files + remaining_files
    else:
        # Original behavior when no reading_order is provided
        valid_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                if is_valid_file(full_path, output_file):
                    valid_files.append(full_path)
        return sorted(valid_files)  # Sort to ensure consistent order

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