from pathlib import Path
from docling.document_converter import DocumentConverter


def csv_to_markdown(csv_path: str, md_out_path: str | None = None) -> None:
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {csv_path}")

    converter = DocumentConverter()

    # Docling will detect InputFormat.CSV internally
    result = converter.convert(csv_path)
    doc = result.document

    markdown_str = doc.export_to_markdown()

    if md_out_path is None:
        md_out_path = csv_path.with_suffix(".md")

    md_out_path = Path(md_out_path)
    md_out_path.write_text(markdown_str, encoding="utf-8")

    print(f"✅ Converted {csv_path} → {md_out_path}")
    print("\n--- Preview (first 500 chars) ---\n")
    print(markdown_str[:500])


if __name__ == "__main__":
    csv_to_markdown(
        csv_path="input/sample.csv",
        md_out_path=None,  # becomes sample.md
    )
