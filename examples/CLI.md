(venv) PS C:\tmp\git\docling-ref\examples> mkdir .\output


    Directory: C:\tmp\git\docling-ref\examples


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        11/24/2025   6:37 AM                output


(venv) PS C:\tmp\git\docling-ref\examples> docling .\input\sample.docx --output .\output
2025-11-24 06:37:49,292 - INFO - Loading plugin 'docling_defaults'
2025-11-24 06:37:49,294 - INFO - Registered ocr engines: ['auto', 'easyocr', 'ocrmac', 'rapidocr', 'tesserocr', 'tesseract']
2025-11-24 06:37:49,325 - INFO - paths: [WindowsPath('C:/Users/ashfa/AppData/Local/Temp/tmpu6_phgju/sample.docx')]
2025-11-24 06:37:49,342 - INFO - detected formats: [<InputFormat.DOCX: 'docx'>]
2025-11-24 06:37:49,350 - INFO - Going to convert document batch...
2025-11-24 06:37:49,350 - INFO - Initializing pipeline for SimplePipeline with options hash 995a146ad601044538e6a923bea22f4e   
2025-11-24 06:37:49,372 - INFO - Loading plugin 'docling_defaults'
2025-11-24 06:37:49,376 - INFO - Registered picture descriptions: ['vlm', 'api']
2025-11-24 06:37:49,376 - INFO - Processing document sample.docx
2025-11-24 06:37:49,483 - INFO - Finished converting document sample.docx in 0.16 sec.
2025-11-24 06:37:49,483 - INFO - writing Markdown output to output\sample.md
2025-11-24 06:37:49,532 - INFO - Processed 1 docs, of which 0 failed
2025-11-24 06:37:49,532 - INFO - All documents were converted in 0.21 seconds.
(venv) PS C:\tmp\git\docling-ref\examples> 




(venv) PS C:\tmp\git\docling-ref\examples> ls .\input\


    Directory: C:\tmp\git\docling-ref\examples\input


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        11/24/2025   6:29 AM            133 sample.csv
-a----        11/24/2025   6:21 AM          34375 sample.docx
-a----        11/24/2025   6:29 AM            340 sample.md


(venv) PS C:\tmp\git\docling-ref\examples> ls .\output\


    Directory: C:\tmp\git\docling-ref\examples\output


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        11/24/2025   6:37 AM          22205 sample.md


(venv) PS C:\tmp\git\docling-ref\examples> 



