from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_applications_id_users_user_id_consent_organizations_response_200 import (
    GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    user_id: str,
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
        "url": f"/api/applications/{id}/users/{user_id}/consent-organizations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200.from_dict(response.json())

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
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200]]:
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
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Response[Union[Any, GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200]]:
    """List all the user consented organizations of a application.

     List all the user consented organizations for a application by application id and user id.

    Args:
        id (str):
        user_id (str):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
        page=page,
        page_size=page_size,
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
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Optional[Union[Any, GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200]]:
    """List all the user consented organizations of a application.

     List all the user consented organizations for a application by application id and user id.

    Args:
        id (str):
        user_id (str):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200]
    """

    return sync_detailed(
        id=id,
        user_id=user_id,
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Response[Union[Any, GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200]]:
    """List all the user consented organizations of a application.

     List all the user consented organizations for a application by application id and user id.

    Args:
        id (str):
        user_id (str):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Optional[Union[Any, GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200]]:
    """List all the user consented organizations of a application.

     List all the user consented organizations for a application by application id and user id.

    Args:
        id (str):
        user_id (str):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiApplicationsIdUsersUserIdConsentOrganizationsResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            user_id=user_id,
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
