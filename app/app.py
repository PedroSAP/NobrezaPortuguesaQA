from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.settings import Settings
import uvicorn

# Define modelo de embeddings local
Settings.embed_model = HuggingFaceEmbedding(model_name="intfloat/multilingual-e5-base")

# Define LLM local
llm = HuggingFaceLLM(model_name="tiiuae/falcon-7b-instruct")

# Inicializa FastAPI
app = FastAPI()

# Carrega índice com embeddings locais
storage_context = StorageContext.from_defaults(persist_dir="storage")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine(llm=llm)

# HTML
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>Nobreza Portuguesa QA</title>
    <style>
        body {{ font-family: Arial; margin: 2em; }}
        input[type=text] {{ padding: 0.5em; width: 70%; }}
        input[type=submit] {{ padding: 0.5em 1em; }}
        h1, h2 {{ color: #004080; }}
    </style>
</head>
<body>
    <h1>Consulta sobre a Nobreza Portuguesa</h1>
    <form action='/consultar' method='post'>
        <label for='pergunta'>Digite sua pergunta:</label><br>
        <input type='text' id='pergunta' name='pergunta'><br><br>
        <input type='submit' value='Consultar'>
    </form>
    {resposta}
</body>
</html>"""

@app.get("/", response_class=HTMLResponse)
async def form_get():
    return HTML_TEMPLATE.format(resposta="")

@app.post("/consultar", response_class=HTMLResponse)
async def form_post(pergunta: str = Form(...)):
    resposta = query_engine.query(pergunta)
    return HTML_TEMPLATE.format(resposta=f"<h2>Resposta:</h2><p>{resposta}</p>")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
