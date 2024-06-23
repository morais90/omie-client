import pytest

from omie_client.bank_accounts import BankAccounts
from omie_client.client import OmieClient


@pytest.fixture
def bank_accounts_payload():
    return {
        "pagina": 1,
        "total_de_paginas": 1,
        "registros": 3,
        "total_de_registros": 3,
        "ListarContasCorrentes": [
            {
                "bloqueado": "N",
                "bol_instr1": "Sr. Caixa, receber até 10 dias após o vencimento.",
                "bol_sn": "N",
                "cobr_sn": "N",
                "codigo_banco": "999",
                "data_alt": "10\/05\/2024",
                "data_inc": "10\/05\/2024",
                "descricao": "Caixinha",
                "hora_alt": "17:38:20",
                "hora_inc": "17:38:20",
                "importado_api": "N",
                "inativo": "N",
                "nCodCC": 7693914365,
                "nao_fluxo": "N",
                "nao_resumo": "N",
                "pdv_categoria": "1.01.03",
                "pdv_enviar": "S",
                "pdv_sincr_analitica": "N",
                "pix_sn": "N",
                "saldo_inicial": 0,
                "tipo": "CX",
                "tipo_conta_corrente": "CX",
                "user_alt": "P000476429",
                "user_inc": "P000476429",
            },
            {
                "bloqueado": "S",
                "bol_sn": "N",
                "cobr_sn": "N",
                "codigo_banco": "450",
                "data_alt": "10\/05\/2024",
                "data_inc": "10\/05\/2024",
                "descricao": "Omie.CASH  - Ative agora",
                "hora_alt": "17:38:33",
                "hora_inc": "17:38:33",
                "importado_api": "N",
                "inativo": "S",
                "nCodCC": 7693914630,
                "nao_fluxo": "N",
                "nao_resumo": "N",
                "observacao": "Incluída automaticamente para a integração com o Omie.CASH.",
                "pdv_enviar": "N",
                "pdv_sincr_analitica": "N",
                "per_juros": 1,
                "per_multa": 2,
                "pix_sn": "N",
                "saldo_data": "10\/05\/2024",
                "saldo_inicial": 0,
                "tipo": "CC",
                "tipo_conta_corrente": "CC",
                "user_alt": "P000476429",
                "user_inc": "P000476429",
            },
            {
                "bloqueado": "N",
                "bol_sn": "N",
                "cobr_sn": "N",
                "codigo_agencia": "1212",
                "codigo_banco": "341",
                "data_alt": "11\/05\/2024",
                "data_inc": "11\/05\/2024",
                "descricao": "Itaú Unibanco",
                "hora_alt": "00:51:23",
                "hora_inc": "00:46:28",
                "importado_api": "N",
                "inativo": "N",
                "nCodCC": 7694063362,
                "nao_fluxo": "N",
                "nao_resumo": "N",
                "numero_conta_corrente": "1111-1",
                "pdv_enviar": "N",
                "pdv_sincr_analitica": "N",
                "pix_sn": "N",
                "saldo_inicial": 0,
                "tipo": "CC",
                "tipo_conta_corrente": "CC",
                "user_alt": "P000476429",
                "user_inc": "P000476429",
            },
        ],
    }


@pytest.fixture
def bank_accounts():
    omie_client = OmieClient(app_key="fake-app-key", app_secret="fake-app-secret")
    return BankAccounts(omie_client)
