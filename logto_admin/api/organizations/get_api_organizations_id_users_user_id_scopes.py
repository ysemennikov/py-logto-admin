from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_organizations_id_users_user_id_scopes_response_200_item import (
    GetApiOrganizationsIdUsersUserIdScopesResponse200Item,
)
from ...types import Response


def _get_kwargs(
    id: str,
    user_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/organizations/{id}/users/{user_id}/scopes",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["GetApiOrganizationsIdUsersUserIdScopesResponse200Item"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetApiOrganizationsIdUsersUserIdScopesResponse200Item.from_dict(response_200_item_data)

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
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["GetApiOrganizationsIdUsersUserIdScopesResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, List["GetApiOrganizationsIdUsersUserIdScopesResponse200Item"]]]:
    """Get scopes for a user in an organization tailored by the organization roles

     Get scopes assigned to a user in the specified organization tailored by the organization roles. The
    scopes are derived from the organization roles assigned to the user.

    Args:
        id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetApiOrganizationsIdUsersUserIdScopesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, List["GetApiOrganizationsIdUsersUserIdScopesResponse200Item"]]]:
    """Get scopes for a user in an organization tailored by the organization roles

     Get scopes assigned to a user in the specified organization tailored by the organization roles. The
    scopes are derived from the organization roles assigned to the user.

    Args:
        id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetApiOrganizationsIdUsersUserIdScopesResponse200Item']]
    """

    return sync_detailed(
        id=id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, List["GetApiOrganizationsIdUsersUserIdScopesResponse200Item"]]]:
    """Get scopes for a user in an organization tailored by the organization roles

     Get scopes assigned to a user in the specified organization tailored by the organization roles. The
    scopes are derived from the organization roles assigned to the user.

    Args:
        id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetApiOrganizationsIdUsersUserIdScopesResponse200Item']]]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, List["GetApiOrganizationsIdUsersUserIdScopesResponse200Item"]]]:
    """Get scopes for a user in an organization tailored by the organization roles

     Get scopes assigned to a user in the specified organization tailored by the organization roles. The
    scopes are derived from the organization roles assigned to the user.

    Args:
        id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetApiOrganizationsIdUsersUserIdScopesResponse200Item']]
    """

    return (
        await asyncio_detailed(
            id=id,
            user_id=user_id,
            client=client,
        )
    ).parsed
