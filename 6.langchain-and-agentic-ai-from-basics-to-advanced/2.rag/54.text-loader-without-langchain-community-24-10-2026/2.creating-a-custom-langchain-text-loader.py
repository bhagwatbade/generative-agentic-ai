from pathlib import Path

from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader


# ========================================
# CUSTOM TEXT LOADER
# ========================================

class SimpleTextLoader(BaseLoader):

    def __init__(
            self,
            file_path,
            encoding="utf-8"
    ):

        self.file_path = Path(file_path)
        self.encoding = encoding

    def lazy_load(self):

        content = self.file_path.read_text(
            encoding=self.encoding
        )

        yield Document(
            page_content=content,
            metadata={
                "source": str(self.file_path)
            }
        )


# ========================================
# CREATE SAMPLE FILE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "library_rules.txt"
)

file_path.write_text(
    "Library opens at 8 AM.\n"
    "Library closes at 6 PM.\n",
    encoding="utf-8"
)


# ========================================
# USE CUSTOM LANGCHAIN LOADER
# ========================================

loader = SimpleTextLoader(
    file_path=file_path
)

documents = loader.load()


# ========================================
# DISPLAY RESULTS
# ========================================

print("RETURN TYPE:", type(documents).__name__)

print("TOTAL DOCUMENTS:", len(documents))

print("DOCUMENT TYPE:", type(documents[0]).__name__)

print("\nCONTENT:")
print(documents[0].page_content.strip())

print("\nSOURCE:")
print(
    Path(
        documents[0].metadata["source"]
    ).name
)