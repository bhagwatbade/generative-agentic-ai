STOP_WORDS = {"a", "the"}

def words(text):
    return {
        word for word in text.lower().split()
        if word not in STOP_WORDS
    }

def jaccard_similarity(text1, text2):
    a = words(text1)
    b = words(text2)
    union = a | b
    return len(a & b) / len(union) if union else 1.0

s1 = "Purchase a vehicle"
s2 = "Buy a car"
print("Jaccard Score:", round(jaccard_similarity(s1, s2), 2))