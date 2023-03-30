# Teste Técnico Úsuario e Tarefas

- [Teste Técnico tarefas](#teste-técnico-tarefas)
  - [1. Sobre](#1-sobre)
  - [2. Tecnologias](#2-tecnologias)
  - [3. Instalação](#3-instalação)
    - [3.1 Requisitos](#31-requisitos)
    - [3.2 Instalação](#32-instalação)
  - [4. Documentação](#4-documentação)
  - [5. Desenvolvedor](#5-desenvolvedor)

<a name="sobre"></a>

## 1. Sobre

Esse Teste consiste em um projeto Back End, onde é possível cadastrar um usuário e adicionar, editar, excluir diversas tarefas para o mesmo.

<a name="links"></a>

<a name="techs"></a>

## 2. Tecnologias

- _Python_
- _Django Rest Framework_
- _PostgreSQL_

<a name="instalacao"></a>

## 3. Instalação

### 3.1 Requisitos

- Python
- Gerenciador de pacotes Pip
- Banco de dados PostgreSQL

### 3.2 Instalação

3.2.1 - Crie um novo banco com nome de sua preferência no PostgreSQL

3.2.2 - Clone esse repositório, entre na pasta raiz do projeto e crie o ambiente virtual do projeto com o comando abaixo:

`python -m venv venv`

3.2.3 - Dentro da pasta raiz do projeto, entre no ambiente virtual do projeto com o comando abaixo:

`source venv/bin/activate`

3.2.4 - Instale as dependências requisitadas no arquivo requirements.txt utilizando o seguinte comando:

`pip install -r requirements.txt`

3.2.5 Crie um arquivo na raiz do projeto chamado .env e altere as variáveis de ambiente conforme o .env.example do projeto

exemplo:

```
POSTGRES_DB='meubanco'
POSTGRES_USER='meuuser'
POSTGRES_PASSWORD='minhasenhadobanco'

```

3.2.6 Para rodar o servidor utilize o comando `python manage.py runserver` no terminal dentro do ambiente do projeto (ou seja, após utilizar o comando no item 3.2.3), se tudo der certo receberá uma mensagem como essa:

      System check identified no issues (0 silenced).
      March 30, 2023 - 14:00:05
      Django version 4.1.7, using settings 'taskproject.settings'
      Starting development server at http://127.0.0.1:8000/
      Quit the server with CONTROL-C.

## 4. Documentação

- Com o servidor ativo, acesse a documentação em:

```
http://127.0.0.1:8000/api/docs/

```

## 5. Desenvolvedor

- <a name="henrique" href="https://www.linkedin.com/in/henriqueyujiandrade/" target="_blank">Henrique Andrade</a>
