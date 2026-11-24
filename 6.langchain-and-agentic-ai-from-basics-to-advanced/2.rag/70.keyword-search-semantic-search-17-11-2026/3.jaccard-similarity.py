def jaccard_similarity(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    union = words1.union(words2)
    if not union:
        return 1.0
    common = words1.intersection(words2)
    return len(common) / len(union)

s1 = "I want to learn Python"
s2 = "I want to study Python"
s3 = "The weather is very hot"

print(round(jaccard_similarity(s1, s2), 2))
print(round(jaccard_similarity(s1, s3), 2))