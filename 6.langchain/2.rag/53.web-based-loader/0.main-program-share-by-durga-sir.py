'''

UNDERSTANDING WEBBASELOADER
----------------------------
If the data is available in the website, how to read data and create Document objects.

What Is WebBaseLoader?
WebBaseLoader is a LangChain document-loading integration that retrieves HTML web pages, extracts text from their parsed HTML and returns Document objects.
It uses web requests and Beautiful Soup for parsing HTML content.

WebBaseLoader converts available HTML page text into LangChain Document objects.
WebBaseLoader works with specified web-page URLs, not automatically with an entire website.

How WebBaseLoader Works Internally
----------------------------------
WebBaseLoader loads website content and converts it into LangChain Document objects.
Step-by-Step Process
1. Retrieve HTML: Downloads the HTML content from the given website URL using an HTTP request.

2. Parse HTML: Uses Beautiful Soup to analyse and understand the HTML structure.

3. Extract Text: Uses get_text() to remove HTML tags and extract text content.

4. Create Document: Stores the extracted text in page_content and website details in metadata.

Understanding WebBaseLoader Metadata
------------------------------------
Metadata Field	Purpose
source--->	Original page URL
title-->	HTML page title
description-->	Available HTML meta description
language--->	Language declared by the page

eg:
{
    "source": "https://example.com/",
    "title": "Python Course",
    "description": "Python training information",
    "language": "en"
}
Understanding Important WebBaseLoader Parameters
-------------------------------------------------
Important Import
from langchain_community.document_loaders import WebBaseLoader

Basic Usage
loader = WebBaseLoader(
    web_path="https://example.com/"
)

Parameter	Purpose
web_path	Single URL or supported sequence of URLs
web_paths	Sequence of URLs to load
header_template	Request headers, including User-Agent
requests_kwargs	Request options such as timeout
raise_for_status	Raise an error for unsuccessful HTTP status codes
bs_kwargs	Options passed to Beautiful Soup while parsing
bs_get_text_kwargs	Options used while extracting text
requests_per_second	Concurrency limit for supported multiple-request operations

Parameter 1 — web_path
---------------------
Identifies the page we want to load.
Example:
https://example.com/

Parameter 2 — web_paths
-----------------------
Allows us to specify multiple pages.
Example:
web_paths=[
    "https://example.com/page1",
    "https://example.com/page2"
]


Parameter 3 — header_template
-----------------------------
This parameter lets us provide HTTP request headers.
For example, we can identify our classroom demo using a User-Agent header.


    header_template={
        "User-Agent": "LangChainDay4EducationalDemo/1.0"
    },


User-Agent is an HTTP request header that tells the website server which application or client is sending the request.


Parameter 4 — requests_kwargs
----------------------------
This can configure request behaviour, such as a timeout.
Example:
requests_kwargs={
    "timeout": 15
}
Friends, this helps prevent the program from waiting indefinitely for a slow server.

Parameter 5 — raise_for_status
------------------------------
With:
raise_for_status=True
HTTP error responses can be raised as exceptions instead of silently being treated as successful page content.


Parameter 6 — bs_get_text_kwargs
--------------------------------
This controls aspects of extracting text from the parsed page.
For example:
bs_get_text_kwargs={
    "separator": " ",
    "strip": True
}
This helps create cleaner spacing between extracted text elements.

1. "separator": " "
Specifies what should be placed between extracted text pieces.

Example HTML:
<h1>Welcome to DURGASOFT</h1>
<p>Learn Python</p>
<p>Learn AI</p>


Separator	Output
" "	Welcome to DURGASOFT Learn Python Learn AI
"\n"	Each text piece appears on a new line
","	Welcome to DURGASOFT,Learn Python,Learn AI
""	Welcome to DURGASOFTLearn PythonLearn AI

Conclusion: separator controls how extracted text pieces are joined together.
2. "strip": True
Removes unnecessary spaces and newline characters from the beginning and end of each extracted text piece.

Example:
<p>    Learn Python    </p>


Without stripping:
"    Learn Python    "


With strip=True:
"Learn Python"


Conclusion: strip=True removes unnecessary surrounding whitespace and makes extracted text cleaner.

Program-1: First Program:
-------------------------
from langchain_community.document_loaders import WebBaseLoader
url = "https://www.durgasoftonline.com/s/pages/new-batches/"

loader = WebBaseLoader(
  web_path = url
)
documents = loader.load()
print(len(documents)) #1
document = documents[0]
print(document.page_content)
print(document.metadata)


Program 4 — Our First WebBaseLoader Program
-------------------------------------------
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
----------------------------------------------------
Program with multiple urls:
----------------------------

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
---------------------------------------------
Program 5 — WebBaseLoader With a Local Demonstration Website
------------------------------------------------------------
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

from langchain_community.document_loaders import WebBaseLoader


# ========================================
# CREATE A LOCAL DEMO WEB PAGE
# ========================================

html_content = """
<html lang="en">
<head>
    <title>Institute Notices</title>
    <meta
        name="description"
        content="Training institute updates"
    >
</head>
<body>
    <main>
        <h1>Institute Notices</h1>
        <p>Python batch starts on Monday.</p>
        <p>Library opens at 8 AM.</p>
    </main>
</body>
</html>
"""


# ========================================
# DEFINE DEMO HTTP SERVER
# ========================================

class DemoHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        body = html_content.encode("utf-8")

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )

        self.send_header(
            "Content-Length",
            str(len(body))
        )

        self.end_headers()

        self.wfile.write(body)

    def log_message(self, *args):
        pass


# ========================================
# START LOCAL WEB SERVER
# ========================================

server = ThreadingHTTPServer(
    ("127.0.0.1", 0),
    DemoHandler
)

thread = Thread(
    target=server.serve_forever,
    daemon=True
)

thread.start()


try:

    # ====================================
    # CREATE WEB LOADER
    # ====================================

    url = (
        f"http://127.0.0.1:"
        f"{server.server_port}/"
    )

    loader = WebBaseLoader(
        web_path=url,

        header_template={
            "User-Agent": "LangChainDay4LocalDemo/1.0"
        },

        bs_get_text_kwargs={
            "separator": " ",
            "strip": True
        },

        requests_kwargs={
            "timeout": 10
        },

        raise_for_status=True
    )

    # ====================================
    # LOAD LOCAL WEB PAGE
    # ====================================

    documents = loader.load()

    document = documents[0]

    # ====================================
    # DISPLAY RESULTS
    # ====================================

    print("TOTAL DOCUMENTS:", len(documents))

    print("\nTITLE:")
    print(
        document.metadata.get(
            "title",
            "Not available"
        )
    )

    print("\nDESCRIPTION:")
    print(
        document.metadata.get(
            "description",
            "Not available"
        )
    )

    print("\nLANGUAGE:")
    print(
        document.metadata.get(
            "language",
            "Not available"
        )
    )

    print("\nSOURCE IS LOCAL:")
    print(
        document.metadata["source"].startswith(
            "http://127.0.0.1:"
        )
    )

    print("\nPAGE CONTENT:")
    print(
        " ".join(
            document.page_content.split()
        )
    )

finally:

    server.shutdown()
    server.server_close()



Limitation of WebBaseLoader:
----------------------------
WebBaseLoader cannot execute JavaScript. It can load static HTML content, but it may miss content generated dynamically using JavaScript.

For JavaScript-rendered websites, we have two main alternatives:
1. PlaywrightURLLoader — Recommended.
2. SeleniumURLLoader — Another good alternative.

'''