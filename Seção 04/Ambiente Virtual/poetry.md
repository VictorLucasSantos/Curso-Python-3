# 🎭 Guia Rápido do Poetry

O **Poetry** é uma ferramenta moderna para **gerenciamento de dependências** e **empacotamento** de projetos Python. Ele substitui o uso tradicional do `pip` e `setup.py`, facilitando a instalação de pacotes e a publicação de bibliotecas no PyPI.

---

## 🚀 Instalando o Poetry

Você pode instalar o Poetry de duas maneiras:

1️⃣ Usando `pip`:
```bash
pip install poetry
```

2️⃣ Usando o script oficial:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Após a instalação, verifique se tudo está certo:
```bash
poetry --version
```

---

## 📦 Criando um Projeto com Poetry
Para iniciar um novo projeto:
```bash
poetry new meu_projeto
```
Isso cria uma estrutura de diretórios como esta:
```
meu_projeto/
├── pyproject.toml  # Configuração do projeto
├── README.rst      # Documentação inicial
├── meu_projeto/    # Código-fonte
│   ├── __init__.py
└── tests/          # Testes
```

Se você já tem um projeto e quer adicionar o Poetry:
```bash
poetry init
```

---

## 🔗 Gerenciando Dependências

### 📥 Adicionando dependências
```bash
poetry add nome_do_pacote
```
Exemplo:
```bash
poetry add requests
```
Isso adiciona `requests` ao arquivo `pyproject.toml`.

### 📤 Removendo dependências
```bash
poetry remove nome_do_pacote
```

### 🔧 Instalando todas as dependências
```bash
poetry install
```

---

## 🌍 Trabalhando com Ambientes Virtuais
O Poetry gerencia automaticamente um ambiente virtual para o seu projeto.

### 🔄 Ativando o ambiente virtual
```bash
poetry shell
```
Para sair do ambiente virtual:
```bash
exit
```

---

## 📤 Publicando Pacotes no PyPI

Se você quiser distribuir um pacote no **PyPI**, siga estes passos:

1️⃣ Configure o token do PyPI:
```bash
poetry config pypi-token.pypi seu-token-aqui
```

2️⃣ Publique o pacote:
```bash
poetry publish --build
```

---

## ✅ Exemplo Completo
Aqui está um fluxo básico de uso do Poetry:

```bash
poetry new exemplo_poetry
cd exemplo_poetry
poetry add requests
poetry shell
python -c "import requests; print(requests.get('https://api.github.com').status_code)"
exit
```

---

## 🎯 Conclusão
O Poetry simplifica a gestão de dependências e ambientes virtuais, sendo uma alternativa moderna ao `pip` e `virtualenv`. Se você busca uma ferramenta prática e eficiente, o Poetry é uma ótima escolha! 🚀

