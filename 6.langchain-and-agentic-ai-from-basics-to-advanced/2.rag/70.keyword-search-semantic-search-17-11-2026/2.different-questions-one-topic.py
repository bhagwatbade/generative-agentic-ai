questions = [
    "Can employees work remotely?",
    "Can staff work from home?",
    "Are workers allowed to do their jobs from home?"
]

for question in questions:
    print("\nQuestion:", question)
    if "remotely" in question.lower():
        print("Keyword Match Found")
    else:
        print("Keyword Match Not Found")