import matplotlib.pyplot as plt

words = {
    "Python": [0.8, 0.7],
    "Java": [0.75, 0.65],
    "Machine Learning": [0.6, 0.8],
    "Cooking": [-0.5, 0.2]
}

for word, (x, y) in words.items():
    plt.scatter(x, y, s=100)
    plt.annotate(word, (x, y), xytext=(5, 5),
                 textcoords="offset points")

plt.title("Simple 2D Embeddings")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.grid()
plt.show()
