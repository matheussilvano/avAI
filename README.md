
# 🤖🦁 avAI - Seu Assistente Virtual sobre o Avaí Futebol Clube

O **avAI** é um chatbot inteligente desenvolvido com Python, capaz de responder perguntas sobre o Avaí Futebol Clube com base em documentos fornecidos (.pdf e .txt). 

O projeto utiliza técnicas de **Processamento de Linguagem Natural (PLN)** e vetorização semântica para fornecer respostas contextuais e relevantes.

---

## 🚧 Em Desenvolvimento

Este projeto está **em desenvolvimento** e novas funcionalidades estão sendo adicionadas frequentemente!  
Fique à vontade para explorar, testar e contribuir.

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4-orange?logo=scikit-learn)
![NumPy](https://img.shields.io/badge/Numpy-1.24-blue?logo=numpy)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-1.23-lightgrey?logo=adobe-acrobat-reader)
![VSCode](https://img.shields.io/badge/Code-VSCode-blue?logo=visualstudiocode)

---

## 📂 Estrutura do Projeto

```
avai/
│
├── data/                   # Pasta com documentos .txt e .pdf para consulta
├── ai/
├─── chatbot.py              # Classe principal do chatbot
├─── vectorizer.py           # Vetorizador semântico
├─── utils.py                # Funções utilitárias (ex: carregar documentos)
├── main.py                 # Interface de linha de comando (CLI)
├── README.md               # Este arquivo
└── requirements.txt        # Arquivo de requerimentos para execução
```

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/avaibot.git
   cd avaibot
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o chatbot:
   ```bash
   python main.py
   ```

---

## 🤝 Como contribuir

Quer contribuir com o projeto? Siga os passos abaixo para colaborar:

1. **Fork** este repositório.
2. Crie uma **branch** para sua feature ou correção:  
   ```bash
   git checkout -b minha-contribuicao
   ```
3. Faça suas alterações e **commit**:
   ```bash
   git commit -m "Adiciona minha contribuição"
   ```
4. Envie para o seu repositório remoto:
   ```bash
   git push origin minha-contribuicao
   ```
5. Abra um **Pull Request** explicando suas alterações.

📄 Também é possível contribuir **adicionando novos arquivos `.pdf` ou `.txt`** na pasta `data/` que contenham informações relevantes sobre o Avaí Futebol Clube. Esses documentos serão usados para melhorar o aprendizado e a base de conhecimento do assistente virtual.

🔍 Dicas:
- Mantenha o conteúdo dos documentos claro e organizado.
- Verifique se suas mudanças não quebram funcionalidades existentes.
- Sinta-se à vontade para sugerir melhorias ou reportar problemas!

Obrigado por ajudar a melhorar o projeto! 💙🦁

## 📌 Funcionalidades Planejadas

- [x] Leitura de documentos `.pdf` e `.txt`
- [x] Resposta baseada em similaridade semântica
- [ ] Interface Web
- [ ] Aprendizado contínuo com feedback do usuário
- [ ] Treinamento com base em novos documentos adicionados dinamicamente

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 💙 Feito de uma avaiano para a torcida do Avaí!
