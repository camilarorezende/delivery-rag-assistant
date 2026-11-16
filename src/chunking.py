class TextChunker:
    """
    Divide documentos de texto em chunks menores,
    respeitando um limite máximo de caracteres por chunk.

    A divisão é feita por palavras, evitando cortar palavras
    durante o processo. Utiliza overlap para preservar parte
    do contexto entre chunks consecutivos.

    Attributes:
        chunk_size (int): Número máximo de caracteres por chunk.
        overlap (int): Número aproximado de caracteres reaproveitados
                       entre chunks consecutivos.
    """
    def __init__(self, chunk_size=300, overlap=50):
        if chunk_size <= 0:
            raise ValueError("O chunk size deve ser maior que zero.")
        if overlap < 0:
            raise ValueError("O overlap não pode ser menor que zero.")
        if overlap >= chunk_size:
            raise ValueError("O overlap deve ser menor que o chunk size.")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def dividir_documentos(self, text):

            if not text or not text.strip():
                return []

            chunks = []
            chunk_atual = ""
            tamanho_atual = 0

            sentences = text.split()

            for frase in sentences:

                espaco = 1 if chunk_atual else 0

                if tamanho_atual + len(frase) + espaco <= self.chunk_size:

                    if chunk_atual:
                        chunk_atual += " "

                    chunk_atual += frase
                    tamanho_atual += len(frase) + espaco

                else:
                    if chunk_atual:
                        chunks.append(chunk_atual)

                    palavras = chunk_atual.split()
                    palavras_overlap = []
                    tamanho_overlap = 0

                    for palavra in reversed(palavras):

                        espaco = 1 if palavras_overlap else 0

                        if tamanho_overlap + len(palavra) + espaco <= self.overlap:
                            palavras_overlap.insert(0, palavra)
                            tamanho_overlap += len(palavra) + espaco
                        else:
                            break

                    chunk_atual = " ".join(palavras_overlap)

                    if chunk_atual:
                        chunk_atual += " "

                    chunk_atual += frase
                    tamanho_atual = len(chunk_atual)

            # Adiciona o último chunk que sobrou
            if chunk_atual:
                chunks.append(chunk_atual)

            return chunks



