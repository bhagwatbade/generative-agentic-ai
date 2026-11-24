sentences = [
    "Java is a programming language",
    "Java is an island in Indonesia",
    "Java is used for backend development"
]

for sentence in sentences:
    if "java" in sentence.lower():
        print("MATCH:", sentence)