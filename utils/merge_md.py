import os


def merge_markdown_files(directory_path, output_file):
    # Getting all markdown files and sorting them alphabetically
    markdown_files = sorted(
        [f for f in os.listdir(directory_path) if f.endswith('.md')])

    with open(output_file, 'w') as outfile:
        for i, filename in enumerate(markdown_files):
            filepath = os.path.join(directory_path, filename)
            with open(filepath, 'r') as infile:
                # Add a separator and filename as header for clarity
                if i > 0:  # Add separator only after the first file
                    outfile.write('\n\n---\n\n')
                outfile.write(f'# {filename}\n\n')

                # Write the content of the file
                outfile.write(infile.read())


# Example usage
directory_path = './endpoints'
output_file = './nba_live_endpoints.md'
merge_markdown_files(directory_path, output_file)
