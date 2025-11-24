from pathlib import Path
from urllib.parse import urlparse
import tempfile

import requests
from docling.document_converter import DocumentConverter


def webpage_to_markdown(url: str, md_out_path: str | None = None) -> None:
    # 1. Fetching the HTML content from the URL
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/129.0.0.0 Safari/537.36"
        )
    }
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    html_text = resp.text

    # 2. Write HTML to a temporary file, so Docling sees it as a .html document
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as tmp:
        tmp_path = Path(tmp.name)
        tmp.write(html_text.encode("utf-8"))

    # 3. Run Docling on the HTML file
    converter = DocumentConverter()
    result = converter.convert(tmp_path)

    doc = result.document
    markdown_str = doc.export_to_markdown()

    # 4. Decide output markdown path
    if md_out_path is None:
        parsed = urlparse(url)
        base_name = (Path(parsed.path).name or "page").split("?")[0] or "page"
        md_out_path = f"{base_name}.md"

    md_out_path = Path(md_out_path)
    md_out_path.write_text(markdown_str, encoding="utf-8")

    print(f"Converted HTML from {url} → {md_out_path}")
    print("\n--- Preview (first 500 chars) ---\n")
    print(markdown_str[:500])


if __name__ == "__main__":
    webpage_to_markdown(
        url="https://en.wikipedia.org/wiki/Graph_(abstract_data_type)",
        md_out_path=None,
    )
