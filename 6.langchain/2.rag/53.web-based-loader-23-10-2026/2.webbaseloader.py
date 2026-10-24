from langchain_community.document_loaders import WebBaseLoader


# ========================================
# SPECIFY WEB PAGE
# ========================================

url = "https://www.durgasoftonline.com/s/pages/new-batches/"


# ========================================
# CREATE WEB LOADER
# ========================================

loader = WebBaseLoader(
    web_path=url,

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
# LOAD WEB PAGE
# ========================================

try:

    documents = loader.load()

    print("TOTAL DOCUMENTS")
    print("---------------")
    print(len(documents))

    document = documents[0]

    print("\nSOURCE")
    print("------")
    print(document.metadata["source"])

    print("\nTITLE")
    print("-----")
    print(
        document.metadata.get(
            "title",
            "Not available"
        )
    )

    print("\nPAGE CONTENT")
    print("------------")

    text = " ".join(
        document.page_content.split()
    )

    print(text)
    #print(text[:500])

except Exception as error:

    print("WEB PAGE COULD NOT BE LOADED")

    print("ERROR TYPE:")
    print(type(error).__name__)

    print("ERROR DETAILS:")
    print(error)