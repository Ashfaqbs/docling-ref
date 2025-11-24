## 1. What is Docling?


> Docling simplifies document processing, parsing diverse formats — including advanced PDF understanding — and providing seamless integrations with the gen AI ecosystem. 


* It’s a **Python library + CLI**.
* It **parses many document types** (PDF, DOCX, PPTX, XLSX, HTML, images, audio transcripts, etc.) into a **unified internal format** called `DoclingDocument`.  
* It then **exports** that into Markdown, HTML, JSON, plain text, or DocTags (a layout-preserving markup format).  
* It’s designed to plug straight into **GenAI / RAG / agent frameworks** (LangChain, LlamaIndex, Haystack, etc.).  

---

## 2. Why was it created?

* Started by the **AI for knowledge team at IBM Research Zurich** and now hosted under the **LF AI & Data Foundation**.  
* Tagline everywhere: *“Get your documents ready for Gen AI.”*  

Working-theory motivation (based on the docs and examples):

* Enterprises are full of **messy PDFs, Office files, scans, and random exports**.
* LLMs + RAG want **structured text, tables, and metadata** in a consistent schema.
* Docling’s job is to be the **strong, boring middle layer**:
  “I will read your 500-page PDF, understand layout, tables, headers/footers, images, etc., and give you a clean, machine-usable representation.”

So: it was created to **standardize document ingestion** for AI workflows, with strong PDF/layout understanding, OCR, and integrations built-in.

---

## 3. Core features from the README


* **Multi-format parsing**

  * PDF, DOCX, PPTX, XLSX, Markdown, HTML/XHTML, CSV
  * Images: PNG, JPEG, TIFF, BMP, WEBP
  * Audio-related text: WebVTT (video subtitles)
  * Specialized XML: USPTO XML (patents), JATS XML (journal articles)
* **Advanced PDF understanding**

  * Page layout & reading order
  * Table structure
  * Code, formulas
  * Image classification
* **Unified representation: `DoclingDocument`**

  * Pydantic data model with:

    * `texts`, `tables`, `pictures`, `key_value_items`
    * `body` and `furniture` (headers/footers etc.) trees
    * Layout information (bounding boxes)
    * Provenance information (where did this content come from in the original)  
* **Export formats**

  * HTML, Markdown, JSON (lossless), plain text, DocTags.  
* **Runs locally**

  * Works on macOS, Linux, Windows, x86_64 + arm64, with optional CPU/GPU acceleration.  
* **OCR + Vision-Language Models**

  * Extensive OCR options for scanned PDFs and images.
  * Supports several VLMs, including **GraniteDocling**.  
* **Audio / ASR support**

  * Can use Automatic Speech Recognition models for audio.  
* **Integrations**

  * Official examples/integrations for LangChain, LlamaIndex, Haystack, Bee Agent Framework, Crew AI, txtai, lots of RAG stacks (Milvus, Qdrant, MongoDB+VoyageAI, Weaviate, OpenSearch, Azure AI Search, etc.).  
* **MCP server**

  * Docling can be exposed via an MCP (Model Context Protocol) server, so any MCP-aware agent can call it.  
* **CLI**

  * Simple `docling` command that converts docs from shell.

---

## 4. Supported input & output formats (from docs)

From the “Supported formats” page:  

**Input formats**

* **General documents**

  * `PDF`
  * `DOCX`, `XLSX`, `PPTX`
  * `Markdown`
  * `AsciiDoc`
  * `HTML`, `XHTML`
  * `CSV`
* **Images**

  * `PNG`, `JPEG`, `TIFF`, `BMP`, `WEBP`
* **Timed text**

  * `WebVTT` (subtitle / caption tracks)
* **Schema-specific / structured**

  * `USPTO XML` (patents)
  * `JATS XML` (articles)
  * `Docling JSON` (serialized DoclingDocument)

**Output formats**

* `HTML`
* `Markdown`
* `JSON` (lossless DoclingDocument)
* `Text` (plain)
* `DocTags` (Docling’s detailed layout+content markup)

That’s exactly the kind of list you check when deciding “can I pipe this weird file into my RAG pipeline?”

---

