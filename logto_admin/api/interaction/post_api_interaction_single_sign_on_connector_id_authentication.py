from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_interaction_single_sign_on_connector_id_authentication_body import (
    PostApiInteractionSingleSignOnConnectorIdAuthenticationBody,
)
from ...models.post_api_interaction_single_sign_on_connector_id_authentication_response_200 import (
    PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200,
)
from ...types import Response


def _get_kwargs(
    connector_id: str,
    *,
    body: PostApiInteractionSingleSignOnConnectorIdAuthenticationBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/interaction/single-sign-on/{connector_id}/authentication",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiInteractionSingleSignOnConnectorIdAuthenticationBody,
) -> Response[Union[Any, PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200]]:
    """
    Args:
        connector_id (str):
        body (PostApiInteractionSingleSignOnConnectorIdAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200]]
    """

    kwargs = _get_kwargs(
        connector_id=connector_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiInteractionSingleSignOnConnectorIdAuthenticationBody,
) -> Optional[Union[Any, PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200]]:
    """
    Args:
        connector_id (str):
        body (PostApiInteractionSingleSignOnConnectorIdAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200]
    """

    return sync_detailed(
        connector_id=connector_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiInteractionSingleSignOnConnectorIdAuthenticationBody,
) -> Response[Union[Any, PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200]]:
    """
    Args:
        connector_id (str):
        body (PostApiInteractionSingleSignOnConnectorIdAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200]]
    """

    kwargs = _get_kwargs(
        connector_id=connector_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiInteractionSingleSignOnConnectorIdAuthenticationBody,
) -> Optional[Union[Any, PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200]]:
    """
    Args:
        connector_id (str):
        body (PostApiInteractionSingleSignOnConnectorIdAuthenticationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostApiInteractionSingleSignOnConnectorIdAuthenticationResponse200]
    """

    return (
        await asyncio_detailed(
            connector_id=connector_id,
            client=client,
            body=body,
        )
    ).parsed
