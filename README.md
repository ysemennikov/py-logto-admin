# logto-admin
Python client for Logto Management API.

## What It Does:

The [py-logto-admin](https://github.com/ysemennikov/py-logto-admin) client allows you to interact with the Logto Management API seamlessly, making it easier to integrate Logto's authentication and user management features into your Python applications.

## Key Features:

- Asynchronous Support: Fully supports asynchronous operations.
- Modern Python: Utilizes the latest Python features, including type annotations and dataclasses, for enhanced code clarity and robustness.
- Comprehensive Documentation: Includes thorough documentation and usage instructions directly within the docstrings.
- Built on top of the OpenAPI Spec: Built using the [openapi-python-client](https://github.com/openapi-generators/openapi-python-client), which means the client is generated from the [Logto OpenAPI Specification](https://openapi.logto.io/operation/operation-get-api-swagger-json).

## Installation

```bash
# pip
pip install logto-admin

# poetry
poetry add logto-admin
```

## Usage

```python
import asyncio
import logto_admin

# Create a token manager first.
# It will manage the access token and refresh it every 3000 seconds.
token_manager = logto_admin.TokenManager(
    logto_endpoint="https://[tenant_id].logto.app",
    m2m_app_id="your-M2M-app-id",
    m2m_app_secret="your-M2M-app-secret",
)

# Fetch the initial access token.
# This can be done on startup of your app.
token_manager.fetch_token_info()

# Create an asyncio task for refreshing token periodically
asyncio.create_task(logto_m2m_token_manager.refresh_token_periodically())


# Create your own client class
class LogtoAdmin(logto_admin.AuthenticatedClient):
    """Logto Management API client"""

    def __init__(self) -> None:
        super().__init__(
            base_url="https://[tenant_id].logto.app/api",
            token=token_manager.token_info["access_token"],
            prefix=token_manager.token_info["token_type"],
        )


# Use the client
async def create_user():
    async with LogtoAdmin() as logto_admin_client:
        await logto_admin.api.users.post_api_users.asyncio(
            client=logto_admin_client,
            body=logto_admin.models.PostApiUsersBody(),
        )
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
class LogtoAdmin(logto_admin.AuthenticatedClient):
    """Logto Management API client"""

    def __init__(self) -> None:
        super().__init__(
            base_url="https://[tenant_id].logto.app/api",
            token=token_manager.token_info["access_token"],
            prefix=token_manager.token_info["token_type"],
            verify_ssl="/path/to/certificate_bundle.pem",
        )
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
class LogtoAdmin(logto_admin.AuthenticatedClient):
    """Logto Management API client"""

    def __init__(self) -> None:
        super().__init__(
            base_url="https://[tenant_id].logto.app/api",
            token=token_manager.token_info["access_token"],
            prefix=token_manager.token_info["token_type"],
            verify_ssl=False,
        )
```

Things to know:
1. Every path/method combo becomes a Python module with two functions:
    1. `asyncio`: Request that returns parsed data (if successful) or `None`
    2. `asyncio_detailed`: Always returns a `Request`, optionally with `parsed` set if the request was successful.

1. All path/query params, and bodies become method arguments.
1. If the endpoint had any tags on it, the first tag will be used as a module name for the function.
1. Any endpoint which did not have a tag will be in `logto_admin.api.default`

## Versioning

Current version is `0.117.*` - based on Logto 1.17.

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.AsyncClient`:

```python
from logto_admin import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.example.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from logto_admin import Client

client = Client(
    base_url="https://api.example.com",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.AsyncClient(base_url="https://api.example.com", proxies="http://localhost:8030"))
```
