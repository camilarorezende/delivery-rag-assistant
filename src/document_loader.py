from pathlib import Path

class DocumentLoader:

    def __init__(self, directory="data"):
        self.directory = Path(directory)

    def carregar_documentos(self):

        documentos = []

        for arquivo in self.directory.glob("*.txt"):
            texto = arquivo.read_text(encoding="utf-8")

            if texto.strip():
                documentos.append({
                    "nome": arquivo.name,
                    "conteudo": texto
                })

        return documentos
