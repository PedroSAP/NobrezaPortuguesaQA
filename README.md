# NobrezaPortuguesaQA

Este projeto é uma aplicação web com FastAPI que responde a perguntas sobre a nobreza portuguesa com base em documentos extraídos da Wikipedia. Ele usa RAG (Retrieval-Augmented Generation) com `llama-index`, `Hugging Face` e modelos LLM gratuitos rodando localmente (sem OpenAI).

## 🧱 Estrutura
- `rag_chain.py`: coleta as páginas da Wikipedia e gera o índice vetorial.
- `app/app.py`: interface FastAPI com formulário HTML.
- `Dockerfile`: empacota tudo para execução via Docker.
- `requirements.txt`: dependências Python.

## 🚀 Como rodar

1. Gere o índice:
```bash
python rag_chain.py
```

2. Construa o container:
```bash
docker build -t nobrezaqa .
```

3. Execute:
```bash
docker run -p 8000:8000 nobrezaqa
```

Acesse via navegador: http://localhost:8000

## 📚 Modelos usados
- `intfloat/multilingual-e5-base` para embeddings
- `tiiuae/falcon-7b-instruct` como LLM (pode ajustar para outro modelo local)

## ✅ Livre de OpenAI, 100% open-source e local
