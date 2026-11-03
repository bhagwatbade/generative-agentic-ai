text = (
    'Python is easy.\n\n'
    'LangChain helps create AI applications.\n\n'
    'RAG uses documents.'
)

separator = '\n\n'

chunks = text.split(separator)

for index, chunk in enumerate(chunks, start = 1):
    print(f'Chunk {index}: \n {chunk}')
