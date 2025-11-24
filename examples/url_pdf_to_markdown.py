from pathlib import Path
from urllib.parse import urlparse
from docling.document_converter import DocumentConverter


def url_to_markdown(url: str, md_out_path: str | None = None) -> None:
    # If user didn't specify, derive a simple filename from the URL
    if md_out_path is None:
        parsed = urlparse(url)
        # Take last path segment or fallback
        name = (Path(parsed.path).name or "document").split("?")[0] or "document"
        if not name:
            name = "document"
        md_out_path = f"{name}.md"

    md_out_path = Path(md_out_path)

    converter = DocumentConverter()

    #   Key difference from the PDF example:
    #    here we pass the URL string directly.
    result = converter.convert(url)

    doc = result.document
    markdown_str = doc.export_to_markdown()

    md_out_path.write_text(markdown_str, encoding="utf-8")

    print(f"Converted {url} → {md_out_path}")
    print("\n--- Preview (first 500 chars) ---\n")
    print(markdown_str[:500])


if __name__ == "__main__":
    url_to_markdown(
        url="https://arxiv.org/pdf/2408.09869",  # or any other PDF/HTML URL
        md_out_path=None,  # let the function pick a name, or set "output.md"
    )
