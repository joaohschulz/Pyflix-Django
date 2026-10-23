# 🎬 PyFlix — Plataforma de Streaming

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-6.1.1-darkgreen)

## 📖 Sobre o projeto

**PyFlix** é uma plataforma web de streaming de filmes e séries desenvolvida com **Python e Django**. O projeto tem como objetivo praticar desenvolvimento web full stack, organização de conteúdo audiovisual e construção de interfaces para navegação pelo catálogo.

> 🚧 **Projeto em desenvolvimento:** funcionalidades, aparência e configurações podem mudar ao longo da implementação.

## ✨ Funcionalidades

O projeto contempla o desenvolvimento de:

- Autenticação e controle de acesso de usuários.
- Catálogo de filmes e séries.
- Exibição de cartazes e informações dos títulos.
- Visualização de detalhes dos conteúdos, como nome, descrição e categoria.
- Interface de navegação pela plataforma.

Novas funcionalidades serão documentadas conforme forem implementadas.

## 🛠️ Tecnologias utilizadas

- **Python** — linguagem principal do back-end.
- **Django** — framework web.
- **HTML e CSS** — estrutura e estilização das páginas.
- **SQLite** — banco de dados utilizado no repositório atual.
- **Pillow** — processamento de imagens.
- **Git e GitHub** — versionamento de código.

As dependências Python estão listadas em `requirements.txt`.

## 🚀 Como executar o projeto

### Pré-requisitos

- Python instalado.
- Git instalado.

**1. Clone o repositório:**

```bash
git clone https://github.com/joaohschulz/PROJETO---Pyflix-Plataforma-de-Streaming.git
cd PROJETO---Pyflix-Plataforma-de-Streaming
```

**2. Crie e ative um ambiente virtual:**

No Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Aplique as migrações do banco de dados:**

```bash
python manage.py migrate
```

**5. Inicie o servidor:**

```bash
python manage.py runserver
```

Acesse **http://127.0.0.1:8000/** no navegador.

> Dependendo da configuração atual do projeto, algumas páginas podem exigir autenticação. A aplicação ainda pode passar por ajustes antes de estar pronta para uso público.

## 🎯 Objetivo

Construir uma aplicação de streaming como projeto de aprendizado e portfólio, aprimorando conhecimentos em **Django, modelagem de dados, autenticação, templates e desenvolvimento de interfaces web**.

## 📌 Status

🟡 **Em desenvolvimento.** Este README será atualizado conforme o projeto evoluir.

## 👨‍💻 Autor

Desenvolvido por [João Henrique Schulz](https://github.com/joaohschulz).

---

⭐ Se você gostou do projeto, considere deixar uma estrela no repositório!
