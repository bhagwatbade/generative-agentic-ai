# ========================================
# PROGRAM 1 — UNDERSTANDING VECTORS
# ========================================

vector = [0.12, -0.35, 0.78, 0.41]

print('Vector:')
print(vector)

print('\nType:')
print(type(vector))

print('\nDimension:')
print(len(vector))

print('\nFirst Component:')
print(vector[0])

print('\nAll Components:')

for index, value in enumerate(vector, start=1):
    print(f'Dimension {index}: {value}')

