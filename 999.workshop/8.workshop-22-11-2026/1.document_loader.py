from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("company_policy.pdf")

documents = loader.load()

print("COMPANY POLICY DOCUMENT LOADER")
print("=" * 50)

print("Total Pages:", len(documents))

for index, doc in enumerate(documents, start=1):
    print(f"\nDOCUMENT {index}")
    print("-" * 50)
    print("Page Content:")
    print(doc.page_content)
    print("\nMetadata:")
    print(doc.metadata)
    print("\nObject Type:")
    print(type(doc))