# 🧾 estoque-web-app

Sistema de controle de estoque construído com Python e Flask, ideal para estudo ou demonstração de um CRUD completo com interface web.

---

## 🚀 Funcionalidades

- ✅ Cadastro de produtos com nome, preço e quantidade
- ➕ Adição ao estoque com validação de produto existente
- ➖ Remoção do estoque com verificação de quantidade disponível
- 📝 Atualização do nome e preço do produto
- 📦 Visualização de:
  - Total de produtos distintos
  - Quantidade total em estoque
  - Valor total em reais
  - Lista detalhada dos produtos

---

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- HTML5 (com renderização via Jinja2)

---

## 🧰 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/estoque-web-app.git
cd estoque-web-app
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows
```

3. Instale as dependências:
```bash
pip install flask
```

4. Execute a aplicação:
```bash
python app.py
```

5. Acesse no navegador:
```
http://127.0.0.1:5000/
```

---

## 📁 Estrutura do Projeto

```
estoque-web-app/
├── app.py
├── entities/
│   ├── __init__.py
│   └── product.py
├── templates/
│   ├── home.html
│   ├── register.html
│   ├── view.html
│   ├── add.html
│   ├── remove.html
│   ├── update_name.html
│   └── update_price.html
└── README.md
```
