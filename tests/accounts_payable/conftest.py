import pytest

from omie_client.accounts_payable import AccountsPayable
from omie_client.client import OmieClient


@pytest.fixture
def payment_payload():
    return {
        "codigo_lancamento_omie": 9809218643,
        "codigo_lancamento_integracao": "00000-1111111111",
        "codigo_cliente_fornecedor": 9809218639,
        "codigo_cliente_fornecedor_integracao": "",
        "data_vencimento": "14/05/2024",
        "valor_documento": 1612.05,
        "codigo_categoria": "2.01.96",
        "categorias": [{"codigo_categoria": "2.01.96", "percentual": 100, "valor": 1612.05}],
        "data_previsao": "14/05/2024",
        "id_conta_corrente": 9788222289,
        "numero_documento_fiscal": "700218",
        "data_emissao": "14/05/2024",
        "data_entrada": "14/05/2024",
        "codigo_projeto": 0,
        "observacao": "",
        "valor_pis": 0,
        "retem_pis": "N",
        "valor_cofins": 0,
        "retem_cofins": "N",
        "valor_csll": 0,
        "retem_csll": "N",
        "valor_ir": 0,
        "retem_ir": "N",
        "valor_iss": 0,
        "retem_iss": "N",
        "valor_inss": 0,
        "retem_inss": "N",
        "distribuicao": [],
        "numero_pedido": "111111",
        "codigo_tipo_documento": "NF",
        "numero_documento": "",
        "numero_parcela": "001/001",
        "chave_nfe": "",
        "codigo_barras_ficha_compensacao": "",
        "codigo_vendedor": 0,
        "id_origem": "APIP",
        "info": {
            "cImpAPI": "S",
            "dAlt": "19/06/2024",
            "dInc": "14/05/2024",
            "hAlt": "13:34:04",
            "hInc": "14:22:48",
            "uAlt": "P000822940",
            "uInc": "WEBSERVICE",
        },
        "operacao": "",
        "status_titulo": "PAGO",
        "nsu": "",
        "acao": "",
        "id_conta_corrente_integracao": "",
        "bloqueado": "",
        "baixa_bloqueada": "",
        "codigo_cmc7_cheque": "",
        "importado_api": "",
        "bloquear_exclusao": "N",
        "cnab_integracao_bancaria": None,
        "servico_tomado": None,
        "valor_pag": 0,
        "aprendizado_rateio": "",
    }


@pytest.fixture
def accounts_payable():
    omie_client = OmieClient(app_key="fake-app-key", app_secret="fake-app-secret")
    return AccountsPayable(omie_client)
