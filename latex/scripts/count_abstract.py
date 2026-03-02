import re
from pathlib import Path

def count_abstract_words(file_path):
    try:
        text = Path(file_path).read_text(encoding='utf-8')
        
        # Ambil konten di dalam environment abstract-id
        match = re.search(r'\\begin{abstract-id}(.*?)\\end{abstract-id}', text, re.DOTALL)
        
        if not match:
            print("Environment abstract-id tidak ditemukan.")
            return

        content = match.group(1)
        
        # Bersihkan perintah LaTeX dasar agar hitungan akurat
        # Hapus perintah \textit{} tapi ambil isinya
        content = re.sub(r'\\textit\{([^}]+)\}', r'\1', content)
        # Hapus perintah \qty{}{} tapi ambil angkanya
        content = re.sub(r'\\qty\{([^}]+)\}\{([^}]+)\}', r'\1', content)
        content = re.sub(r'\\qtyrange\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}', r'\1-\2', content)
        # Hapus command lain yang diawali backslash
        content = re.sub(r'\\[a-zA-Z]+', ' ', content)
        # Hapus kurung kurawal sisa
        content = re.sub(r'[{}]', ' ', content)
        # Hapus karakter non-alphanumeric kecuali spasi dan strip (opsional)
        # content = re.sub(r'[^\w\s-]', '', content)

        words = content.split()
        print(f"--- Statistik Abstrak ---")
        print(f"Jumlah Kata: {len(words)}")
        
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")

if __name__ == "__main__":
    # Sesuaikan path relatif terhadap root workspace
    count_abstract_words("main.tex")