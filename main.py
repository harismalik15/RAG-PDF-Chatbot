from pdf import read_pdf
from chunking import chunk_text
from embeddings import get_embeddings
from vector import save_to_database
from rag import ask_my_pdf


pdf_text = read_pdf("customer_care.pdf")
chunks = chunk_text(pdf_text)

embeddings = get_embeddings(chunks)
save_to_database(chunks, embeddings)

answer = ask_my_pdf()
print(answer)
