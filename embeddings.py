from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class SentenceEmbedding:

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """
        Initialize the Sentence Transformer model.
        """
        print("Loading Sentence Transformer model...")
        self.model = SentenceTransformer(model_name)
        print("Model loaded successfully.")


    def generate_embedding(self, sentence):
        """
        Generate an embedding vector for a single sentence.
        """
        if not sentence or not sentence.strip():
            raise ValueError("Sentence cannot be empty.")

        embedding = self.model.encode(sentence)
        return embedding


    def generate_multiple_embeddings(self, sentences):
        """
        Generate embeddings for multiple sentences.
        """
        if not sentences:
            raise ValueError("Sentence list cannot be empty.")

        embeddings = self.model.encode(sentences)
        return embeddings


    def calculate_similarity(self, sentence1, sentence2):
        """
        Calculate cosine similarity between two sentences.
        """
        embedding1 = self.generate_embedding(sentence1)
        embedding2 = self.generate_embedding(sentence2)

        embedding1 = embedding1.reshape(1, -1)
        embedding2 = embedding2.reshape(1, -1)

        similarity = cosine_similarity(
            embedding1,
            embedding2
        )[0][0]

        return similarity


    def display_embedding(self, sentence):
        """
        Display the embedding vector of a sentence.
        """
        embedding = self.generate_embedding(sentence)

        print("\nSentence:")
        print(sentence)

        print("\nEmbedding Vector:")
        print(embedding)

        print("\nEmbedding Dimension:")
        print(len(embedding))


    def display_similarity(self, sentence1, sentence2):
        """
        Display similarity between two sentences.
        """
        similarity = self.calculate_similarity(sentence1, sentence2)

        percentage = similarity * 100

        print("\n----------------------------------------")
        print("Sentence Similarity Result")
        print("----------------------------------------")

        print("\nSentence 1:")
        print(sentence1)

        print("\nSentence 2:")
        print(sentence2)

        print("\nCosine Similarity Score:")
        print(round(similarity, 4))

        print("\nSimilarity Percentage:")
        print(round(percentage, 2), "%")

        if similarity >= 0.75:
            result = "Highly Similar"
        elif similarity >= 0.50:
            result = "Moderately Similar"
        elif similarity >= 0.25:
            result = "Slightly Similar"
        else:
            result = "Not Similar"

        print("\nSimilarity Result:")
        print(result)

        print("----------------------------------------")


def main():

    print("========================================")
    print("       SENTENCE EMBEDDING SYSTEM")
    print("========================================")

    embedding_system = SentenceEmbedding()

    print("\nEnter the first sentence:")
    sentence1 = input("> ")

    print("\nEnter the second sentence:")
    sentence2 = input("> ")

    try:

        embedding_system.display_embedding(sentence1)

        embedding_system.display_embedding(sentence2)

        embedding_system.display_similarity(
            sentence1,
            sentence2
        )

    except ValueError as error:

        print("\nError:")
        print(error)


if __name__ == "__main__":
    main()
