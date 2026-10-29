from langchain_community.document_loaders import WebBaseLoader


# ========================================
# SPECIFY MULTIPLE WEB PAGES
# ========================================

urls = [
    "https://www.durgasoftonline.com/",
    "https://www.durgasoftonline.com/s/pages/new-batches/",
    "https://www.durgasoftonline.com/faqs"
]


# ========================================
# CREATE WEB LOADER
# ========================================

loader = WebBaseLoader(
    web_paths=urls,

    header_template={
        "User-Agent": "LangChainDay4EducationalDemo/1.0"
    },

    requests_kwargs={
        "timeout": 15
    },

    raise_for_status=True,

    bs_get_text_kwargs={
        "separator": " ",
        "strip": True
    }
)


# ========================================
# LOAD MULTIPLE WEB PAGES
# ========================================

try:

    documents = loader.load()

    print("TOTAL DOCUMENTS")
    print("---------------")
    print(len(documents))


    # ====================================
    # DISPLAY EACH DOCUMENT
    # ====================================

    for index, document in enumerate(documents, start=1):

        print("\nDOCUMENT", index)
        print("====================")

        print("\nSOURCE")
        print("------")
        print(document.metadata.get("source", "Not available"))

        print("\nTITLE")
        print("-----")
        print(document.metadata.get("title", "Not available"))

        print("\nPAGE CONTENT")
        print("------------")

        text = " ".join(
            document.page_content.split()
        )

        print(text[:500])


except Exception as error:

    print("WEB PAGES COULD NOT BE LOADED")

    print("ERROR TYPE:")
    print(type(error).__name__)

    print("ERROR DETAILS:")
    print(error)