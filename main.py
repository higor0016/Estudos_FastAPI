from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
from typing import List
from model import Genero, Funcao, Usuario, Atualiza_Usuario

app = FastAPI()
db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primeiro_nome="Higor",
        sobrenome="Lucas",
        genero=Genero.masculino,
        funcoes=[Funcao.admin],
    ),
    Usuario(
        id=uuid4(),
        primeiro_nome="Márcio",
        sobrenome="José",
        genero=Genero.masculino,
        funcoes=[Funcao.usuario],
    ),
    Usuario(
        id=uuid4(),
        primeiro_nome="Joana",
        sobrenome="Jesus",
        genero=Genero.feminino,
        funcoes=[Funcao.usuario],
    ),
    Usuario(
        id=uuid4(),
        primeiro_nome="Lucas",
        sobrenome="Gomes",
        genero=Genero.masculino,
        funcoes=[Funcao.usuario],
    ),

]

@app.get("/api/v1/users")
async def get_users():
    return db

@app.post("/api/v1/users")
async def create_users(user: Usuario):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/users{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(status_code=404, detail=f'Delete falhou, id {id} não encontrado')

@app.put("/api/v1/users{id}")
async def atualiza_usuario(atualiza_usuario: Atualiza_Usuario, id: UUID):
    for user in db:
        if user.id == id:
            if atualiza_usuario.primeiro_nome is not None:
                user.primeiro_nome = atualiza_usuario.primeiro_nome
            if atualiza_usuario.sobrenome is not None:
                user.sobrenome = atualiza_usuario.sobrenome
            if atualiza_usuario.funcoes is not None:
                user.funcoes = atualiza_usuario.funcoes
            return user.id
    raise HTTPException(status_code=404, detail=f"Não pôde ser encontrado usuário com o ID: {id}")

