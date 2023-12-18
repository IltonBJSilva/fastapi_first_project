from fastapi import FastAPI
from colaborador import Colaborador

app = FastAPI()

'''
uvicorn main:app --reload
'''


@app.get("/email")
async def root():
    funcionario = Colaborador(1, "João")
    return {"nome": funcionario.name, "id": funcionario.id}



