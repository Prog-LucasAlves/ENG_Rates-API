# 📈 Projeto: Exchange Rates API

Este projeto é uma aplicação web que coleta, armazena e exibe pares de moedas utilizando a **API AwesomeAPI**. O backend é desenvolvido com **Flask**, **Pydantic** e **SQLite**, enquanto o frontend usa **HTML**.

## 🛠 Tecnologias Utilizadas

### 📌 Backend

- Flask - Framework para desenvolvimento web
- Flask-CORS - Permite requisições entre domínios
- Requests - Para fazer chamadas à API externa
- Pydantic - Validação de dados
- SQLite - Banco de dados local
- Gunicorn - Servidor para deploy no Render

### 🎨 Frontend

- HTML5 - Estrutura da página
- JavaScript - Manipulação de dados e atualização dinâmica da tabela

### 🚀 Deploy

- Render - Hospedagem do backend

## 📥 Instalação e Execução Local

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/Prog-LucasAlves/ENG_Rates-API
cd exchange-rates
```

### 2️⃣ Configurar o Backend (**Flask**)

Criar ambiente virtual e instalar dependências:

```bash
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

Rodar o servidor **Flask**

```bash
python app.py
```

A API estará disponível em `**http://127.0.0.1:5000**`

## 📡 Endpoints da API

| **Método** | **Endpoint** | **Descrição** |
| ------ | -------- | --------- |
| **GET** | / | Retorna os dados armazenadas no banco de dados |

## 🌍 Deploy no Render

- 1️⃣ Criar conta no Render
- 2️⃣ Criar um serviço Web
- 3️⃣ Conectar ao repositório GitHub
- 4️⃣ Configurar:
  - **Start Command**: `gunicorn app:app`
  - **Build Command**: `pip install -r requirements.txt`

## 📊 Funcionalidades

- ✅ Coleta automática das taxas de câmbio
- ✅ Armazena os dados no banco SQLite
- ✅ Exibe os valores dinamicamente na interface
- ✅ API acessível para consultas externas
- ✅ Deploy no Render

## 🔗 Links Úteis

- **Backend (Render)**: [URL do backend](https://eng-rates-api.onrender.com/)

## 📌 Sinta-se à vontade para contribuir! Caso queira sugerir melhorias, abra um Pull Request. 🚀
