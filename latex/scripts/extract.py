import os
import sys

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    print("Error: 'pypdf' library is not installed.")
    print("Please install it using: uv pip install pypdf")
    sys.exit(1)

def extract_pages(input_path, output_path, pages_to_extract):
    """
    Extract specific pages from a PDF file.
    
    Args:
        input_path (str): Path to the source PDF file.
        output_path (str): Path to the destination PDF file.
        pages_to_extract (list): List of 1-based page numbers to extract.
    """
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return

    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()
        
        extracted_count = 0
        
        for page_num in pages_to_extract:
            # Convert 1-based index to 0-based index
            idx = page_num - 1
            
            if 0 <= idx < len(reader.pages):
                writer.add_page(reader.pages[idx])
                extracted_count += 1
            else:
                print(f"Warning: Page {page_num} is out of range (Total pages: {len(reader.pages)})")
        
        if extracted_count > 0:
            with open(output_path, "wb") as f:
                writer.write(f)
            print(f"Successfully extracted {extracted_count} pages to '{output_path}'")
        else:
            print("No pages were extracted.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Configuration
    INPUT_FILE = "test_word.pdf"
    OUTPUT_FILE = "extracted_pages.pdf"
    
    # Pages to extract (1-based index as requested)
    # 1, 2, 4, 5, 7, 10, 12, 13, 16, 25
    PAGES = [
        1, 2, 4, 5, 7, 10, 12, 13, 16, 25
    ]
    
    # Sort pages just in case, though order usually matters for output. 
    # The user listed them in order, so we keep that order.
    
    print(f"Extracting pages: {PAGES}")
    extract_pages(INPUT_FILE, OUTPUT_FILE, PAGES)
