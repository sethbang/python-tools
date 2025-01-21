import os
import argparse
from reportlab.pdfgen import canvas
import json
import yaml
from jinja2 import Template


def generate_directory_structure(startpath, max_depth):
    structure = []
    start_level = startpath.count(os.sep)
    for root, dirs, files in os.walk(startpath):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not is_hidden(d)]
        files = [f for f in files if not is_hidden(f)]   # Skip hidden files

        level = root.count(os.sep) - start_level
        if max_depth != -1 and level > max_depth:
            continue
        if is_hidden(os.path.basename(root)):
            continue  # Skip hidden root

        indent = ' ' * 4 * level
        structure.append({'dir': os.path.basename(
            root), 'level': level, 'files': files, 'subdirs': dirs})
    return structure


def describe_directory_in_natural_language(structure):
    description = []
    for item in structure:
        dir_name = item['dir']
        num_files = len(item['files'])
        num_subdirs = len(item['subdirs'])
        indent = ' ' * 4 * item['level']

        description.append(
            f"{indent}The directory '{dir_name}' contains {num_files} files and {num_subdirs} subdirectories.")
        if num_files > 0:
            file_list = ', '.join([f"'{file}'" for file in item['files']])
            description.append(
                f"{indent} The list of files includes: {file_list}.")
        if num_subdirs > 0:
            subdir_list = ', '.join(
                [f"'{subdir}'" for subdir in item['subdirs']])
            description.append(
                f"{indent} The subdirectories are: {subdir_list}.")

    return '\n'.join(description)


def save_to_file(structure, filename, format):
    if format == 'pdf':
        save_to_pdf(structure, filename)
    elif format in ['txt', 'natural']:
        if format == 'txt':
            content = '\n'.join([str(item) for item in structure])
        else:
            content = describe_directory_in_natural_language(structure)
        with open(filename + '_' + format[0] + '.txt', 'w') as f:
            f.write(content)
    elif format == 'html':
        template = Template(
            '<html><body><pre>{{ content }}</pre></body></html>')
        rendered = template.render(content='\n'.join(
            [str(item) for item in structure]))
        with open(filename + '.html', 'w') as f:
            f.write(rendered)
    elif format == 'json':
        with open(filename + '.json', 'w') as f:
            json.dump(structure, f, indent=4)
    elif format == 'yaml':
        with open(filename + '.yaml', 'w') as f:
            yaml.dump(structure, f)


def save_to_pdf(structure, filename):
    c = canvas.Canvas(filename + '.pdf')
    textobject = c.beginText(40, 800)
    textobject.setFont("Times-Roman", 12)

    for item in structure:
        line = ' ' * 4 * item['level'] + f"{item['dir']}/"
        textobject.textLine(line)
        for file in item['files']:
            file_line = ' ' * 4 * (item['level'] + 1) + file
            textobject.textLine(file_line)

    c.drawText(textobject)
    c.save()


def save_all_formats(structure, filename):
    output_dir = "trees"
    os.makedirs(output_dir, exist_ok=True)
    formats = ['txt', 'html', 'pdf', 'json', 'yaml', 'natural']

    for fmt in formats:
        save_to_file(structure, os.path.join(output_dir, filename), fmt)


def is_hidden(path):
    return path.startswith('.')


def main():
    parser = argparse.ArgumentParser(
        description="Generate directory structure in different formats.")
    parser.add_argument("-p", "--path", default=".",
                        help="Path to the repository, defaults to current directory")
    parser.add_argument("-o", "--output", default="directory_structure",
                        help="Output file name without extension, defaults to 'directory_structure'")
    parser.add_argument("-f", "--format", choices=['txt', 'html', 'pdf',
                        'json', 'yaml', 'natural', '*'], default='txt', help="Output format")
    parser.add_argument("-d", "--depth", type=int, default=-1,
                        help="Maximum depth for mapping, -1 for unlimited, defaults to -1")

    args = parser.parse_args()

    structure = generate_directory_structure(args.path, args.depth)

    if args.format == '*':
        save_all_formats(structure, args.output)
    else:
        save_to_file(structure, args.output, args.format)


if __name__ == "__main__":
    main()
