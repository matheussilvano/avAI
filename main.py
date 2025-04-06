import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from ai.chatbot import ChatbotAvai
from ai.utils import carregar_documentos  # ou o caminho correto

print("🤖 avAI - Seu Assistente sobre o Avaí Futebol Clube!")
print("Digite sua pergunta (ou 'sair' para encerrar):\n")

bot = ChatbotAvai()

nomes, docs = carregar_documentos('data')
bot.vectorizer.ajustar(docs)

while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ['sair', 'exit']:
        print("avAI: Até logo! 🦁")
        break
    resposta = bot.responder(pergunta)
    print("\navAI:", resposta, "\n")
