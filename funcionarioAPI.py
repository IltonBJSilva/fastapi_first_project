import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from colaborador import Colaborador

app = FastAPI()

'''
uvicorn main:app --reload
'''

class Inputs(BaseModel):
    inp: int
    inp2: str

@app.get("/funcionario")
async def root():
    funcionario = Colaborador(1, "João")
    return {"nome": funcionario.name, "id": funcionario.id}


@app.post("/exemplo02")
def exemplo(inputs: Inputs) -> str:
    return inputs.inp2




if __name__ == "__main__":
    uvicorn.run(app, port=8000)
