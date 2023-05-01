from typing import List, Dict, Any, Optional

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends

from fastapi import Path
from time import sleep

from models import Curso
from models import cursos


def fake_db():
    try:
        print("Abrindo conexao com banco de dados")
        #sleep(1)
    finally:
        print("fechando conexao com o banco de dados")
        #sleep(1)


app = FastAPI(title="API de Cursos Geek university",
              version="0.0.1",
              description="Uma API para estudo do FastAPI")


@app.get("/cursos",
         description='Retorna totos od cursos ou uma lista vazia',
         summary='Consultar cursos',
         response_model=List[Curso],
         response_description='Cursos encontrados com sucesso.')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int = Path(default=None, title="ID do curso",
                                         description="Deve ser entre 1 e 3", gt=-1, lt=4), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso nao encontrado.')


@app.post("/cursos", status_code=status.HTTP_201_CREATED,
          response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso


@app.put("/cursos/{curso_id}", status_code=status.HTTP_200_OK)
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nao existe um curso com o ID {curso_id}")


@app.delete("/cursos/{curso_id}", status_code=status.HTTP_200_OK)
async def delete_curso(curso_id: int, db: Any = Depends(fake_db), curso=Curso):
    curso.id = curso_id
    if curso.id in cursos:
        curso = cursos[curso.id]
        del cursos[curso.id]
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"O curso com o ID {curso_id} NAO existe.")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
