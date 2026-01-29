import chromadb


db_client = chromadb.PersistentClient(path="my_database")

my_folder = db_client.get_or_create_collection("customer_care_info")


def save_to_database(all_text_pieces, all_numbers):
    name_tags = []
    count = 0
    for item in all_text_pieces:
        name_tags.append(str(count))
        count = count + 1

    my_folder.add(
        documents=all_text_pieces,
        embeddings=all_numbers,
        ids=name_tags
    )


def find_answers(question_numbers):

    results = my_folder.query(
        query_embeddings=[question_numbers],
        n_results=1

    )
    return results
