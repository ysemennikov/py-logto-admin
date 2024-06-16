from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_api_applications_application_id_sign_in_experience_body import (
    PutApiApplicationsApplicationIdSignInExperienceBody,
)
from ...models.put_api_applications_application_id_sign_in_experience_response_200 import (
    PutApiApplicationsApplicationIdSignInExperienceResponse200,
)
from ...types import Response


def _get_kwargs(
    application_id: str,
    *,
    body: PutApiApplicationsApplicationIdSignInExperienceBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/applications/{application_id}/sign-in-experience",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PutApiApplicationsApplicationIdSignInExperienceResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PutApiApplicationsApplicationIdSignInExperienceResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(Any, None)
        return response_201
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
) -> Response[Union[Any, PutApiApplicationsApplicationIdSignInExperienceResponse200]]:
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
    body: PutApiApplicationsApplicationIdSignInExperienceBody,
) -> Response[Union[Any, PutApiApplicationsApplicationIdSignInExperienceResponse200]]:
    """Update application level sign-in experience

     Update application level sign-in experience for the specified application. Create a new sign-in
    experience if it does not exist.
     - Only branding properties and terms links customization is supported for now.

     - Only third-party applications can be customized for now.

     - Application level sign-in experience customization is optional, if provided, it will override the
    default branding and terms links.

    Args:
        application_id (str):
        body (PutApiApplicationsApplicationIdSignInExperienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PutApiApplicationsApplicationIdSignInExperienceResponse200]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutApiApplicationsApplicationIdSignInExperienceBody,
) -> Optional[Union[Any, PutApiApplicationsApplicationIdSignInExperienceResponse200]]:
    """Update application level sign-in experience

     Update application level sign-in experience for the specified application. Create a new sign-in
    experience if it does not exist.
     - Only branding properties and terms links customization is supported for now.

     - Only third-party applications can be customized for now.

     - Application level sign-in experience customization is optional, if provided, it will override the
    default branding and terms links.

    Args:
        application_id (str):
        body (PutApiApplicationsApplicationIdSignInExperienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PutApiApplicationsApplicationIdSignInExperienceResponse200]
    """

    return sync_detailed(
        application_id=application_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutApiApplicationsApplicationIdSignInExperienceBody,
) -> Response[Union[Any, PutApiApplicationsApplicationIdSignInExperienceResponse200]]:
    """Update application level sign-in experience

     Update application level sign-in experience for the specified application. Create a new sign-in
    experience if it does not exist.
     - Only branding properties and terms links customization is supported for now.

     - Only third-party applications can be customized for now.

     - Application level sign-in experience customization is optional, if provided, it will override the
    default branding and terms links.

    Args:
        application_id (str):
        body (PutApiApplicationsApplicationIdSignInExperienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PutApiApplicationsApplicationIdSignInExperienceResponse200]]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutApiApplicationsApplicationIdSignInExperienceBody,
) -> Optional[Union[Any, PutApiApplicationsApplicationIdSignInExperienceResponse200]]:
    """Update application level sign-in experience

     Update application level sign-in experience for the specified application. Create a new sign-in
    experience if it does not exist.
     - Only branding properties and terms links customization is supported for now.

     - Only third-party applications can be customized for now.

     - Application level sign-in experience customization is optional, if provided, it will override the
    default branding and terms links.

    Args:
        application_id (str):
        body (PutApiApplicationsApplicationIdSignInExperienceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PutApiApplicationsApplicationIdSignInExperienceResponse200]
    """

    return (
        await asyncio_detailed(
            application_id=application_id,
            client=client,
            body=body,
        )
    ).parsed
