documents = [
    "Employees can work remotely.",
    "Students can attend online classes.",
    "The library closes at 6 PM."
]

question = "Can staff work from home?"

print("STEP 1: DOCUMENTS")
for document in documents:
    print(document)

print("STEP 2: GENERATE DOCUMENT EMBEDDINGS")
print("STEP 3: USER QUESTION:", question)
print("STEP 4: GENERATE QUESTION EMBEDDING")
print("STEP 5: COMPARE VECTORS")
print("STEP 6: RETURN RELEVANT DOCUMENTS")