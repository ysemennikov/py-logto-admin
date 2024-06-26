from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_interaction_verification_social_authorization_uri_body import (
    PostApiInteractionVerificationSocialAuthorizationUriBody,
)
from ...models.post_api_interaction_verification_social_authorization_uri_response_200 import (
    PostApiInteractionVerificationSocialAuthorizationUriResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiInteractionVerificationSocialAuthorizationUriBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/interaction/verification/social-authorization-uri",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostApiInteractionVerificationSocialAuthorizationUriResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostApiInteractionVerificationSocialAuthorizationUriResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PostApiInteractionVerificationSocialAuthorizationUriResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiInteractionVerificationSocialAuthorizationUriBody,
) -> Response[Union[Any, PostApiInteractionVerificationSocialAuthorizationUriResponse200]]:
    """
    Args:
        body (PostApiInteractionVerificationSocialAuthorizationUriBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostApiInteractionVerificationSocialAuthorizationUriResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiInteractionVerificationSocialAuthorizationUriBody,
) -> Optional[Union[Any, PostApiInteractionVerificationSocialAuthorizationUriResponse200]]:
    """
    Args:
        body (PostApiInteractionVerificationSocialAuthorizationUriBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostApiInteractionVerificationSocialAuthorizationUriResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiInteractionVerificationSocialAuthorizationUriBody,
) -> Response[Union[Any, PostApiInteractionVerificationSocialAuthorizationUriResponse200]]:
    """
    Args:
        body (PostApiInteractionVerificationSocialAuthorizationUriBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostApiInteractionVerificationSocialAuthorizationUriResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiInteractionVerificationSocialAuthorizationUriBody,
) -> Optional[Union[Any, PostApiInteractionVerificationSocialAuthorizationUriResponse200]]:
    """
    Args:
        body (PostApiInteractionVerificationSocialAuthorizationUriBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostApiInteractionVerificationSocialAuthorizationUriResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
