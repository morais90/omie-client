import httpx
from pydantic import HttpUrl

from omie_client.accounts_payable import AccountsPayable
from omie_client.exceptions import OmieBlockedError, OmieRequestError


class OmieClient:
    def __init__(
        self,
        app_key: str,
        app_secret: str,
        api_base_url: HttpUrl = "https://app.omie.com.br/api",
        default_timeout: int = 5,
    ):
        self._app_key = app_key
        self._app_secret = app_secret
        self._client = httpx.Client(base_url=api_base_url, timeout=default_timeout, http2=True)

    def request(self, url: str, data: dict):
        authenticated_data = {
            "app_key": self._app_key,
            "app_secret": self._app_secret,
            **data,
        }

        try:
            response = self._client.post(url, json=authenticated_data)
            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 500:
                error_data = e.response.json()

                raise OmieRequestError(
                    status_code=e.response.status_code,
                    code=error_data.get("code", "SOAP-ENV:Unknown-error"),
                    message=error_data.get("faultstring", "Unknown error"),
                )

            elif e.response.status_code == 403:
                raise OmieBlockedError

    @property
    def accounts_payable(self):
        return AccountsPayable(self)
