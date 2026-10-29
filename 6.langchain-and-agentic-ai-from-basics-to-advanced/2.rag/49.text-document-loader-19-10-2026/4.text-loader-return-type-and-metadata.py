from pathlib import Path

from langchain_community.document_loaders import TextLoader


# ========================================
# CREATE SAMPLE TEXT FILE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "library_rules.txt"
)

content = (
    "The library opens at 8 AM.\n"
    "The library closes at 6 PM.\n"
)

file_path.write_text(
    content,
    encoding="utf-8"
)


# ========================================
# CREATE TEXT LOADER
# ========================================

loader = TextLoader(
    file_path=str(file_path),
    encoding="utf-8"
)


# ========================================
# LOAD DOCUMENTS
# ========================================

documents = loader.load()


# ========================================
# CHECK RETURN TYPE
# ========================================

print("RETURN TYPE")
print("-----------")

print(type(documents).__name__)


# ========================================
# CHECK TOTAL DOCUMENTS
# ========================================

print("\nTOTAL DOCUMENTS")
print("---------------")

print(len(documents))


# ========================================
# ACCESS DOCUMENT
# ========================================

document = documents[0]

print("\nDOCUMENT TYPE")
print("-------------")

print(type(document).__name__)


# ========================================
# DISPLAY SOURCE METADATA
# ========================================

print("\nSOURCE FILE")
print("-----------")

print(
    Path(
        document.metadata["source"]
    ).name
)


# ========================================
# ADD CUSTOM METADATA
# ========================================

document.metadata["department"] = "Library"


# ========================================
# DISPLAY CUSTOM METADATA
# ========================================

print("\nDEPARTMENT")
print("----------")

print(document.metadata["department"])


# ========================================
# CHECK ORIGINAL FILE
# ========================================

print("\nORIGINAL FILE UNCHANGED?")
print("------------------------")

print(
    file_path.read_text(encoding="utf-8")
    == content
)
