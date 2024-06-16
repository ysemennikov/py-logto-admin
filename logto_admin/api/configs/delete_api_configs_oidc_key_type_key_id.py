from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_api_configs_oidc_key_type_key_id_key_type import DeleteApiConfigsOidcKeyTypeKeyIdKeyType
from ...types import Response


def _get_kwargs(
    key_type: DeleteApiConfigsOidcKeyTypeKeyIdKeyType,
    key_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/configs/oidc/{key_type}/{key_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_type: DeleteApiConfigsOidcKeyTypeKeyIdKeyType,
    key_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Delete OIDC key

     Delete an OIDC signing key by key type and key ID.

    Args:
        key_type (DeleteApiConfigsOidcKeyTypeKeyIdKeyType):
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        key_type=key_type,
        key_id=key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    key_type: DeleteApiConfigsOidcKeyTypeKeyIdKeyType,
    key_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Delete OIDC key

     Delete an OIDC signing key by key type and key ID.

    Args:
        key_type (DeleteApiConfigsOidcKeyTypeKeyIdKeyType):
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        key_type=key_type,
        key_id=key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
