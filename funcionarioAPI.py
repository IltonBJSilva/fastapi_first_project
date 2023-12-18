import uvicorn
from fastapi import FastAPI
from colaborador import Colaborador

app = FastAPI()

'''
uvicorn main:app --reload
'''

@app.get("/funcionario")
async def root():
    funcionario = Colaborador(1, "João")
    return {"nome": funcionario.name, "id": funcionario.id}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
