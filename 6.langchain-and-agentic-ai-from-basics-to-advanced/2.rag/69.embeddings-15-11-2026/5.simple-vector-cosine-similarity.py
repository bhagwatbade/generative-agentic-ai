# ========================================
# PROGRAM 5 — SIMPLE VECTOR SIMILARITY
# ========================================

import math

vector1 = [1, 0]
vector2 = [0.8, 0.6]
vector3 = [0, 1]

def cosine_similarity(a, b):

    if len(a) != len(b):
        raise ValueError("Vector dimensions must match")

    dot_product = sum(
        x * y
        for x, y in zip(a, b)
    )

    # Magnitude (Euclidean Length) Calculations
    magnitude_a = math.sqrt(
        sum(x * x for x in a)
    )

    magnitude_b = math.sqrt(
        sum(y * y for y in b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Zero vectors are not supported")

    return dot_product / (
            magnitude_a * magnitude_b
    )

print(
    "Vector 1 vs Vector 2:",
    round(cosine_similarity(vector1, vector2), 2)
)

print(
    "Vector 1 vs Vector 3:",
    round(cosine_similarity(vector1, vector3), 2)
)