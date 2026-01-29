from google import genai
client = genai.Client(api_key="")


def get_embeddings(list_of_sentences):
    my_results = []

    for item in list_of_sentences:

        data = client.models.embed_content(
            model="models/text-embedding-004",
            contents=item
        )

        numbers = data.embeddings[0].values
        my_results.append(numbers)

    return my_results
