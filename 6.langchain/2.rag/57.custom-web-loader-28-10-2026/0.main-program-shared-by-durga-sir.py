'''

UNDERSTANDING WEB-PAGE LOADING
------------------------------
requests --->HTML → BeautifulSoup → Extracted Text → Document

An HTML page contains
•	Headers
•	Navigation menus
•	Sidebars
•	Main content
•	Footers
•	Advertisements
we may not want every piece of information. We required only the relevant content.

8. What Is Beautiful Soup?
-------------------------
Beautiful Soup is a Python library for parsing HTML content.
For today's lesson, we will use it to extract text from a html page.

python -m pip install beautifulsoup4

Important import:

from bs4 import BeautifulSoup

Note:
It is not a LangChain class.
It parses HTML.
Then LangChain Document represents the extracted information.
Beautiful Soup documents the get_text() method for obtaining readable text from parsed HTML.

What is requests module:
-------------------------
To fetch an accessible public web page, we can use a maintained HTTP client such as requests.

We can use requests to get html page from the server. It acts as courier boy.

Note:
An HTTP request is not a JavaScript-enabled browser.
Some websites require login, JavaScript execution or specialised tools.


Program 1 — Creating a Document From a Local HTML Page
------------------------------------------------------
soup = BeautifulSoup(
    html,
    "html.parser"
)


Purpose: Convert HTML text into a structured object so that we can easily search and extract information.
- BeautifulSoup → A class from the bs4 library used to parse HTML.
- html → A string containing HTML content.
- "html.parser" → Python's built-in HTML parser.
- soup → A BeautifulSoup object representing the parsed HTML document.

main = soup.select_one("main")

Purpose: Find the first <main> HTML element in the document.
- soup → The parsed HTML document.
- select_one() → A BeautifulSoup method that finds the first matching element using a CSS selector.
- "main" → CSS selector that searches for an HTML <main> tag.
- main → Contains the matching HTML element as a Tag object.
Important: If no <main> element exists, select_one() returns None.

Note:
Understanding select_one() vs select()
---------------------------------------
soup.select_one("main")	Finds the first matching element	Tag or None
soup.select("main")	Finds all matching elements	ResultSet (list-like)

Final Learning Conclusion:
- BeautifulSoup() → Converts HTML text into a searchable HTML structure.
- select_one() → Finds the first element matching a CSS selector.
- get_text() → Extracts readable text from HTML elements.

get_text() method:
-----------------
Consider this HTML:
<main>
    <h1>Python Training</h1>
    <p>Learn Python</p>
    <p>Learn LangChain</p>
</main>


Example 1: Without arguments
print(main.get_text())



Output (includes newlines and spaces from HTML formatting):
Python Training
Learn Python
Learn LangChain


Example 2: With separator " "
print(main.get_text(" "))

Output (extra whitespace may remain):
Python Training Learn Python Learn LangChain
----------------------------------------------

from pathlib import Path

from bs4 import BeautifulSoup

from langchain_core.documents import Document


# ========================================
# PREPARE SAMPLE HTML PAGE
# ========================================

file_path = (
    Path(__file__).resolve().parent
    / "course_page.html"
)

file_path.write_text(
    """
    <html lang="en">
    <head>
        <title>Course Updates</title>
    </head>
    <body>
        <main>
            <h1>Python Training</h1>
            <p>New batch starts on Monday.</p>
        </main>
    </body>
    </html>
    """,
    encoding="utf-8"
)


# ========================================
# PARSE HTML
# ========================================

html = file_path.read_text(
    encoding="utf-8"
)

soup = BeautifulSoup(
    html,
    "html.parser"
)

main = soup.select_one("main")


# ========================================
# CREATE LANGCHAIN DOCUMENT
# ========================================

document = Document(
    page_content=main.get_text(
        " ",
        strip=True
    ),
    metadata={
        "source": file_path.as_uri(),
        "source_type": "html",
        "title": soup.title.get_text(
            strip=True
        )
    }
)


# ========================================
# DISPLAY RESULT
# ========================================

print("TITLE:", document.metadata["title"])

print("CONTENT:", document.page_content)

print(
    "SOURCE TYPE:",
    document.metadata["source_type"]
)
print("SOURCE:", document.metadata["source"])
---------------------------------------------------------
Program 2 — Loading a Public Web Page
--------------------------------------
python -m pip install requests beautifulsoup4



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




Note:
response.raise_for_status() → Checks the HTTP status code.
If successful → Execution continues normally.
If an HTTP error occurs → Raises requests.exceptions.HTTPError.
====================================
Program-3: Custom Web Page Loader Using BaseLoader
==================================================
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

Important explanations
1. class CustomWebLoader(BaseLoader)
Our custom loader inherits from LangChain's BaseLoader.
2. __init__(self, url)
Stores the website URL in self.url, so we can access it inside lazy_load().
3. lazy_load(self)
This method fetches the web page, extracts readable text using BeautifulSoup and generates a Document.
4. yield Document(...)
Generates one LangChain document containing the web page content and metadata.
5. loader.load()
Calls the inherited load() method, which collects the documents produced by lazy_load() into a Python list. We do not need to override load().
================

'''