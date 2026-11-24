# ========================================
# PROGRAM 3 — DIMENSION COMPARISON
# ========================================

vector1 = [0.1, 0.2, 0.3]
vector2 = [0.4, 0.5, 0.6]
vector3 = [0.7, 0.8]

print("Vector 1 Dimensions:", len(vector1))
print("Vector 2 Dimensions:", len(vector2))
print("Vector 3 Dimensions:", len(vector3))

print("\nVector 1 vs Vector 2:")

if len(vector1) == len(vector2):
    print("Dimensions match")
else:
    print("Dimensions do not match")

print("\nVector 1 vs Vector 3:")

if len(vector1) == len(vector3):
    print("Dimensions match")
else:
    print("Dimensions do not match")
