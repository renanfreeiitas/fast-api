from typing import Optional

from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(id=1, titulo='Programacao para leigos', aulas=42, horas=56),
    Curso(id=2, titulo='Programacao Java', aulas=112, horas=95)
]