from google.genai import Client
from embeddings import get_embeddings
from vector import find_answers


client = Client(api_key="")


def ask_my_pdf():
    print("\n--- Assistant Ready (Type 'q' to quit) ---")

    while True:
        # 1. Get input from user
        question = input("\nCustomer: ")

        # 2. Check if user wants to exit
        if question.lower() == "q":
            print("Exiting...")
            break

        # 3. Retrieve context from ChromaDB
        query_embedding = get_embeddings([question])[0]

        results = find_answers(query_embedding)
        context = "\n".join(results["documents"][0])

        # 4. Generate response
        prompt = f"""
        You are a customer support assistant.
        Context: {context}
        User question: {question}
        Rules:
        1. If the user says "Hi", "Hello", or asks "How are you", respond politely and ask how you can help with their support needs.
        2. For all other questions, answer ONLY using the Context provided above.
        3. If the answer is not in the context, say: "I'm sorry, I don't have information on that. Please contact customer support at support@example.com."
        """
        response = client.models.generate_content(
            model="gemini-2.5-flash",  # or gemini-2.5-flash
            contents=prompt
        )

        print("\nAgent:", response.text)
