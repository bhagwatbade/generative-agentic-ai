from unittest import result


def numbers():
    yield 10
    yield 20
    yield 30

result = numbers()
print(type(result))

for num in result:
    print(num)
