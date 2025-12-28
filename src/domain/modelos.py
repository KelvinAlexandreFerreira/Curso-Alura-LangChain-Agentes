from typing import List
from pydantic import BaseModel, Field

class ExtratorDeEstudante(BaseModel):
    estudante: str = Field(description="Nome do estudante sempre em letras minúsculas. Exemplo: joão, carlos, joana, carla.")

class Nota(BaseModel):
    area: str = Field(description="Nome da área de conhecimento.")
    nota: float = Field(description="Nota obtida pelo estudante na área de conhecimento.")

class PerfilAcademicoDeEstudante(BaseModel):
    nome: str = Field(description="Nome do estudante.")
    ano_de_conclusao: int = Field(description="Ano de conclusão")
    notas: List[Nota] = Field(description="Lista de notas obtidas pelo estudante em suas disciplinas e áreas de conhecimentos.")
    resumo: str = Field(description="Resumo das principais características desse estudante de forma a torná-lo único e um ótimo potencial estudante para facultades. Exemplo: só este estudante tem bla bla bla.")