from pathlib import Path
from docling.document_converter import DocumentConverter


def convert_pdf_to_markdown(pdf_path: str, md_out_path: str) -> None:
    pdf_path = Path(pdf_path)
    md_out_path = Path(md_out_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"Input PDF not found: {pdf_path}")

    # 1. Create a converter (uses IBM models under the hood)
    converter = DocumentConverter()

    # 2. Run conversion – this returns a ConversionResult
    result = converter.convert(pdf_path)

    # 3. Get the structured DoclingDocument
    doc = result.document

    # 4. Export to Markdown (you can also export JSON/HTML/DocTags)
    markdown_str = doc.export_to_markdown()

    # 5. Save to disk
    md_out_path.write_text(markdown_str, encoding="utf-8")

    print(f"Converted {pdf_path} → {md_out_path}")
    print("\n--- Preview (first 500 chars) ---\n")
    print(markdown_str[:500])


if __name__ == "__main__":
    convert_pdf_to_markdown(
        pdf_path="sample.pdf",
        md_out_path="output.md",
    )
