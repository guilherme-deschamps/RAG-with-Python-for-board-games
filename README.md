# RAG Application with Local Models and ChromaDB

This repository contains a **Retrieval-Augmented Generation (RAG)** application that reads content from PDF files, embeds the text, stores the embeddings in **ChromaDB**, and uses **local models from Ollama** for querying.

---

## Project Overview

The application works in the following stages:
1. **Reading PDFs:** Files stored in the `data/` folder are processed.
2. **Embedding:** The text content is embedded using the **Nomic Embed Text** model.
3. **Storage:** The embeddings are stored in a **ChromaDB** vector database.
4. **Querying:** A **Mistral** language model (running locally via Ollama) is used to answer user queries based on retrieved context from the ChromaDB.

---

## Requirements

This project uses Python and several dependencies listed in `requirements.txt`.

To install the necessary packages, run:

```bash
pip install -r requirements.txt
```

---

## Prerequisites

This application uses **Ollama** to run models locally. Make sure you have Ollama installed and the following models pulled:

```bash
ollama pull mistral
ollama pull nomic-embed-text
```

- **Mistral:** The local language model for answering queries.
- **Nomic Embed Text:** The embedding model used to convert text into vector representations.

---

## Folder Structure

```
.
├── data/                      # Folder containing PDF files to process
├── populate_database.py       # Script to populate ChromaDB with embedded data
├── query_rag.py                # Script to query the RAG system
├── requirements.txt           # Project dependencies
├── test_rag.py                # Script to test the RAG output
└── README.md                   # Project documentation (this file)
```

---

## Populating the Database

To populate the ChromaDB vector database with content from the `data/` folder, run:

```bash
python populate_database.py
```

### Reset and Populate

To **reset** the database and fully re-populate from scratch, use:

```bash
python populate_database.py --reset
```

---

## Querying the RAG Model

To query the RAG system and get an answer from the Mistral model using retrieved context, run:

```bash
python query_rag.py --query_text="How many players can play Monopoly?"
```

Replace the query text with your own question as needed.

---

## Example Workflow

1. Place your PDF files in the `data/` folder.
2. Populate the vector database:
    ```bash
    python populate_database.py
    ```
3. Run a query:
    ```bash
    python query_rag.py --query_text="What is the objective of the game Scrabble?"
    ```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For questions or issues, please open an issue in the repository.

---

Let me know if you want me to create a sample `requirements.txt` or add example outputs!
