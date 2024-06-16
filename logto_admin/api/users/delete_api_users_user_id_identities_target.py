from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_api_users_user_id_identities_target_response_200 import (
    DeleteApiUsersUserIdIdentitiesTargetResponse200,
)
from ...types import Response


def _get_kwargs(
    user_id: str,
    target: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/users/{user_id}/identities/{target}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeleteApiUsersUserIdIdentitiesTargetResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteApiUsersUserIdIdentitiesTargetResponse200.from_dict(response.json())

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
) -> Response[Union[Any, DeleteApiUsersUserIdIdentitiesTargetResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    target: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DeleteApiUsersUserIdIdentitiesTargetResponse200]]:
    """Delete social identity from user

     Delete a social identity from the user.

    Args:
        user_id (str):
        target (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteApiUsersUserIdIdentitiesTargetResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        target=target,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    target: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DeleteApiUsersUserIdIdentitiesTargetResponse200]]:
    """Delete social identity from user

     Delete a social identity from the user.

    Args:
        user_id (str):
        target (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteApiUsersUserIdIdentitiesTargetResponse200]
    """

    return sync_detailed(
        user_id=user_id,
        target=target,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    target: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, DeleteApiUsersUserIdIdentitiesTargetResponse200]]:
    """Delete social identity from user

     Delete a social identity from the user.

    Args:
        user_id (str):
        target (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteApiUsersUserIdIdentitiesTargetResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        target=target,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    target: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, DeleteApiUsersUserIdIdentitiesTargetResponse200]]:
    """Delete social identity from user

     Delete a social identity from the user.

    Args:
        user_id (str):
        target (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteApiUsersUserIdIdentitiesTargetResponse200]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            target=target,
            client=client,
        )
    ).parsed
