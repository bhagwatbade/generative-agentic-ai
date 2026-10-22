from pathlib import Path

from langchain_community.document_loaders import TextLoader


# ========================================
# SPECIFY NON-EXISTING FILE
# ========================================

file_path = (
        Path(__file__).resolve().parent
        / "missing_notice_for_demo_98765.txt"
)


# ========================================
# CREATE TEXT LOADER
# ========================================

loader = TextLoader(
    file_path=str(file_path),
    encoding="utf-8"
)


# ========================================
# ATTEMPT TO LOAD FILE
# ========================================

try:

    documents = loader.load()

    print(
        "TOTAL DOCUMENTS:",
        len(documents)
    )

except RuntimeError:

    print("FILE LOADING FAILED")

    print(
        "The file could not be read."
    )

    print(
        "Check the file path,"
        " permissions and encoding."
    )