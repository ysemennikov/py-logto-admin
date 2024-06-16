from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_applications_id_users_user_id_consent_organizations_body import (
    PostApiApplicationsIdUsersUserIdConsentOrganizationsBody,
)
from ...types import Response


def _get_kwargs(
    id: str,
    user_id: str,
    *,
    body: PostApiApplicationsIdUsersUserIdConsentOrganizationsBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/applications/{id}/users/{user_id}/consent-organizations",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.CREATED:
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
    id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiApplicationsIdUsersUserIdConsentOrganizationsBody,
) -> Response[Any]:
    """Grant a list of organization access of a user for a application.

     Grant a list of organization access of a user for a application by application id and user id. <br/>
    The user must be a member of all the organizations. <br/> Only third-party application needs to be
    granted access to organizations, all the other applications can request for all the organizations'
    access by default.

    Args:
        id (str):
        user_id (str):
        body (PostApiApplicationsIdUsersUserIdConsentOrganizationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiApplicationsIdUsersUserIdConsentOrganizationsBody,
) -> Response[Any]:
    """Grant a list of organization access of a user for a application.

     Grant a list of organization access of a user for a application by application id and user id. <br/>
    The user must be a member of all the organizations. <br/> Only third-party application needs to be
    granted access to organizations, all the other applications can request for all the organizations'
    access by default.

    Args:
        id (str):
        user_id (str):
        body (PostApiApplicationsIdUsersUserIdConsentOrganizationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
