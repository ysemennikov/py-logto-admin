from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_well_known_phrases_response_200 import GetApiWellKnownPhrasesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lng: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["lng"] = lng

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/.well-known/phrases",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetApiWellKnownPhrasesResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetApiWellKnownPhrasesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetApiWellKnownPhrasesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    lng: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetApiWellKnownPhrasesResponse200]]:
    """Get localized phrases

     Get localized phrases based on the specified language.

    Args:
        lng (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiWellKnownPhrasesResponse200]]
    """

    kwargs = _get_kwargs(
        lng=lng,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    lng: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetApiWellKnownPhrasesResponse200]]:
    """Get localized phrases

     Get localized phrases based on the specified language.

    Args:
        lng (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiWellKnownPhrasesResponse200]
    """

    return sync_detailed(
        client=client,
        lng=lng,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    lng: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetApiWellKnownPhrasesResponse200]]:
    """Get localized phrases

     Get localized phrases based on the specified language.

    Args:
        lng (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiWellKnownPhrasesResponse200]]
    """

    kwargs = _get_kwargs(
        lng=lng,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    lng: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetApiWellKnownPhrasesResponse200]]:
    """Get localized phrases

     Get localized phrases based on the specified language.

    Args:
        lng (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiWellKnownPhrasesResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            lng=lng,
        )
    ).parsed
