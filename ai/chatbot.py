from .vectorizer import Vectorizador
from .utils import carregar_documentos
import numpy as np

class ChatbotAvai:
    def __init__(self):
        self.nomes, self.docs = carregar_documentos()
        self.vectorizer = Vectorizador()
        self.vectorizer.ajustar(self.docs)

    def responder(self, pergunta):
        indice, confianca = self.vectorizer.buscar_resposta(pergunta)

        if confianca < 0.3:
            return "🦁 Desculpe, não encontrei uma resposta exata. Tente reformular a pergunta ou adicione mais conteúdo nos documentos."

        trecho = self.docs[indice].replace('\n', ' ').strip()
        resposta = f"""🦁 Resposta sobre o Avaí FC:
A partir das informações que encontrei, aqui está o que posso dizer:

"{trecho}"

Se quiser saber mais, estou aqui pra ajudar! 😉"""

        return resposta
