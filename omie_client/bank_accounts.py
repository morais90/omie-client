import typing

from pydantic import Field, RootModel, TypeAdapter, field_validator
from pydantic.dataclasses import dataclass

from omie_client.endpoint import Endpoint

T = typing.TypeVar("T")


@dataclass(frozen=True)
class BankAccountListParams:
    pagina: int = Field(ge=0)
    codigo: int = None
    registros_por_pagina: int = Field(None, ge=1)


@dataclass(frozen=True)
class BankAccount:
    codigo_banco: str
    descricao: str
    inativo: bool
    tipo: str
    codigo_agencia: typing.Optional[str] = None
    numero_conta_corrente: typing.Optional[str] = None
    codigo: int = Field(..., alias="nCodCC")

    @field_validator("inativo", mode="before")
    @classmethod
    def parse_string_boolean(cls, value: str) -> bool:
        return value == "S"


@dataclass(frozen=True)
class PaginatedResponse(typing.Generic[T]):
    pagina: int
    total_de_paginas: int
    registros: int
    total_de_registros: int
    items: list[T]


class BankAccounts(Endpoint):
    ENDPOINT_URL: typing.ClassVar[str] = "/v1/geral/contacorrente/"

    def list(self, params: BankAccountListParams) -> PaginatedResponse[BankAccount]:
        response = self._omie_client.request(
            self.ENDPOINT_URL,
            data={
                "call": "ConsultarContaPagar",
                "param": [RootModel[BankAccountListParams](params).model_dump()],
            },
        )
        items = response.pop("ListarContasCorrentes")

        return PaginatedResponse(
            **response, items=TypeAdapter(list[BankAccount]).validate_python(items)
        )
