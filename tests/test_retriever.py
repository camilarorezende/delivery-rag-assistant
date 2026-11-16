from src.embeddings import EmbeddingModel
from src.retriever import Retriever

modelo = EmbeddingModel()

chunks = [
    "O cliente pode acompanhar o pedido pelo aplicativo.",
    "O cliente pode solicitar reembolso em determinadas situações.",
    "O pagamento deve ser confirmado antes do preparo.",
    "Quando o pedido atrasa, o cliente pode acompanhar a entrega."
]

retriever = Retriever(modelo)

retriever.indexar_documentos(chunks)

pergunta = "Meu pedido está atrasado. Como acompanho a entrega?"

resultados = retriever.buscar(pergunta, top_k=2)

for resultado in resultados:
    print("\nTexto:", resultado["chunk"])
    print("Similaridade:", resultado["similaridade"])