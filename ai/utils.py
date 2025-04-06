import os
import fitz
import re

def carregar_documentos(pasta='data'):
    nomes = []
    docs = []

    for nome_arquivo in os.listdir(pasta):
        caminho = os.path.join(pasta, nome_arquivo)

        if not os.path.isfile(caminho):
            continue

        if nome_arquivo.endswith(".txt"):
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()

        elif nome_arquivo.endswith(".pdf"):
            conteudo = ""
            with fitz.open(caminho) as pdf:
                for pagina in pdf:
                    conteudo += pagina.get_text()

        else:
            continue  # ignora outros tipos de arquivos

        # Divide o conteúdo em frases usando pontuação
        frases = re.split(r'(?<=[.!?])\s+', conteudo.strip())

        for frase in frases:
            if frase.strip():  # ignora vazios
                nomes.append(nome_arquivo)
                docs.append(frase.strip())

    return nomes, docs
