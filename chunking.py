# creating a function for chunking that will divide the data
def chunk_text(text, chunk_size=200, overlap=50):
    chunk = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk.append(text[start:end])
        start = end - overlap
    return chunk
