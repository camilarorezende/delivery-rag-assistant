from src.embeddings import EmbeddingModel

def test_gerar_embedding():

    modelo = EmbeddingModel()

    texto = "Meu pedido está atrasado."

    vetor = modelo.generate_embedding(texto)

    assert vetor is not None

    assert vetor.ndim == 1

    assert vetor.size > 0

    print("Teste de embeddings executado com sucesso!")
    print("Dimensões do embedding:", vetor.shape)


if __name__ == "__main__":
    test_gerar_embedding()
