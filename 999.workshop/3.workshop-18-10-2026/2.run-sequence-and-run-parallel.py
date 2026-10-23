from langchain_core.runnables import RunnableLambda, RunnableParallel


def add10(x):
    return x + 10

def double(x):
    return x * 2

def square(x):
    return x * x

chain = RunnableLambda(add10) | RunnableLambda(double) | RunnableLambda(square)

result = chain.invoke(10)

print('Chain sequence result :', result)

print('=========================================')

chain = RunnableParallel(
    x1 = RunnableLambda(add10),
    x2 = RunnableLambda(double),
    x3 = RunnableLambda(square)
)

result = chain.invoke(10)
print('Chain parallel result :', result)