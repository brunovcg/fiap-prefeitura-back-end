# FIAP - PREFEITURA BACK-END

## Pré-requisitos

- Para iniciar o projeto você precisa ter o Python (versão 3) e o GIT instalados em seu computador.
- O banco de dados utilizado é o sqlite3, já instalado pelo django, não se preocupe com isso.

## Iniciando o Projeto

### Baixe o Repositório do github

Execute o código no diretório em que deseja instalar o projeto.

```shell
   git clone https://github.com/brunovcg/fiap-prefeitura-back-end.git
```

### Instale e inicie um ambiente virtual do python

#### Instalar o venv

```shell
   python3 -m venv venv
```

#### Iniciar o venv

obs. Você com o terminal aberto no diretório em que o venv esteja:

Mac e Linux:

```shell
   source venv/bin/activate
```

OU

Windows:

```shell
   .\venv\Scripts\activate
```

#### Instalando as libs necessárias

```shell
  pip install -r requirements.txt
```

#### Construindo o banco de dados

```shell
  python manage.py makemigrations accounts buildings
```

#### Realizando as migrations

```shell
  python manage.py migrate
```

#### Inicializando o servidor

```shell
   python manage.py runserver
```

O servidor iniciará em localhost:8000

## Executando o Projeto

### Erros e exceções

Essa aplicação trata os erros permissão e autenticação, cadastro de usuário com CPF (username) em duplicata, verifica se o objeto existe no banco para deletar ou alterá-lo, se todos os campos setados como não nulos existem na request, etc.

#### Exemplo erro de token authentication

```json
{
  "detail": "Invalid token."
}
```

#### Quando existe um token mas este não é de um dos tipos permitidos:

```json
{
  "detail": "You do not have permission to perform this action."
}
```

### Rotas

obs - o arquivo 'Insomnia_FIAP-prefeitura.json' anexo a esse projeto no diretório raiz pode ser carregado no Insomnia para gerar as rotas e suas settings.

#### POST - /api/signup/ - Criar Usuário

##### Exemplo de corpo da Request

```json
{
  "username": "00000000000",
  "email": "aluno@fiap.com.br",
  "password": "12345",
  "telefone": "1112345678",
  "name": "aluno",
  "persona": 1
}
```

##### Responses

- STATUS 201 CREATED

```json
{
  "id": 1
}
```

- STATUS 409 CONFLICT

```json
{
  "message": "User already exists"
}
```

- STATUS 400 BAD REQUEST

```json
{
  "message": {
    "missing_fields": ["telefone"]
  }
}
```

#### POST - /api/login/ - Login do Usuário

##### Exemplo de corpo da Request

```json
{
  "username": "00000000000",
  "password": "12345"
}
```

##### Responses

- STATUS 200 OK

```json
{
  "token": "11b857c9f8d765e19d80f1d4a44dbfc2aa0cd4f6",
  "username": "00000000000",
  "telefone": "1112345678",
  "email": "aluno@fiap.com.br",
  "persona": ""
}
```

- STATUS 401 UNAUTHORIZED

```json
{
  "message": "wrong cpf or password"
}
```

- STATUS 400 BAD REQUEST

```json
{
  "message": "missing cpf or password"
}
```

#### GET - /api/personas/ - Listar Personar

##### Exemplo de corpo da Request

- Sem corpo de request

##### Response

```json
[
  {
    "id": 1,
    "name": "Impostos"
  },
  {
    "id": 2,
    "name": "Notícias"
  },
  {
    "id": 3,
    "name": "Regulamentação"
  }
]
```

#### GET - buildings/neighborhood/ - Listar Bairros

##### Exemplo de corpo da Request

- Sem corpo de request

##### Responses

- STATUS 200 OK

```json
{
  "data": [
    {
      "id": 1,
      "name": "Madalena"
    },
    {
      "id": 2,
      "name": "Boa Viagem"
    },
    {
      "id": 3,
      "name": "Casa Forte"
    },
    {
      "id": 1,
      "name": "Torre"
    }
  ]
}
```

