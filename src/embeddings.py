from sentence_transformers import SentenceTransformer

# classe que utiliza um modelo leve de inteligência artificial de embeddings
class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

    def generate_embedding(self, text):
        embedding = self.model.encode(text)

        return embedding
