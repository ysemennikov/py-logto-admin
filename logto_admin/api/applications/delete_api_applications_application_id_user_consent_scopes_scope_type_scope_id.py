from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_api_applications_application_id_user_consent_scopes_scope_type_scope_id_scope_type import (
    DeleteApiApplicationsApplicationIdUserConsentScopesScopeTypeScopeIdScopeType,
)
from ...types import Response


def _get_kwargs(
    application_id: str,
    scope_type: DeleteApiApplicationsApplicationIdUserConsentScopesScopeTypeScopeIdScopeType,
    scope_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/applications/{application_id}/user-consent-scopes/{scope_type}/{scope_id}",
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
    application_id: str,
    scope_type: DeleteApiApplicationsApplicationIdUserConsentScopesScopeTypeScopeIdScopeType,
    scope_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Remove user consent scope from application.

     Remove the user consent scope from an application by application id, scope type and scope id

    Args:
        application_id (str):
        scope_type (DeleteApiApplicationsApplicationIdUserConsentScopesScopeTypeScopeIdScopeType):
        scope_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        scope_type=scope_type,
        scope_id=scope_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    application_id: str,
    scope_type: DeleteApiApplicationsApplicationIdUserConsentScopesScopeTypeScopeIdScopeType,
    scope_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Remove user consent scope from application.

     Remove the user consent scope from an application by application id, scope type and scope id

    Args:
        application_id (str):
        scope_type (DeleteApiApplicationsApplicationIdUserConsentScopesScopeTypeScopeIdScopeType):
        scope_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        scope_type=scope_type,
        scope_id=scope_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
