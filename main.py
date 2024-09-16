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
    return {"message": "Bem-vindo à API de datas!"}

@app.get("/data_atual")
def get_data_atual():
    """
    Função que retorna a data e hora atuais.
    """
    return {"data_atual": datetime.now().strftime("%d/%m/%Y - %H:%M")}