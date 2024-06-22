import typing
from datetime import date
from decimal import Decimal

from pydantic.dataclasses import dataclass

from omie_client.endpoint import Endpoint


@dataclass(frozen=True)
class Payment:
    codigo_lancamento_omie: int
    codigo_lancamento_integracao: str
    codigo_cliente_fornecedor: int
    codigo_cliente_fornecedor_integracao: str
    data_vencimento: date
    valor_documento: Decimal
    codigo_categoria: str
    data_previsao: str
    id_conta_corrente: int
    observacao: str
    valor_pis: Decimal
    retem_pis: bool
    valor_cofins: Decimal
    retem_cofins: bool
    valor_csll: Decimal
    retem_csll: bool
    valor_ir: Decimal
    retem_ir: bool
    valor_iss: Decimal
    retem_iss: bool
    numero_pedido: str
    status_titulo: str
    codigo_barras_ficha_compensacao: str


class AccountsPayable(Endpoint):
    ENDPOINT_URL: typing.ClassVar[str] = "/v1/financas/contapagar/"

    def get_by_erp_id(self, erp_id: int) -> Payment:
        response = self._omie_client.request(
            self.ENDPOINT_URL,
            data={
                "call": "ConsultarContaPagar",
                "param": [{"codigo_lancamento_omie": erp_id}],
            },
        )

        return Payment(**response)