#### GET - buildings/ - Listar imóveis do usuário

##### Authentication

- O usuário somente poderá executar com sucesso o request se for o dono do imóvel
- Rota Autenticada com Token
  No header da request usar:8000
  Authorization : Token hash_do_token

##### Exemplo de corpo da Request

```json
{
  "user": 1
}
```

##### Responses

- STATUS 200 OK

```json
[
  {
    "id": 1,
    "matricula": 9,
    "tamanho": 123,
    "endereco": "Av Boa Viagem",
    "bairro": "Madalena",
    "user": 1
  },
  {
    "id": 2,
    "matricula": 254135,
    "tamanho": 123,
    "endereco": "Av Boa Viagem",
    "bairro": "Madalena",
    "user": 1
  },
  {
    "id": 3,
    "matricula": 425056,
    "tamanho": 123,
    "endereco": "Av Boa Viagem",
    "bairro": "Madalena",
    "user": 1
  },
  {
    "id": 4,
    "matricula": 899881,
    "tamanho": 123,
    "endereco": "Av Boa Viagem",
    "bairro": "Madalena",
    "user": 1
  }
]
```

- STATUS 400 BAD REQUEST

```json
{
  "message": {
    "missing_fields": ["user"]
  }
}
```

#### POST - buildings/ - Criar imóvel do usuário

##### Authentication

- O usuário somente poderá executar com sucesso o request se for o dono do imóvel
- Rota Autenticada com Token
  No header da request usar:8000
  Authorization : Token hash_do_token

##### Exemplo de corpo da Request

```json
{
  "user": 1,
  "tamanho": 123,
  "endereco": "Av Boa Viagem",
  "bairro": "Madalena"
}
```

##### Responses

- STATUS 200 OK

```json
{
  "id": 2,
  "matricula": 254135,
  "tamanho": 123,
  "endereco": "Av Boa Viagem",
  "bairro": "Madalena",
  "user": 1
}
```

- STATUS 400 BAD REQUEST

```json
{
  "message": {
    "missing_fields": ["bairro"]
  }
}
```

#### UPDATE - buildings/ - Editar imóvel do usuário

##### Authentication

- O usuário somente poderá executar com sucesso o request se for o dono do imóvel
- Rota Autenticada com Token
  No header da request usar:8000
  Authorization : Token hash_do_token

##### Exemplo de corpo da Request

obs: Os campos user e matricula são obrigatórios para localizar o imóvel, os demais pode-se utilizar apenas
o que se deseja alterar.

```json
{
  "user": 1,
  "matricula": 254135,
  "bairro": "Boa Viagem"
}
```

##### Responses

- STATUS 200 OK

```json
{
  "id": 2,
  "matricula": 254135,
  "tamanho": 123,
  "endereco": "Av Boa Viagem",
  "bairro": "Boa Viagem",
  "user": 1
}
```

- STATUS 404 NOT FOUND

```json
{
  "detail": "Not found."
}
```

- STATUS 400 BAD REQUEST

```json
{
  "message": {
    "missing_fields": ["matricula"]
  }
}
```

#### DELETE - buildings/ - Deletar imóvel do usuários

obs: Os campos user e matricula são obrigatórios para localizar o imóvel e o deletar.

##### Authentication

- O usuário somente poderá executar com sucesso o request se for o dono do imóvel
- Rota Autenticada com Token
  No header da request usar:8000
  Authorization : Token hash_do_token

##### Exemplo de corpo da Request

```json
{
  "matricula": "423423487",
  "user": 1
}
```

##### Responses

- STATUS 200 OK

```json
{
  "message": "Building 9 deleted"
}
```

- STATUS 404 NOT FOUND

```json
{
  "detail": "Not found."
}
```

- STATUS 400 BAD REQUEST

```json
{
  "message": {
    "missing_fields": ["matricula"]
  }
}
```
