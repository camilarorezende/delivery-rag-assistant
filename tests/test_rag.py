from src.embeddings import EmbeddingModel
from src.retriever import Retriever
from src.rag import RAGPipeline
from src.document_loader import DocumentLoader
from src.chunking import TextChunker

loader = DocumentLoader()
documentos = loader.carregar_documentos()

chunker = TextChunker(chunk_size=300, overlap=50)

chunks = []

for documento in documentos:
    chunks.extend(
        chunker.dividir_documentos(documento["conteudo"])
    )

modelo = EmbeddingModel()

retriever = Retriever(modelo)
retriever.indexar_documentos(chunks)

rag = RAGPipeline(retriever)

pergunta = "Meu pedido está atrasado. Como acompanho a entrega?"

resposta = rag.gerar_resposta(pergunta)

print("\nResposta do assistente:")
print(resposta)

