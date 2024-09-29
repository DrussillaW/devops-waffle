"""
Este módulo implementa uma API FastAPI para rotas de exemplo.
"""

from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """
    Função que retorna a mensagem de boas-vindas.
    """
    return {"message": "Bem-vindo à API!"}


@app.get("/data_atual")
def get_data_atual():
    """
    Função que retorna a data e hora atuais.
    """
    return {"data_atual": datetime.now().strftime("%d/%m/%Y - %H:%M")}


@app.get("/quadrado")
def quadrado(qs_x: int = None):
    """
    Função que retorna o quadrado de um inteiro.
    """
    if qs_x is not None:
        return {"quadrado": qs_x * qs_x}

    return {"message": "x não encontrado no query param"}
