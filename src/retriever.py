import numpy as np

class Retriever:

    def __init__(self, embedding_model):
        self.embedding_model = embedding_model
        self.chunks = []
        self.embeddings = []

    def indexar_documentos(self, chunks):

        self.chunks = chunks

        for chunk in chunks:
            embedding = self.embedding_model.generate_embedding(chunk)
            self.embeddings.append(embedding)

    def buscar(self, pergunta, top_k=3):

        if not self.chunks:
            return []

        if top_k <= 0:
            raise ValueError("O valor do top k deve ser positivo e maior que zero.")

        embedding_pergunta = self.embedding_model.generate_embedding(pergunta)

        similaridades = []

        for embedding in self.embeddings:

            similaridade = np.dot(embedding_pergunta, embedding) / (
                np.linalg.norm(embedding_pergunta) *
                np.linalg.norm(embedding))

            similaridades.append(similaridade)


        if top_k <= len(similaridades):
            indices = np.argsort(similaridades)[::-1][:top_k]
        else:
            indices = np.argsort(similaridades)[::-1]


        resultados = []

        for indice in indices:
            resultados.append({
                "chunk": self.chunks[indice],
                "similaridade": float(similaridades[indice])
            })

        return resultados