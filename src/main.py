import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

def main():
    """Main function to orchestrate the static site generation."""
    dir_path_static = "./static"
    dir_path_public = "./public"
    dir_path_content = "./content"
    template_path = "./template.html"

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        try:
            shutil.rmtree(dir_path_public)
        except OSError as e:
            print(f"Error deleting {dir_path_public}: {e}")
            return

    print("Copying static files to public directory...")
    try:
        copy_files_recursive(dir_path_static, dir_path_public)
    except Exception as e:
        print(f"Error copying static files: {e}")
        return

    print("Generating pages recursively...")
    try:
        generate_pages_recursive(dir_path_content, template_path, dir_path_public)
    except Exception as e:
        print(f"Error generating pages: {e}")
        return

    print("Build complete!")


if __name__ == "__main__":
    main()