import requests

from bs4 import BeautifulSoup

from langchain_core.documents import Document
from langchain_core.document_loaders import BaseLoader


# ========================================
# CUSTOM WEB PAGE LOADER
# ========================================

class CustomWebLoader(BaseLoader):

    def __init__(self, url):

        self.url = url

    def lazy_load(self):

        response = requests.get(
            self.url,
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

        content_node = (
            main if main else soup.body
        )

        if content_node is None:
            content_node = soup

        content = content_node.get_text(
            " ",
            strip=True
        )

        yield Document(
            page_content=content,
            metadata={
                "source": self.url,
                "source_type": "web",
                "title": title
            }
        )


# ========================================
# SPECIFY WEB PAGE
# ========================================

url = "https://www.durgasoftonline.com/s/pages/new-batches"


# ========================================
# LOAD WEB PAGE DOCUMENTS
# ========================================

loader = CustomWebLoader(url)

try:

    documents = loader.load()

    # ====================================
    # DISPLAY RESULTS
    # ====================================

    print("TOTAL DOCUMENTS:", len(documents))

    for document in documents:

        print("\nTITLE:")
        print(document.metadata["title"])

        print("\nSOURCE:")
        print(document.metadata["source"])

        print("\nCONTENT:")
        print(document.page_content)

except requests.RequestException as error:

    print("WEB PAGE COULD NOT BE LOADED")

    print("ERROR:", type(error).__name__)
