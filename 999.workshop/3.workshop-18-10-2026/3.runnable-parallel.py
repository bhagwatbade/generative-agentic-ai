from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel
)

def heading(data):
    return 'Learning ' + data['topic']

def hashtag(data):
    return '#' + data['topic'].replace(' ', '')

def count(data):
    return len(data['topic'].split(' '))

parallel = RunnableParallel(
    heading = RunnableLambda(heading),
    hashtag = RunnableLambda(hashtag),
    words = RunnableLambda(count),
)

result = parallel.invoke(
    {'topic' : 'Generative AI'}
)

print(result)