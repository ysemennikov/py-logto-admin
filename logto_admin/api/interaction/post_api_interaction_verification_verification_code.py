from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_interaction_verification_verification_code_body_type_0 import (
    PostApiInteractionVerificationVerificationCodeBodyType0,
)
from ...models.post_api_interaction_verification_verification_code_body_type_1 import (
    PostApiInteractionVerificationVerificationCodeBodyType1,
)
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        "PostApiInteractionVerificationVerificationCodeBodyType0",
        "PostApiInteractionVerificationVerificationCodeBodyType1",
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/interaction/verification/verification-code",
    }

    _body: Dict[str, Any]
    if isinstance(body, PostApiInteractionVerificationVerificationCodeBodyType0):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "PostApiInteractionVerificationVerificationCodeBodyType0",
        "PostApiInteractionVerificationVerificationCodeBodyType1",
    ],
) -> Response[Any]:
    """
    Args:
        body (Union['PostApiInteractionVerificationVerificationCodeBodyType0',
            'PostApiInteractionVerificationVerificationCodeBodyType1']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "PostApiInteractionVerificationVerificationCodeBodyType0",
        "PostApiInteractionVerificationVerificationCodeBodyType1",
    ],
) -> Response[Any]:
    """
    Args:
        body (Union['PostApiInteractionVerificationVerificationCodeBodyType0',
            'PostApiInteractionVerificationVerificationCodeBodyType1']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
