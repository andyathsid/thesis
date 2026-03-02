import sys
from pathlib import Path
import fitz  # PyMuPDF


def count_pages_with_images(pdf_path: str) -> tuple[int, int, list[int]]:
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    pages_with_images = []

    for page_num in range(total_pages):
        page = doc[page_num]
        images = page.get_images(full=True)
        if images:
            pages_with_images.append(page_num + 1)

    doc.close()
    return total_pages, len(pages_with_images), pages_with_images


def main():
    pdf_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("main.pdf")

    if not pdf_path.exists():
        print(f"File tidak ditemukan: {pdf_path}")
        sys.exit(1)

    total, colored_count, colored_pages = count_pages_with_images(str(pdf_path))

    bw_count = total - colored_count
    colored_pct = colored_count / total * 100 if total else 0
    bw_pct = bw_count / total * 100 if total else 0

    print(f"File                : {pdf_path}")
    print(f"Total halaman       : {total}")
    print(f"Halaman berwarna    : {colored_count} ({colored_pct:.1f}%)")
    print(f"Halaman hitam-putih : {bw_count} ({bw_pct:.1f}%)")
    print(f"Daftar halaman berwarna: {colored_pages}")


if __name__ == "__main__":
    main()