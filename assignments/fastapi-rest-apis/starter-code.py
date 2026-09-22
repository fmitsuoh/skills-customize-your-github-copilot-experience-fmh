# Código Inicial para a Tarefa de APIs REST com FastAPI
# Instale as dependências antes de começar: pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Tarefa 1: Criar seu Primeiro Endpoint
# Preencha as rotas abaixo


@app.get("/")
def read_root():
    # Retornar mensagem de boas-vindas
    pass


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    # Retornar os dados da tarefa correspondente
    pass


# Tarefa 2: Validar Dados com Pydantic
# Defina o modelo Task abaixo

class Task(BaseModel):
    pass


# Lista em memória para armazenar as tarefas
tasks = []


@app.post("/tasks")
def create_task(task: Task):
    # Adicionar a tarefa à lista com um id gerado automaticamente
    pass


# Tarefa 3: Implementar CRUD Completo
# Adicione as rotas GET (lista), PUT e DELETE descritas na tarefa

# Para rodar a aplicação:
# uvicorn starter-code:app --reload
