from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_api_users_user_id_password_body import PatchApiUsersUserIdPasswordBody
from ...models.patch_api_users_user_id_password_response_200 import PatchApiUsersUserIdPasswordResponse200
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: PatchApiUsersUserIdPasswordBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/api/users/{user_id}/password",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PatchApiUsersUserIdPasswordResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PatchApiUsersUserIdPasswordResponse200.from_dict(response.json())

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
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PatchApiUsersUserIdPasswordResponse200]]:
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
    body: PatchApiUsersUserIdPasswordBody,
) -> Response[Union[Any, PatchApiUsersUserIdPasswordResponse200]]:
    """Update user password

     Update user password for the given ID.

    Args:
        user_id (str):
        body (PatchApiUsersUserIdPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PatchApiUsersUserIdPasswordResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiUsersUserIdPasswordBody,
) -> Optional[Union[Any, PatchApiUsersUserIdPasswordResponse200]]:
    """Update user password

     Update user password for the given ID.

    Args:
        user_id (str):
        body (PatchApiUsersUserIdPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PatchApiUsersUserIdPasswordResponse200]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiUsersUserIdPasswordBody,
) -> Response[Union[Any, PatchApiUsersUserIdPasswordResponse200]]:
    """Update user password

     Update user password for the given ID.

    Args:
        user_id (str):
        body (PatchApiUsersUserIdPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PatchApiUsersUserIdPasswordResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiUsersUserIdPasswordBody,
) -> Optional[Union[Any, PatchApiUsersUserIdPasswordResponse200]]:
    """Update user password

     Update user password for the given ID.

    Args:
        user_id (str):
        body (PatchApiUsersUserIdPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PatchApiUsersUserIdPasswordResponse200]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
