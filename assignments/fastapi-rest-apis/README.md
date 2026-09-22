# 📘 Tarefa: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprenda a construir uma API REST usando o framework FastAPI, incluindo a criação de endpoints, validação de dados com Pydantic e operações CRUD básicas.

## 📝 Tasks

### 🛠️ Criar seu Primeiro Endpoint

#### Descrição
Crie uma aplicação FastAPI básica com um endpoint raiz e um endpoint que retorne informações sobre um item específico usando um parâmetro de rota.

#### Requisitos
O programa completo deve:

- Criar uma instância de `FastAPI` chamada `app`
- Definir uma rota `GET /` que retorne `{"message": "Welcome to the Task API"}`
- Definir uma rota `GET /tasks/{task_id}` que receba um `task_id` inteiro e retorne os dados do item correspondente
- Rodar localmente com `uvicorn` e testar os endpoints em `/docs`

### 🛠️ Validar Dados com Pydantic

#### Descrição
Crie um modelo Pydantic chamado `Task` para representar uma tarefa e utilize-o para validar os dados recebidos ao criar uma nova tarefa.

#### Requisitos
O programa completo deve:

- Definir um modelo `Task` com os campos `title` (str), `description` (str, opcional) e `completed` (bool, padrão `False`)
- Definir uma rota `POST /tasks` que receba um `Task` no corpo da requisição e o adicione a uma lista em memória
- Retornar a tarefa criada junto com um `id` gerado automaticamente
- Exemplo de requisição:
  ```json
  {
    "title": "Estudar FastAPI",
    "description": "Ler a documentação oficial"
  }
  ```

### 🛠️ Implementar CRUD Completo

#### Descrição
Expanda a API para suportar listagem, atualização e remoção de tarefas, retornando erros apropriados quando uma tarefa não existir.

#### Requisitos
O programa completo deve:

- Definir uma rota `GET /tasks` que retorne a lista completa de tarefas
- Definir uma rota `PUT /tasks/{task_id}` que atualize uma tarefa existente
- Definir uma rota `DELETE /tasks/{task_id}` que remova uma tarefa existente
- Retornar um erro `404 Not Found` com uma mensagem clara quando o `task_id` não existir
