from langchain_community.document_loaders import PyPDFLoader


# ========================================
# CREATE PAGE-WISE PDF LOADER
# ========================================

loader = PyPDFLoader(
    file_path="company_policy.pdf",
    mode="page"
)


# ========================================
# PROCESS PDF PAGES LAZILY
# ========================================

processed_pages = 0

lazy_documents = loader.lazy_load()

print(type(lazy_documents))
print(type(lazy_documents).__name__)

for document in lazy_documents:

    processed_pages += 1

    page_number = (
            document.metadata["page"] + 1
    )

    text = document.page_content

    print("\nPAGE", page_number)
    print("---------------------")

    if text:

        print("STATUS: Text extracted")

        print("CONTENT:", text)

    else:

        print("STATUS: No extractable text")

        print(
            "Check whether the page is blank,"
            " scanned, or requires a different"
            " extraction approach."
        )


# ========================================
# DISPLAY TOTAL
# ========================================

print("\nTOTAL PAGES PROCESSED")
print("---------------------")

print(processed_pages)
