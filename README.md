## Omie's Python SDK

![Omie's Logo](https://raw.githubusercontent.com/morais90/omie-client/main/assets/omie-logo.jpeg)
<p align="center">An unofficial implementation of Omie's API. </p>

[![codecov](https://codecov.io/github/morais90/omie-client/graph/badge.svg?token=09Q1ENULCS)](https://codecov.io/github/morais90/omie-client)


For a full reference of the API documentation look at Omie [Developer Portal](https://developer.omie.com.br/)

### Installation:
```shell
$ pip install omie-client
```

### Getting started
```python
>>> from omie_client import OmieClient
>>> omie_client = OmieClient(app_key="your-app-key", app_secret="your-app-secret")
>>> payment = omie_client.accounts_payable.get_by_id(9873625)
Payment(
    codigo_lancamento_omie=9873625,
    codigo_lancamento_integracao='MAJAWg',
    codigo_cliente_fornecedor=9809218639,
    data_vencimento=datetime.date(2024, 5, 14),
    ....
)
```

### Features

Our foundation is built upon established and modern libraries.

- [HTTPX - A next-generation HTTP client for Python.](https://github.com/encode/httpx)
- [Pydantic - Data validation using Python type hints.](https://github.com/pydantic/pydantic)

### Contributing

Would you like to support this project and help it progress 🙏✨? Follow our [Contributing Guidelines](CONTRIBUTING.md)
