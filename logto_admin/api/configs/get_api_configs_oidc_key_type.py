from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_configs_oidc_key_type_key_type import GetApiConfigsOidcKeyTypeKeyType
from ...models.get_api_configs_oidc_key_type_response_200_item import GetApiConfigsOidcKeyTypeResponse200Item
from ...types import Response


def _get_kwargs(
    key_type: GetApiConfigsOidcKeyTypeKeyType,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/configs/oidc/{key_type}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["GetApiConfigsOidcKeyTypeResponse200Item"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetApiConfigsOidcKeyTypeResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["GetApiConfigsOidcKeyTypeResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_type: GetApiConfigsOidcKeyTypeKeyType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, List["GetApiConfigsOidcKeyTypeResponse200Item"]]]:
    """Get OIDC keys

     Get OIDC signing keys by key type. The actual key will be redacted from the result.

    Args:
        key_type (GetApiConfigsOidcKeyTypeKeyType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetApiConfigsOidcKeyTypeResponse200Item']]]
    """

    kwargs = _get_kwargs(
        key_type=key_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_type: GetApiConfigsOidcKeyTypeKeyType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, List["GetApiConfigsOidcKeyTypeResponse200Item"]]]:
    """Get OIDC keys

     Get OIDC signing keys by key type. The actual key will be redacted from the result.

    Args:
        key_type (GetApiConfigsOidcKeyTypeKeyType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetApiConfigsOidcKeyTypeResponse200Item']]
    """

    return sync_detailed(
        key_type=key_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    key_type: GetApiConfigsOidcKeyTypeKeyType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, List["GetApiConfigsOidcKeyTypeResponse200Item"]]]:
    """Get OIDC keys

     Get OIDC signing keys by key type. The actual key will be redacted from the result.

    Args:
        key_type (GetApiConfigsOidcKeyTypeKeyType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetApiConfigsOidcKeyTypeResponse200Item']]]
    """

    kwargs = _get_kwargs(
        key_type=key_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_type: GetApiConfigsOidcKeyTypeKeyType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, List["GetApiConfigsOidcKeyTypeResponse200Item"]]]:
    """Get OIDC keys

     Get OIDC signing keys by key type. The actual key will be redacted from the result.

    Args:
        key_type (GetApiConfigsOidcKeyTypeKeyType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetApiConfigsOidcKeyTypeResponse200Item']]
    """

    return (
        await asyncio_detailed(
            key_type=key_type,
            client=client,
        )
    ).parsed
