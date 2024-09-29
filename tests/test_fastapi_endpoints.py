from src.main import *
from datetime import datetime
from unittest.mock import patch


def test_root():
    assert root() == {"message": "Bem-vindo à API!"}


def test_get_data_atual_retorno():
    with patch('src.main.datetime') as mock_datetime:
        mock_datetime.now.return_value = datetime(2024, 7, 29, 14, 30)
        ret = get_data_atual()

    assert ret == {"data_atual": datetime(2024, 7, 29, 14, 30).strftime("%d/%m/%Y - %H:%M")}


def test_se_nao_e_data_futura():
    ret = get_data_atual()
    data_retorno = datetime.strptime(ret["data_atual"], "%d/%m/%Y - %H:%M")
    assert data_retorno.date() == datetime.now().date()


def test_quadrado_sem_param():
    assert quadrado() == {"message": "x não encontrado no query param"}


def test_quadrado_de_2():
    assert quadrado(2) == {"quadrado": 4}


def test_quadrado_de_negativo_tem_que_ser_positivo():
    ret = quadrado(-5)
    assert ret['quadrado'] >= 0

