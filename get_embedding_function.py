from langchain_ollama import OllamaEmbeddings

def get_embedding_function():
    """Gets an embedding function from Langchain.
    This function returns an embedding function provided by Ollama, but it can also be done
    using other local embedding models or online embedding providers like Amazon Bedrock.

    Returns:
        _type_: Embedding function provided by Ollama.
    """
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )
    return embeddings