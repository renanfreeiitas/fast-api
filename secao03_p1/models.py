from typing import Optional

from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O titulo deve possuir ao menos 3 palavras')
        
        if value.islower():
            raise ValueError('O titulo deve ser capitalizado.')
        return value


cursos = [
    Curso(id=1, titulo='Programacao Para Leigos', aulas=42, horas=56),
    Curso(id=2, titulo='Programacao Especialista Java', aulas=112, horas=95)
]