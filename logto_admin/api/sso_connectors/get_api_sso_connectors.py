from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_sso_connectors_response_200_item import GetApiSsoConnectorsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/sso-connectors",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["GetApiSsoConnectorsResponse200Item"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetApiSsoConnectorsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
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
) -> Response[Union[Any, List["GetApiSsoConnectorsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Response[Union[Any, List["GetApiSsoConnectorsResponse200Item"]]]:
    """List SSO connectors

     Get SSO connectors with pagination. In addition to the raw SSO connector data, a copy of fetched or
    parsed IdP configs and a copy of connector provider's data will be attached.

    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetApiSsoConnectorsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Optional[Union[Any, List["GetApiSsoConnectorsResponse200Item"]]]:
    """List SSO connectors

     Get SSO connectors with pagination. In addition to the raw SSO connector data, a copy of fetched or
    parsed IdP configs and a copy of connector provider's data will be attached.

    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetApiSsoConnectorsResponse200Item']]
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Response[Union[Any, List["GetApiSsoConnectorsResponse200Item"]]]:
    """List SSO connectors

     Get SSO connectors with pagination. In addition to the raw SSO connector data, a copy of fetched or
    parsed IdP configs and a copy of connector provider's data will be attached.

    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetApiSsoConnectorsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Optional[Union[Any, List["GetApiSsoConnectorsResponse200Item"]]]:
    """List SSO connectors

     Get SSO connectors with pagination. In addition to the raw SSO connector data, a copy of fetched or
    parsed IdP configs and a copy of connector provider's data will be attached.

    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetApiSsoConnectorsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
