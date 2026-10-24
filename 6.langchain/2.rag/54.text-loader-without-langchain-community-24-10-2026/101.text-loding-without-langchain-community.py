from pathlib import Path
from langchain_core.documents import Document
file_path = Path('student_rules.txt')

document = Document(
    page_content = file_path.read_text(encoding='utf-8'),
    metadata = {'source' : str(file_path)},
)
print(document.page_content)
print(document.metadata)
