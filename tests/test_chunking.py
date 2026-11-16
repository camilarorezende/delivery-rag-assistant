from src.chunking import TextChunker

texto = """
O cliente pode acompanhar o pedido pelo aplicativo.
O pagamento precisa ser confirmado.
Depois disso, o restaurante começa a preparar o pedido.
O prazo de entrega pode variar conforme a localização.
"""

chunker = TextChunker(
    chunk_size=80,
    overlap=20
)

chunks = chunker.dividir_documentos(texto)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)

print("\nTotal de chunks:", len(chunks))
