from dataclasses import asdict
from datetime import date
from decimal import Decimal

import httpx
import pytest

from omie_client.accounts_payable import AccountsPayable


@pytest.mark.respx(base_url="https://app.omie.com.br/api")
class TestGetById:
    def test_get_byid(self, accounts_payable, payment_payload, respx_mock):
        respx_mock.post(AccountsPayable.ENDPOINT_URL).mock(
            return_value=httpx.Response(status_code=200, json=payment_payload)
        )

        payment = accounts_payable.get_by_id(99999)
        assert asdict(payment) == {
            "codigo_lancamento_omie": 9809218643,
            "codigo_lancamento_integracao": "00000-1111111111",
            "codigo_cliente_fornecedor": 9809218639,
            "codigo_cliente_fornecedor_integracao": "",
            "data_vencimento": date(2024, 5, 14),
            "valor_documento": Decimal("1612.05"),
            "codigo_categoria": "2.01.96",
            "data_previsao": date(2024, 5, 14),
            "id_conta_corrente": 9788222289,
            "observacao": "",
            "valor_pis": Decimal("0"),
            "retem_pis": False,
            "valor_cofins": Decimal("0"),
            "retem_cofins": False,
            "valor_csll": Decimal("0"),
            "retem_csll": False,
            "valor_ir": Decimal("0"),
            "retem_ir": False,
            "valor_iss": Decimal("0"),
            "retem_iss": False,
            "numero_pedido": "111111",
            "status_titulo": "PAGO",
            "codigo_barras_ficha_compensacao": "",
        }

    def test_get_by_id_withfolding_field_as_true(self, accounts_payable, payment_payload, respx_mock):
        payment_payload.update(
            {"retem_pis": "S", "retem_cofins": "S", "retem_csll": "S", "retem_ir": "S", "retem_iss": "S"}
        )

        respx_mock.post(AccountsPayable.ENDPOINT_URL).mock(
            return_value=httpx.Response(status_code=200, json=payment_payload)
        )

        payment = accounts_payable.get_by_id(99999)

        assert payment.retem_pis is True
        assert payment.retem_cofins is True
        assert payment.retem_csll is True
        assert payment.retem_ir is True
        assert payment.retem_iss is True
