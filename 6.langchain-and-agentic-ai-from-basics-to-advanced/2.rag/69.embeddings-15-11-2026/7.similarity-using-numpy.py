import numpy as np

python = [0.8, 0.7, 0.6]
java = [0.75, 0.65, 0.55]
machine_learning = [0.6, 0.8, 0.7]
cooking = [-0.5, 0.2, 0.1]

def similarity(a, b):
    return np.dot(a, b) / (
            np.linalg.norm(a) * np.linalg.norm(b)
    )

print("Python vs Java:",
      round(similarity(python, java), 3))

print("Python vs Machine Learning:",
      round(similarity(python, machine_learning), 3))

print("Python vs Cooking:",
      round(similarity(python, cooking), 3))