from pathlib import Path
from docling.document_converter import DocumentConverter


def docx_to_markdown(docx_path: str, md_out_path: str | None = None) -> None:
    docx_path = Path(docx_path)

    if not docx_path.exists():
        raise FileNotFoundError(f"Input DOCX not found: {docx_path}")

    # 1. Converter – will pick the right backend / pipeline for DOCX
    converter = DocumentConverter()

    # 2. Convert the DOCX
    result = converter.convert(docx_path)
    doc = result.document  # DoclingDocument

    # 3. Export to Markdown
    markdown_str = doc.export_to_markdown()

    # 4. Output path
    if md_out_path is None:
        md_out_path = docx_path.with_suffix(".md")
    md_out_path = Path(md_out_path)
    md_out_path.write_text(markdown_str, encoding="utf-8")

    print(f"Converted {docx_path} → {md_out_path}")
    print("\n--- Preview (first 500 chars) ---\n")
    print(markdown_str[:500])


if __name__ == "__main__":
    docx_to_markdown(
        docx_path="input/sample.docx",  
        md_out_path=None,          # auto: sample.md
    )
