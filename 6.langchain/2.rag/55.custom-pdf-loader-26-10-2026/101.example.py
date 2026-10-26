from reportlab.pdfgen import canvas
from pypdf import PdfReader
from langchain_core.documents import Document

pdf_path = 'library_notice7.pdf'
pdf = canvas.Canvas(pdf_path)

pdf.drawString(60, 750, "Library Notice")
pdf.drawString(60, 720, "Library opens at 8 AM")
pdf.drawString(60, 690, "Library closes at 6 PM")

pdf.save()

reader = PdfReader(pdf_path)

page =  reader.pages[0]

document = Document(
    page_content = page.extract_text(),
    metadata = {
        'source' : pdf_path,
        'source_type' : 'pdf',
        'page' : 0,
        'total_pages' : len(reader.pages)
    }
)

print(document.page_content)
print(document.metadata)


