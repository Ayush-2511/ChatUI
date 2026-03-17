import chromadb
from sentence_transformers import SentenceTransformer

#---------------------------------------------------------------------------#
client = chromadb.PersistentClient(path="./vector_db")
collection = client.get_or_create_collection("memory")
model = SentenceTransformer("all-MiniLM-L6-v2")
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
def store_memory(text):
    vector = model.encode(text).tolist()
    collection.add(
        ids=[str(hash(text))],
        documents=[text],
        embeddings=[vector]
    )

def retrieve_memory(query):
    vector = model.encode(query).tolist()
    result = collection.query(
        query_embeddings=[vector],
        n_results=1
    )
    return result["documents"][0]
#---------------------------------------------------------------------------#
