import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown file
    with open(from_path, "r") as f:
        markdown_content = f.read()
    
    # Read the template file  
    with open(template_path, "r") as f:
        template = f.read()
    
    # Convert markdown to HTML
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()
    
    # Extract title
    title = extract_title(markdown_content)
    
    # Replace placeholders
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    # Create directory if needed
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    
    # Write the final HTML
    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(content_dir_path, template_path, dest_dir_path):
    """
    Crawls a content directory and generates HTML pages for each markdown file 
    using a given template, writing the results to a destination directory.
    """
    for root, _, files in os.walk(content_dir_path):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, content_dir_path)
                dest_path = os.path.join(dest_dir_path, relative_path.replace(".md", ".html"))
                generate_page(from_path, template_path, dest_path)

