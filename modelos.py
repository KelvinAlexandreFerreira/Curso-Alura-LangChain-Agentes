from pydantic import BaseModel, Field

class ExtratorDeEstudante(BaseModel):
    estudante: str = Field(description="Nome do estudante sempre em letras minúsculas. Exemplo: joão, carlos, joana, carla.")