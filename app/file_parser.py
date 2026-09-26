from pathlib import Path

def read_text_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

def read_jd(path: str) -> str:
    p = Path(path)
    suffix = p.suffix.lower()

    if suffix in {".txt", ".md"}:
        return p.read_text(encoding="utf-8")

    if suffix == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise RuntimeError(
                "PDF support requires pypdf. Run: pip install -r requirements.txt"
            ) from exc

        reader = PdfReader(str(p))
        pages = []
        for page in reader.pages:
            pages.append(page.extract_text() or "")
        return "\n".join(pages).strip()

    raise ValueError(
        f"Unsupported JD format: {suffix}. Use .txt, .md, or .pdf."
    )
