# 📘 Tarefa: Construindo APIs REST com Express

## 🎯 Objective

Aprenda a construir uma API REST usando Node.js e o framework Express, incluindo a criação de rotas, tratamento do corpo das requisições e operações CRUD básicas.

## 📝 Tasks

### 🛠️ Criar seu Primeiro Servidor

#### Descrição
Crie um servidor Express básico com uma rota raiz e uma rota que retorne informações sobre uma tarefa específica usando um parâmetro de rota.

#### Requisitos
O programa completo deve:

- Criar uma instância do Express chamada `app`
- Definir uma rota `GET /` que retorne `{"message": "Welcome to the Task API"}`
- Definir uma rota `GET /tasks/:taskId` que receba um `taskId` e retorne os dados do item correspondente
- Iniciar o servidor com `app.listen()` na porta `3000`

### 🛠️ Validar Dados e Criar Tarefas

#### Descrição
Utilize o middleware `express.json()` para processar o corpo das requisições e crie uma rota para adicionar novas tarefas a uma lista em memória.

#### Requisitos
O programa completo deve:

- Configurar o middleware `express.json()` na aplicação
- Definir uma rota `POST /tasks` que receba `title` (string) e `description` (string, opcional) no corpo da requisição
- Validar que `title` foi enviado, retornando `400 Bad Request` caso contrário
- Adicionar a tarefa à lista em memória com um `id` gerado automaticamente e retornar a tarefa criada
- Exemplo de requisição:
  ```json
  {
    "title": "Estudar Express",
    "description": "Ler a documentação oficial"
  }
  ```

### 🛠️ Implementar CRUD Completo

#### Descrição
Expanda a API para suportar listagem, atualização e remoção de tarefas, retornando erros apropriados quando uma tarefa não existir.

#### Requisitos
O programa completo deve:

- Definir uma rota `GET /tasks` que retorne a lista completa de tarefas
- Definir uma rota `PUT /tasks/:taskId` que atualize uma tarefa existente
- Definir uma rota `DELETE /tasks/:taskId` que remova uma tarefa existente
- Retornar um erro `404 Not Found` com uma mensagem clara quando o `taskId` não existir
