from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.readers.wikipedia import WikipediaReader
import wikipedia

# Define idioma da Wikipedia
wikipedia.set_lang("pt")

# Define e aplica modelo de embeddings local
Settings.embed_model = HuggingFaceEmbedding(model_name="intfloat/multilingual-e5-base")

# Páginas a carregar
pages = [
    "Lista de senhorios em Portugal",
    "Lista de baronias em Portugal",
    "Lista de viscondados em Portugal",
    "Lista de condados em Portugal",
    "Lista de marquesados em Portugal",
    "Lista de ducados em Portugal"
]

# Carrega os documentos
reader = WikipediaReader()
documents = reader.load_data(pages=pages)

# Cria índice vetorial com embeddings locais
index = VectorStoreIndex.from_documents(documents)

# Salva o índice
index.storage_context.persist(persist_dir="storage")

print("✅ Índice criado e salvo com sucesso.")
