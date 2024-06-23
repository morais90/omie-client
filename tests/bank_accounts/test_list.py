from dataclasses import asdict

import httpx
import pytest

from omie_client.bank_accounts import BankAccountListParams, BankAccounts


@pytest.mark.respx(base_url="https://app.omie.com.br/api")
class TestBankAccountsList:
    def test_list(self, bank_accounts_payload, respx_mock, bank_accounts):
        respx_mock.post(BankAccounts.ENDPOINT_URL).mock(
            return_value=httpx.Response(status_code=200, json=bank_accounts_payload)
        )

        paginated_response = bank_accounts.list(params=BankAccountListParams(pagina=1))

        assert asdict(paginated_response) == {
            "pagina": 1,
            "total_de_paginas": 1,
            "registros": 3,
            "total_de_registros": 3,
            "items": [
                {
                    "codigo_banco": "999",
                    "codigo_agencia": None,
                    "numero_conta_corrente": None,
                    "descricao": "Caixinha",
                    "inativo": False,
                    "tipo": "CX",
                    "codigo": 7693914365,
                },
                {
                    "codigo_banco": "450",
                    "codigo_agencia": None,
                    "numero_conta_corrente": None,
                    "descricao": "Omie.CASH  - Ative agora",
                    "inativo": True,
                    "tipo": "CC",
                    "codigo": 7693914630,
                },
                {
                    "codigo_banco": "341",
                    "codigo_agencia": "1212",
                    "numero_conta_corrente": "1111-1",
                    "descricao": "Itaú Unibanco",
                    "inativo": False,
                    "tipo": "CC",
                    "codigo": 7694063362,
                },
            ],
        }

    def test_list_with_inactive_account(self, bank_accounts_payload, respx_mock, bank_accounts):
        bank_accounts_payload["ListarContasCorrentes"][0]["inativo"] = "S"

        respx_mock.post(BankAccounts.ENDPOINT_URL).mock(
            return_value=httpx.Response(status_code=200, json=bank_accounts_payload)
        )

        paginated_response = bank_accounts.list(params=BankAccountListParams(pagina=1))

        assert asdict(paginated_response) == {
            "pagina": 1,
            "total_de_paginas": 1,
            "registros": 3,
            "total_de_registros": 3,
            "items": [
                {
                    "codigo_banco": "999",
                    "codigo_agencia": None,
                    "numero_conta_corrente": None,
                    "descricao": "Caixinha",
                    "inativo": True,
                    "tipo": "CX",
                    "codigo": 7693914365,
                },
                {
                    "codigo_banco": "450",
                    "codigo_agencia": None,
                    "numero_conta_corrente": None,
                    "descricao": "Omie.CASH  - Ative agora",
                    "inativo": True,
                    "tipo": "CC",
                    "codigo": 7693914630,
                },
                {
                    "codigo_banco": "341",
                    "codigo_agencia": "1212",
                    "numero_conta_corrente": "1111-1",
                    "descricao": "Itaú Unibanco",
                    "inativo": False,
                    "tipo": "CC",
                    "codigo": 7694063362,
                },
            ],
        }
