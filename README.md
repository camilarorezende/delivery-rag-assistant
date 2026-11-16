# 🍔 Delivery RAG Assistant

Um assistente inteligente de atendimento para um aplicativo de delivery, desenvolvido com **Python, Retrieval-Augmented Generation (RAG), Embeddings e Large Language Models (LLMs)**.

O projeto utiliza uma base de conhecimento local para recuperar informações relevantes e gerar respostas contextualizadas às dúvidas dos clientes sobre entregas, cancelamentos, pagamentos e reembolsos.

## 🎯 Objetivo

Desenvolver um sistema de perguntas e respostas baseado em RAG, explorando na prática conceitos fundamentais de Inteligência Artificial Generativa.

O projeto busca reduzir respostas incorretas e alucinações dos modelos de linguagem por meio da recuperação de informações de documentos previamente definidos.

## 🧠 Como funciona

O pipeline RAG segue as seguintes etapas:

1. **Carregamento de documentos:** leitura dos arquivos `.txt` armazenados na base de conhecimento.
2. **Chunking:** divisão dos documentos em pequenos trechos de texto, com sobreposição (*overlap*) para preservar o contexto.
3. **Embeddings:** transformação dos chunks em representações vetoriais utilizando Sentence Transformers.
4. **Indexação:** armazenamento dos embeddings para permitir buscas semânticas.
5. **Retrieval:** recuperação dos trechos mais relevantes para a pergunta do usuário por meio da similaridade do cosseno.
6. **Generation:** envio do contexto recuperado e da pergunta para um LLM local, executado com Ollama.
7. **Resposta:** geração de uma resposta baseada nas informações encontradas na base de conhecimento.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **Sentence Transformers:** geração de embeddings multilíngues.
- **NumPy:** operações matemáticas e cálculo de similaridade.
- **Ollama:** execução local de modelos de linguagem.
- **Qwen3 4B:** modelo de linguagem utilizado para geração de respostas.

## 📁 Estrutura do projeto

```text
delivery-rag-assistant/
│
├── data/
│    ├── entregas.txt
│    ├── cancelamentos.txt
│    ├── pagamentos.txt
│    └── reembolsos.txt
│
│
├── src/
│   ├── __init__.py
│   ├── embeddings.py
│   ├── chunking.py
│   ├── document_loader.py
│   ├── retriever.py
│   └── rag.py
│
├── tests/
│   ├── __init__.py
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   ├── test_retriever.py
│   └── test_rag.py
│
├── README.md
└── requirements.txt
```

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/delivery-rag-assistant.git
cd delivery-rag-assistant
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Instale e configure o Ollama

Instale o Ollama seguindo as instruções oficiais:

https://ollama.com/download

Baixe o modelo utilizado:

```bash
ollama pull qwen3:4b
```-

Verifique se o modelo está disponível:

```bash
ollama list
```

### 5. Execute o projeto

Com o Ollama em execução e o ambiente virtual ativado:

```bash
python3 -m tests.test_rag
```

## 💬 Exemplo de utilização

**Pergunta:**

"Meu pedido está atrasado. Como posso acompanhar a entrega?"

**Contexto recuperado:**

"Quando o pedido atrasa, o cliente deve consultar o status atualizado pelo aplicativo."

**Resposta esperada:**

"Você pode acompanhar o status atualizado do seu pedido diretamente pelo aplicativo."

*As respostas podem variar de acordo com o modelo utilizado e os documentos disponíveis na base de conhecimento.*

## 📚 Conceitos estudados e aplicados

- Retrieval-Augmented Generation (RAG).
- Embeddings e representação vetorial de textos.
- Processamento e divisão de documentos (*chunking*).
- Overlap e preservação de contexto.
- Busca semântica.
- Similaridade do cosseno (*Cosine Similarity*).
- Recuperação de contexto (*Information Retrieval*).
- Engenharia de Prompt (*Prompt Engineering*).
- Integração de LLMs com Python.
- Execução local de modelos de linguagem.
- Organização e modularização de projetos Python.
