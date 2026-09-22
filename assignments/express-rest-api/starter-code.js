// Código Inicial para a Tarefa de APIs REST com Express
// Instale as dependências antes de começar: npm install express

const express = require("express");

const app = express();
app.use(express.json());

// Tarefa 1: Criar seu Primeiro Servidor
// Preencha as rotas abaixo

app.get("/", (req, res) => {
  // Retornar mensagem de boas-vindas
});

app.get("/tasks/:taskId", (req, res) => {
  // Retornar os dados da tarefa correspondente
});

// Lista em memória para armazenar as tarefas
const tasks = [];

// Tarefa 2: Validar Dados e Criar Tarefas
app.post("/tasks", (req, res) => {
  // Validar o corpo da requisição e adicionar a tarefa com um id gerado automaticamente
});

// Tarefa 3: Implementar CRUD Completo
// Adicione as rotas GET (lista), PUT e DELETE descritas na tarefa

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
