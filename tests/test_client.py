import httpx
import pytest

from omie_client import OmieClient
from omie_client.exceptions import OmieBlockedError, OmieRateLimitError, OmieRequestError


@pytest.fixture
def omie_client():
    return OmieClient(app_key="fake-app-key", app_secret="fake-app-secret")


@pytest.mark.respx(base_url="https://app.omie.com.br/api")
class TestOmieClient:
    def test_request(self, omie_client, respx_mock):
        data = {"baz": 1, "qux": True}
        respx_mock.post("/fake-url").mock(return_value=httpx.Response(status_code=200, json=data))

        response = omie_client.request(url="fake-url", data={"foo": "bar"})
        assert response == data

    def test_request_on_403_error(self, omie_client, respx_mock):
        respx_mock.post("/fake-url").mock(
            return_value=httpx.Response(
                status_code=403,
                json={
                    "faultstring": "A chave de acesso está inválida ou o aplicativo está suspenso.",
                    "faultcode": "SOAP-ENV:Server",
                },
            )
        )

        with pytest.raises(OmieBlockedError):
            omie_client.request(url="fake-url", data={"foo": "bar"})

    def test_request_on_429_error(self, omie_client, respx_mock):
        respx_mock.post("/fake-url").mock(
            return_value=httpx.Response(
                status_code=429,
                json={"error_code": 429, "error_message": "Too Many Requests", "error_hash": "jkHayusgd"},
            )
        )

        with pytest.raises(OmieRateLimitError):
            omie_client.request(url="fake-url", data={"foo": "bar"})

    def test_request_on_500_error(self, omie_client, respx_mock):
        respx_mock.post("/fake-url").mock(
            return_value=httpx.Response(
                status_code=500,
                json={
                    "faultstring": "ERROR: Lançamento não cadastrado para o Código!",
                    "faultcode": "SOAP-ENV:Client-105",
                },
            )
        )

        with pytest.raises(OmieRequestError, match="ERROR: Lançamento não cadastrado para o Código!"):
            omie_client.request(url="fake-url", data={"foo": "bar"})
