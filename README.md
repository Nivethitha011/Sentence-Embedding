# Sentence Embedding 

## Project Description

This project demonstrates Sentence Embedding using Python and a pre-trained Sentence Transformer model.

Sentence embedding converts a sentence into a numerical vector that represents its semantic meaning. These vectors can be compared to find how similar two sentences are in meaning.

In this project, two sentences are given as input, their embeddings are generated, and Cosine Similarity is used to calculate the semantic similarity between them.

## Objective

The main objectives of this project are:

* Convert sentences into numerical vectors.
* Generate sentence embeddings using a pre-trained model.
* Compare the meaning of two sentences.
* Calculate semantic similarity using Cosine Similarity.
* Display the similarity score and percentage.

## Technologies Used

* Python
* Sentence Transformers
* Scikit-learn
* VS Code

### Model Used

`all-MiniLM-L6-v2`

This is a pre-trained Sentence Transformer model used to generate sentence embeddings.

## Project Structure

```text
SentenceEmbedding/
│
├── app.py
└── README.md
```

## Installation

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the Python version using:

```bash
python --version
```

### Step 2: Install Required Libraries

Open the VS Code terminal and run:

```bash
pip install sentence-transformers scikit-learn
```

## How to Run

Open the project folder in VS Code.

Run the following command in the terminal:

```bash
python app.py
```

The program will ask for two sentences.

Example:

```text
Enter first sentence: I love learning artificial intelligence.

Enter second sentence: I enjoy studying AI.
```

The program will generate embeddings for both sentences and calculate their similarity.

## How It Works

The project follows these steps:

```text
Input Sentence 1
       |
       v
Sentence Embedding Model
       |
       v
Numerical Vector
       |
       | Cosine Similarity
       |
       v
Similarity Score
       ^
       |
Numerical Vector
       ^
       |
Sentence Embedding Model
       ^
       |
Input Sentence 2
```

### 1. Input

The user enters two sentences.

### 2. Sentence Embedding

The `all-MiniLM-L6-v2` model converts each sentence into a numerical vector.

### 3. Similarity Calculation

Cosine Similarity is used to compare the two sentence vectors.

### 4. Result

The similarity score is converted into a percentage and displayed.

## Example Output

```text
--- Sentence Embedding Result ---

Sentence 1: I love learning artificial intelligence.
Sentence 2: I enjoy studying AI.

Similarity Score: 0.72
Similarity Percentage: 72.0 %
Result: Moderately Similar
```

The exact score may vary depending on the input sentences and model version.

## What is Sentence Embedding?

Sentence embedding is the process of representing a complete sentence as a numerical vector.

For example:

```text
"I love Python"
       |
       v
[0.21, -0.45, 0.78, 0.12, ...]
```

The vector represents information about the semantic meaning of the sentence.

This allows computers to compare sentences based on their meaning rather than only comparing individual words.

## What is Cosine Similarity?

Cosine Similarity measures how similar two vectors are based on the angle between them.

A higher similarity score generally indicates that the sentences have more similar meanings.

## Applications

Sentence embeddings can be used in many Natural Language Processing applications:

* Semantic search
* Chatbots
* Question answering
* Text classification
* Document similarity
* Recommendation systems
* Duplicate question detection
* Information retrieval

## Python Libraries

The project uses the following libraries:

```text
sentence-transformers
scikit-learn
```

`sentence-transformers` is used to generate sentence embeddings.

`scikit-learn` is used to calculate Cosine Similarity.

## Future Improvements

This project can be extended by:

* Adding a Streamlit web interface.
* Comparing multiple sentences.
* Creating a semantic search system.
* Storing embeddings in a vector database.
* Adding visualization of sentence vectors.
* Building a document similarity application.

## Author

Nivethitha

## License

This project is created for educational and learning purposes.
