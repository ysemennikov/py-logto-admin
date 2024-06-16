from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_applications_application_id_sign_in_experience_response_200 import (
    GetApiApplicationsApplicationIdSignInExperienceResponse200,
)
from ...types import Response


def _get_kwargs(
    application_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/applications/{application_id}/sign-in-experience",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetApiApplicationsApplicationIdSignInExperienceResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetApiApplicationsApplicationIdSignInExperienceResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetApiApplicationsApplicationIdSignInExperienceResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetApiApplicationsApplicationIdSignInExperienceResponse200]]:
    """Get the application level sign-in experience

     Get application level sign-in experience for a given application.
     - Only branding properties and terms links customization is supported for now.

     - Only third-party applications can have the sign-in experience customization for now.

    Args:
        application_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiApplicationsApplicationIdSignInExperienceResponse200]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetApiApplicationsApplicationIdSignInExperienceResponse200]]:
    """Get the application level sign-in experience

     Get application level sign-in experience for a given application.
     - Only branding properties and terms links customization is supported for now.

     - Only third-party applications can have the sign-in experience customization for now.

    Args:
        application_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiApplicationsApplicationIdSignInExperienceResponse200]
    """

    return sync_detailed(
        application_id=application_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetApiApplicationsApplicationIdSignInExperienceResponse200]]:
    """Get the application level sign-in experience

     Get application level sign-in experience for a given application.
     - Only branding properties and terms links customization is supported for now.

     - Only third-party applications can have the sign-in experience customization for now.

    Args:
        application_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiApplicationsApplicationIdSignInExperienceResponse200]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetApiApplicationsApplicationIdSignInExperienceResponse200]]:
    """Get the application level sign-in experience

     Get application level sign-in experience for a given application.
     - Only branding properties and terms links customization is supported for now.

     - Only third-party applications can have the sign-in experience customization for now.

    Args:
        application_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiApplicationsApplicationIdSignInExperienceResponse200]
    """

    return (
        await asyncio_detailed(
            application_id=application_id,
            client=client,
        )
    ).parsed
