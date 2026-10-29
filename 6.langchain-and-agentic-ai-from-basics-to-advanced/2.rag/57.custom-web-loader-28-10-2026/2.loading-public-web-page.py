import requests

from bs4 import BeautifulSoup

from langchain_core.documents import Document


# ========================================
# APPROVED DEMO URL
# ========================================

url = "https://www.durgasoftonline.com/s/pages/new-batches"


# ========================================
# FETCH AND PARSE THE WEB PAGE
# ========================================

try:

    response = requests.get(
        url,
        headers={
            "User-Agent": "LangChainClassroomDemo/1.0"
        },
        timeout=15
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    title = (
        soup.title.get_text(strip=True)
        if soup.title
        else "Not available"
    )

    main = soup.select_one("main")

    content_node = main if main else soup.body

    content = content_node.get_text(
        " ",
        strip=True
    )


    # ====================================
    # CREATE LANGCHAIN DOCUMENT
    # ====================================

    document = Document(
        page_content=content,
        metadata={
            "source": url,
            "source_type": "web",
            "title": title
        }
    )


    # ====================================
    # DISPLAY RESULT
    # ====================================

    print("TOTAL DOCUMENTS: 1")

    print("TITLE:", document.metadata["title"])

    print("SOURCE:", document.metadata["source"])

    print(
        "CONTENT PREVIEW:",
        document.page_content[:250]
    )

except requests.RequestException as error:

    print("WEB PAGE COULD NOT BE LOADED")

    print("ERROR:", type(error).__name__)
