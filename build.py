#!/usr/bin/env python3
import os
import shutil

# Define file paths
HEADER_FILE = "header.html"
FOOTER_FILE = "footer.html"
TEMPLATE_FILE = "template.html"
CONTENT_DIR = "content"
DRAFTS_DIR = "drafts"  # Directory to ignore
CSS_DIR = "css"  # Source CSS directory
JS_DIR = "js"  # Source JS directory
IMAGES_DIR = "images"  # Source Images directory
OUTPUT_DIR = "public"

OUTPUT_CSS_DIR = os.path.join(OUTPUT_DIR, "css")  # Destination CSS directory
OUTPUT_JS_DIR = os.path.join(OUTPUT_DIR, "js")  # Destination JS directory
OUTPUT_IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")

# Ensure output and CSS/JS/IMAGES directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_CSS_DIR, exist_ok=True)
os.makedirs(OUTPUT_JS_DIR, exist_ok=True)
os.makedirs(OUTPUT_IMAGES_DIR, exist_ok=True)

# Copy CSS files to output directory and generate <link> tags
css_links = ""
if os.path.exists(CSS_DIR):
    css_files = sorted(f for f in os.listdir(CSS_DIR) if f.endswith(".css"))  # Ensure order

    for css_file in css_files:
        src_path = os.path.join(CSS_DIR, css_file)
        dest_path = os.path.join(OUTPUT_CSS_DIR, css_file)

        shutil.copy2(src_path, dest_path)  # Copy while preserving metadata
        print(f"Copied CSS: {css_file}")
        css_links += f'<link rel="stylesheet" href="/css/{css_file}">\n'

# Copy JS files to output directory and generate <script> tags
js_scripts = ""
if os.path.exists(JS_DIR):
    js_files = sorted(f for f in os.listdir(JS_DIR) if f.endswith(".js"))  # Ensure order

    for js_file in js_files:
        src_path = os.path.join(JS_DIR, js_file)
        dest_path = os.path.join(OUTPUT_JS_DIR, js_file)

        shutil.copy2(src_path, dest_path)  # Copy while preserving metadata
        print(f"Copied JS: {js_file}")
        js_scripts += f'<script src="/js/{js_file}"></script>\n'

# Copy image files (any common image format)
if os.path.exists(IMAGES_DIR):
    for root, _, files in os.walk(IMAGES_DIR):
        if root.startswith(IMAGES_DIR + '/' + DRAFTS_DIR):  # Skip drafts directory
            print(f'Skipped {root}')
            continue

        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")):
                src_path = os.path.join(root, file)
                relative_path = os.path.relpath(src_path, IMAGES_DIR)
                dest_path = os.path.join(OUTPUT_IMAGES_DIR, relative_path)

                # Ensure destination subdirectory exists
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                shutil.copy2(src_path, dest_path)
                print(f"Copied image: {relative_path}")

# Read template, header, and footer
with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
    template = f.read()

with open(HEADER_FILE, "r", encoding="utf-8") as f:
    header = f.read()

with open(FOOTER_FILE, "r", encoding="utf-8") as f:
    footer = f.read()

# Process each file inside CONTENT (excluding drafts/)
for root, _, files in os.walk(CONTENT_DIR):
    if root.startswith(CONTENT_DIR + '/' + DRAFTS_DIR):  # Skip drafts directory
        print(f'Skipped {root}')
        continue

    for file in files:
        if file.endswith(".html"):
            content_path = os.path.join(root, file)

            # Preserve folder structure in OUTPUT dir
            relative_path = os.path.relpath(content_path, CONTENT_DIR)
            output_path = os.path.join(OUTPUT_DIR, relative_path)
            output_dir = os.path.dirname(output_path)

            # Ensure the output subdirectory exists
            os.makedirs(output_dir, exist_ok=True)

            with open(content_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Generate HTML with template
            final_html = template.replace("{{ title }}", file.replace('.html', '').capitalize()) \
                                 .replace("{{ css }}", css_links) \
                                 .replace("{{ js }}", js_scripts) \
                                 .replace("{{ header }}", header) \
                                 .replace("{{ content }}", content) \
                                 .replace("{{ footer }}", footer)

            # Write output file
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(final_html)

            print(f"Generated: {output_path}")

print("Build complete!")

