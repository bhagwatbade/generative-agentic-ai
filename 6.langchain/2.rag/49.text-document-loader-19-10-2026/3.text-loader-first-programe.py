from pathlib import Path
from langchain_community.document_loaders import TextLoader

# ========================================
# CREATE SAMPLE TEXT FILE
# ========================================

file_path = (
    Path(__file__).resolve().parent
    / 'student_rules.txt'
)

print(type(file_path))

file_path.write_text(
    "Students must carry their ID cards.\n"
    "Classes start at 9 AM.\n"
    "Mobile phones are not allowed.\n",
    encoding="utf-8"
)

# ========================================
# CREATE TEXT LOADER
# ========================================

loader = TextLoader(
    file_path = str(file_path),
    encoding="utf-8"
)

# ========================================
# LOAD DOCUMENTS
# ========================================

documents = loader.load()

# ========================================
# DISPLAY TOTAL DOCUMENTS
# ========================================

print("TOTAL DOCUMENTS")
print("---------------")

print(len(documents))

print(type(documents))
print(type(documents).__name__)

# ========================================
# ACCESS FIRST DOCUMENT
# ========================================

document = documents[0]

# ========================================
# DISPLAY CONTENT
# ========================================

print("\nPAGE CONTENT")
print("------------")

print(document.page_content.strip())

# ========================================
# DISPLAY SOURCE
# ========================================


print("\nSOURCE FILE")
print("-----------")

print(document.metadata['source'])
print(Path(document.metadata['source']).name)