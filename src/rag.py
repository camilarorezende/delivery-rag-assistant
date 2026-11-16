import ollama

class RAGPipeline:
    """
    Pipeline RAG que recupera informações relevantes
    e utiliza um LLM para gerar respostas baseadas nelas.

    Attributes:
        retriever: Componente responsável pela busca semântica.
        model_name (str): Nome do modelo LLM executado pelo Ollama.
    """

    def __init__(self, retriever, model_name="qwen3:4b"):
        self.retriever = retriever
        self.model_name = model_name

    def gerar_resposta(self, pergunta, top_k=3):

        resultados = self.retriever.buscar(pergunta, top_k=top_k)

        if not resultados:
            return "Não encontrei informações relevantes para responder."

        contexto = "\n\n".join(
            resultado["chunk"] for resultado in resultados
        )

        prompt = f"""
        Você é um assistente de atendimento de um aplicativo de delivery.

        Responda à pergunta do usuário utilizando apenas as informações
        disponíveis no contexto.

        Se o contexto não tiver informações suficientes, informe que
        não encontrou informações suficientes para responder.

        CONTEXTO:
        {contexto}

        PERGUNTA:
        {pergunta}
        """

        resposta = ollama.chat(model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return resposta["message"]["content"]
