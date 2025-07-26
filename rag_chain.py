from llama_index import VectorStoreIndex
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.readers.wikipedia import WikipediaReader
import wikipedia

# Define idioma da Wikipedia
wikipedia.set_lang("pt")

pages = [
    "Lista de senhorios em Portugal",
    "Lista de baronias em Portugal",
    "Lista de viscondados em Portugal",
    "Lista de condados em Portugal",
    "Lista de marquesados em Portugal",
    "Lista de ducados em Portugal"
]

reader = WikipediaReader()
documents = reader.load_data(pages=pages)

embed_model = HuggingFaceEmbedding(model_name="intfloat/multilingual-e5-base")
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
index.storage_context.persist(persist_dir="storage")

print("✅ Índice criado e salvo com sucesso.")
