from langchain_text_splitters import CharacterTextSplitter


# ========================================
# ORIGINAL TEXT
# ========================================

text = "AAA|BBB|CCC|DDD"


# ========================================
# CREATE SPLITTER
# ========================================

splitter = CharacterTextSplitter(
    separator="|",
    chunk_size=7,
    chunk_overlap=3
)


# ========================================
# SPLIT TEXT
# ========================================

chunks = splitter.split_text(text)


# ========================================
# DISPLAY RESULTS
# ========================================

for index, chunk in enumerate(chunks, start=1):

    print(f"Chunk {index}: {chunk}")

'''

Rule	           Correct understanding
1. Chunk merging	current length + separator length + next piece length <= chunk_size

2. Chunk overlap	Remove complete pieces from the beginning of the previous chunk until overlap/next-chunk size conditions are satisfied.

    while total > chunk_overlap or (
        (total + separator_length + next_piece_length > chunk_size) and total > 0
    ):
        remove_first_piece()
    
    There are two important conditions:
    1. total > chunk_overlap: Remove the first piece if the current chunk length is larger than the requested overlap.
    2. total + separator_length + next_piece_length > chunk_size : Remove the first piece if the next piece cannot fit.
    
    total = current accumulated chunk length. (with including separator length, only actual pice length)
    separator_len = separator length.
    remove_first_piece() : (remove tailing separator as well : not exactly but assume)

explain:

Let's understand Chunk Overlap in LangChain's `CharacterTextSplitter` using multiple examples.

The most important thing to understand is:

Chunk overlap means retaining some content from the previous chunk in the next chunk so that contextual information is not lost.

LangChain does not blindly copy the last N characters. It retains complete split pieces and removes pieces from the beginning when necessary.

## 1. Example 1: Exact overlap

```
text = "AAA|BBB|CCC|DDD"chunk_size = 7chunk_overlap = 3separator = "|"
```

First, LangChain splits the text:

```
["AAA", "BBB", "CCC", "DDD"]
```

Step-by-step execution:

Step 1: Create first chunk

`AAA + | + BBB = 7`

Chunk 1

`AAA|BBB`

Step 2: Try adding CCC

`AAA|BBB + | + CCC = 11`

11 is greater than chunk_size (7), so merging is avoided.

Step 3: Check overlap

Current chunk length = 7

Required overlap = 3

Remove `AAA` (3 characters) from the beginning.

Remaining content = `BBB` (3 characters).

Overlap retained

`BBB`

Step 4: Create second chunk

`BBB + | + CCC = 7`

Chunk 2

`BBB|CCC`

Step 5: Try adding DDD

`BBB|CCC + | + DDD = 11`

Remove `BBB`, retain `CCC`, and add `DDD`.

Chunk 3

`CCC|DDD`

Final output:

```
Chunk 1: AAA|BBB
Chunk 2: BBB|CCC
Chunk 3: CCC|DDD
```

Notice that `BBB` and `CCC` are overlapping pieces.

## 2. Example 2: Overlap is smaller than the previous chunk

```
text = "AAAA|BBBB|CCCC|DDDD"chunk_size = 10chunk_overlap = 4
```

Split pieces:

```
["AAAA", "BBBB", "CCCC", "DDDD"]
```

Step 1: First chunk

```
AAAA|BBBB
```

Length = 9.

Step 2: Try adding CCCC

```
AAAA|BBBB|CCCC
```

Length = 14, which exceeds 10.

Step 3: Apply overlap

Previous chunk:

```
AAAA|BBBB
```

Remove `AAAA` (4 characters).

Remaining:

```
BBBB
```

Length = 4, equal to chunk_overlap.

Step 4: Create next chunk

```
BBBB|CCCC
```

Final result:

```
Chunk 1: AAAA|BBBB
Chunk 2: BBBB|CCCC
Chunk 3: CCCC|DDDD
```

Here, the overlap is exactly 4 characters.

## 3. Example 3: Overlap is not exactly equal to chunk_overlap

This is an important example.

```
text = "AAA|BBB|CCC|DDD"chunk_size = 10chunk_overlap = 5
```

Step 1: First chunk

```
AAA|BBB|CCC
```

Length = 11, so it cannot fit.

Actually, the first chunk will be:

```
AAA|BBB
```

Length = 7.

Step 2: Add CCC

It doesn't fit, so overlap logic starts.

Remove `AAA` (3 characters).

Remaining:

```
BBB
```

Length = 3.

Although `chunk_overlap = 5`, LangChain does not remove `BBB`, because removing it would leave no previous content.

The next chunk becomes:

```
BBB|CCC|DDD
```

However, this is 11 characters, so it also exceeds the chunk size. The resulting chunks are:

```
Chunk 1: AAA|BBB
Chunk 2: BBB|CCC
Chunk 3: CCC|DDD
```

The overlap is 3, not 5.

Why? LangChain retains complete split pieces; it cannot create an overlap of 5 by splitting `BBB` into smaller pieces.

## 4. Example 4: Chunk overlap = 0

```
text = "AAA|BBB|CCC|DDD"chunk_size = 7chunk_overlap = 0
```

Since overlap is zero, LangChain removes all previous pieces before starting the next chunk.

```
Chunk 1: AAA|BBB
Chunk 2: CCC|DDD
```

There is no overlapping content.

## 5. Understand the actual overlap algorithm

The following is simplified pseudocode representing the important logic inside LangChain's `_merge_splits()` method.

```
while current_chunk_size > chunk_overlap or (    current_chunk_size + next_piece_length > chunk_size    and current_chunk_size > 0):    remove_first_piece_from_current_chunk()
```

There are two important conditions:

1. `current_chunk_size > chunk_overlap`: Remove the first piece if the current chunk is larger than the requested overlap.
2. `current_chunk_size + next_piece_length > chunk_size`: Remove the first piece if the next piece cannot fit.

The algorithm continues removing pieces until these conditions are satisfied.

Note that the actual implementation also accounts for separator lengths and handles empty chunks.

## 6. Test your understanding

Question 1. Previous chunk = AAA|BBB (length 7), chunk_overlap = 3. Which content will be retained?

AAA|BBB

BBB

AAA

Nothing

Question 2. Previous chunk = AAA|BBB, chunk_overlap = 0. What will remain?

AAA

BBB

AAA|BBB

Nothing

Question 3. Previous chunk = AAA|BBB, chunk_overlap = 5. What will remain?

AAA|BBB

BBB

AAA

Nothing

Check answers

My suggestion: Pay special attention to Example 3. It demonstrates why `chunk_overlap` is a maximum target rather than a guarantee that every chunk will have exactly that many overlapping characters.

'''