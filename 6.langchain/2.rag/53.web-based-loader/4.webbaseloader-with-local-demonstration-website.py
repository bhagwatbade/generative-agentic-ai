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