from sentence_transformers import SentenceTransformer, util
import torch

class Vectorizador:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = None
        self.docs = None

    def ajustar(self, documentos):
        self.docs = documentos
        self.embeddings = self.model.encode(documentos, convert_to_tensor=True)

    def buscar_resposta(self, pergunta):
        pergunta_embedding = self.model.encode(pergunta, convert_to_tensor=True)
        similaridades = util.cos_sim(pergunta_embedding, self.embeddings)[0]
        indice_mais_proximo = torch.argmax(similaridades).item()
        confianca = similaridades[indice_mais_proximo].item()
        return indice_mais_proximo, confianca
