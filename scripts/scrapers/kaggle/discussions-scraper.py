import os
import sys
from bs4 import BeautifulSoup
import html2text


def extract_html(file_path: str, output_file: str):
    """
    Extracts specific HTML content from a file and converts it to Markdown.

    Args:
    - file_path (str): Path to the input HTML file on the local system.
    - output_file (str): Path to the output Markdown file where the result will be saved.

    This function reads the HTML file, parses it with BeautifulSoup, and extracts the
    content from the second div inside the `#site-content` container. Then, it converts
    the extracted HTML content to Markdown format using the `html2text` library,
    and saves it to the specified output file.

    Raises:
    - FileNotFoundError: If the HTML file is not found at the provided file_path.
    - ValueError: If the expected HTML structure is not found.
    """
    # Read the HTML file from disk
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"Error: HTML file '{file_path}' not found!")
        sys.exit(1)

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the site-content container and select the second div inside it
    site_container = soup.find("div", id="site-content")
    if not site_container:
        print("Error: Site container not found!")
        sys.exit(1)

    site_container_divs = site_container.find_all("div")
    if len(site_container_divs) < 2:
        print("Error: Insufficient number of divs inside the site container.")
        sys.exit(1)

    # Extract HTML of the second div inside site-container
    html_content = str(site_container_divs[1])

    # Convert HTML content to Markdown using html2text
    converter = html2text.HTML2Text()
    converter.ignore_links = False  # Set to True to ignore links during conversion

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Write the converted Markdown content to the output file
    with open(output_file, "w") as file_pointer:
        file_pointer.write(converter.handle(html_content))


def main():
    """
    Main function to handle command-line arguments and initiate HTML extraction and conversion.

    The script expects two command-line arguments:
    - The path to the HTML file to be read
    - The path to the output Markdown file where the converted content will be saved
    """
    if len(sys.argv) != 3:
        print("Usage: python discussions-scraper.py <path-to-html-file> <output-markdown-file>")
        sys.exit(1)

    file_path = sys.argv[1]  # Path to the HTML file
    output_file = sys.argv[2]  # Path to the output Markdown file

    extract_html(file_path=file_path, output_file=output_file)


# Run the script when executed from the command line
if __name__ == "__main__":
    main()
