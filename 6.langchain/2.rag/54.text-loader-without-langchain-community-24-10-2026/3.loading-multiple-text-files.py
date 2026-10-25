from pathlib import Path

from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader


# ========================================
# CUSTOM DIRECTORY TEXT LOADER
# ========================================

class FolderTextLoader(BaseLoader):

    def __init__(self, folder_path):

        self.folder_path = Path(folder_path)

    def lazy_load(self):

        for file_path in sorted(
                self.folder_path.glob("*.txt")
        ):

            content = file_path.read_text(
                encoding="utf-8"
            )

            yield Document(
                page_content=content,
                metadata={
                    "source": str(file_path)
                }
            )


# ========================================
# PREPARE SAMPLE FILES
# ========================================

folder = (
        Path(__file__).resolve().parent
        / "day2_sample_files"
)

folder.mkdir(exist_ok=True)

files = {
    "admissions.txt": "Admissions start on Monday.",
    "library.txt": "Library opens at 8 AM.",
    "student_rules.txt": "Students must carry ID cards."
}

for filename, content in files.items():

    (folder / filename).write_text(
        content,
        encoding="utf-8"
    )


# ========================================
# LOAD MULTIPLE TEXT FILES
# ========================================

loader = FolderTextLoader(folder)

documents = loader.load()


# ========================================
# DISPLAY DOCUMENTS
# ========================================

print("TOTAL DOCUMENTS:", len(documents))


for number, document in enumerate(
        documents,
        start=1
):

    print("\nDOCUMENT", number)

    print(
        "SOURCE:",
        Path(
            document.metadata["source"]
        ).name
    )

    print(
        "CONTENT:",
        document.page_content
    )