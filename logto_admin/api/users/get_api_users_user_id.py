from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_users_user_id_response_200 import GetApiUsersUserIdResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    include_sso_identities: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["includeSsoIdentities"] = include_sso_identities

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/users/{user_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetApiUsersUserIdResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetApiUsersUserIdResponse200.from_dict(response.json())

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
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetApiUsersUserIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_sso_identities: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetApiUsersUserIdResponse200]]:
    """Get user

     Get user data for the given ID.

    Args:
        user_id (str):
        include_sso_identities (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiUsersUserIdResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        include_sso_identities=include_sso_identities,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_sso_identities: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetApiUsersUserIdResponse200]]:
    """Get user

     Get user data for the given ID.

    Args:
        user_id (str):
        include_sso_identities (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiUsersUserIdResponse200]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        include_sso_identities=include_sso_identities,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_sso_identities: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetApiUsersUserIdResponse200]]:
    """Get user

     Get user data for the given ID.

    Args:
        user_id (str):
        include_sso_identities (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiUsersUserIdResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        include_sso_identities=include_sso_identities,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include_sso_identities: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetApiUsersUserIdResponse200]]:
    """Get user

     Get user data for the given ID.

    Args:
        user_id (str):
        include_sso_identities (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiUsersUserIdResponse200]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            include_sso_identities=include_sso_identities,
        )
    ).parsed
