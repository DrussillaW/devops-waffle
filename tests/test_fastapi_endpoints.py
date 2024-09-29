"""
Este módulo testa uma API FastAPI para rotas de exemplo.
"""

from datetime import datetime
from unittest.mock import patch
from src.main import root, get_data_atual, quadrado


def test_root():
    """
        Função que testa root.
    """
    assert root() == {"message": "Bem-vindo à API!"}


def test_get_data_atual_retorno():
    """
    Função que testa get_data_atual.
    """
    with patch('src.main.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime(2024, 7, 29, 14, 30)
        ret = get_data_atual()

    assert ret == {"data_atual": datetime(2024, 7, 29, 14, 30).strftime("%d/%m/%Y - %H:%M")}


def test_se_nao_e_data_futura():
    """
    Função que testa get_data_atual 2.
    """
    ret = get_data_atual()
    data_retorno = datetime.strptime(ret["data_atual"], "%d/%m/%Y - %H:%M")
    assert data_retorno.date() == datetime.now().date()


def test_quadrado_sem_param():
    """
    Função que testa quadrado sem parâmetro.

    """
    assert quadrado() == {"message": "x não encontrado no query param"}


def test_quadrado_de_2():
    """
   Função que testa quadrado com parâmetro.

   """
    assert quadrado(2) == {"quadrado": 4}


def test_quadrado_de_negativo_tem_que_ser_positivo():
    """
   Função que testa quadrado com parâmetro negativo.

   """
    ret = quadrado(-5)
    assert ret['quadrado'] >= 0
