from pathlib import Path

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document


class SimpleTextLoader(BaseLoader):
    def __init__(self, file_path, encoding="utf-8"):
        self.file_path = Path(file_path)
        self.encoding = encoding

    def lazy_load(self):
        content = self.file_path.read_text(
            encoding=self.encoding
        )

        yield Document(
            page_content=content,
            metadata={"source": str(self.file_path)}
        )


loader = SimpleTextLoader(file_path="student_rules.txt")

documents = loader.load()

print(type(documents))

document = documents[0]

print(document.page_content)
print(document.metadata)