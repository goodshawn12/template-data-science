import os


def generate_readme(root_dir):
    readme_content = "# Project Structure\n\n"

    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 2 * (level)

        # Ignore directories starting with . or _, unless it's the root directory
        if level > 0 and os.path.basename(root).startswith((".", "_")):
            dirs[:] = []  # ignore sub-directories
            files[:] = []  # ignore files
        elif root != root_dir:  # only add to readme_content if not root_dir
            readme_content += '{}- {}/\n'.format(indent, os.path.basename(root))

        subindent = ' ' * 2 * (level + 1)
        for f in files:
            # Ignore files starting with . or _
            if not f.startswith((".", "_")):
                readme_content += '{}- {}\n'.format(subindent, f)

    with open('README.md', 'w') as f:
        f.write(readme_content)


if __name__ == "__main__":
    generate_readme('.')