## 5. Minimal examples (Python + CLI)

### Python example

README shows the basic pattern with `DocumentConverter`:  

```python
from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # path or URL
converter = DocumentConverter()

result = converter.convert(source)

# Export to Markdown (you can also export to HTML, JSON, text, etc.)
markdown_text = result.document.export_to_markdown()
print(markdown_text[:500])  # just peek at first 500 chars
```

Key bits:

* `source` can be a **local file path** or a **URL**.
* `DocumentConverter().convert(source)` returns a result object whose `.document` is a `DoclingDocument`.
* The `DoclingDocument` has convenience methods like `export_to_markdown()`, and you can also serialize to JSON.

There are also “advanced options” and examples for batch conversion, custom pipelines, OCR configs, VLM pipelines, etc., in the docs.  

### CLI example

From the README:  

```bash
# Simple conversion
docling https://arxiv.org/pdf/2206.01062

# Using a VLM pipeline with GraniteDocling
docling --pipeline vlm --vlm-model granite_docling https://arxiv.org/pdf/2206.01062
```

By default it prints converted content (e.g., Markdown) to stdout; you can redirect or use CLI options (see CLI reference in docs).

---

## 6. Typical use cases (where Docling actually shines)

Based on README + examples list:  

1. **RAG over PDFs / Office docs**

   * Ingest PDFs, DOCX, PPTX, XLSX, etc.
   * Convert to `DoclingDocument` → chunk/export to Markdown/JSON → feed into LangChain/LlamaIndex/Haystack and then vector DBs (Milvus, Qdrant, Mongo, etc.).

2. **OCR-heavy workflows**

   * Scanned contracts, invoices, reports as images/PDF.
   * Use OCR integrations (Tesseract, RapidOCR, SuryaOCR) to recover text + layout.

3. **Table & figure extraction**

   * They have explicit examples for table export, figure export, and chunking with layout awareness.
   * Useful if you care about structured tables rather than “flat text soup”.

4. **Information extraction**

   * Structured information extraction feature (beta) plus examples like:

     * Detect & obfuscate PII
     * Extract key-value pairs, structured fields, etc.

5. **Multimodal pipelines**

   * VLM pipelines with GraniteDocling or remote models.
   * Picture annotation examples (local and remote VLM).
   * ASR pipeline with Whisper for audio → text → DoclingDocument.

6. **Serialization, chunking & downstream prep**

   * There are dedicated recipes for:

     * Hybrid chunking & serialization
     * Tokenization & chunking with Data Prep Kit
   * This is basically the “make it RAG-ready” layer.

---

## 7. Important concepts worth reading (beyond README)

If you’re going deeper than copy–paste example:

1. **DoclingDocument concept**

   * Pydantic model representing text, tables, pictures, key/value items, layout, and document hierarchy.
   * Separation between `body` (main content) and `furniture` (headers/footers etc.).
   * This is what you actually store / index / manipulate.  

2. **Supported formats page**

   * When you’re unsure “can it handle this format?”, that’s your canonical reference.  

3. **Examples section**

   * Simple conversion / batch / multi-format
   * RAG with LangChain, LlamaIndex, Haystack, and multiple vector DBs
   * OCR variants, PII obfuscation, translation, CSV & custom XML conversion, etc.  

4. **Integrations**

   * See which frameworks already have ready-made glue (e.g., LangChain, LlamaIndex, spaCy, NVIDIA stack, etc.).  

5. **Technical report**

   * There’s an arXiv technical report linked from README if you want the “why this architecture” deep-dive.  

---

## 8. Quick mental model

For an AI/ML + backend brain:

* Treat Docling as a **document ingestion service**:

  * Input: `{pdf | docx | xlsx | pptx | html | markdown | csv | img | xml | vtt | audio-as-text}`
  * Output: `DoclingDocument` → `{markdown | html | json | doctags | text}`
* Then:

  * Feed to **chunker** + **embedder** → **vector DB**
  * Or to **IE pipeline** → structured fields
  * Or to **multimodal models** via VLM support

It’s the missing pre-processing glue between “dumb files lying on disk” and “LLM actually understands your knowledge base.”
