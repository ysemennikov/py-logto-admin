from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_configs_oidc_key_type_rotate_body import PostApiConfigsOidcKeyTypeRotateBody
from ...models.post_api_configs_oidc_key_type_rotate_key_type import PostApiConfigsOidcKeyTypeRotateKeyType
from ...models.post_api_configs_oidc_key_type_rotate_response_200_item import (
    PostApiConfigsOidcKeyTypeRotateResponse200Item,
)
from ...types import Response


def _get_kwargs(
    key_type: PostApiConfigsOidcKeyTypeRotateKeyType,
    *,
    body: PostApiConfigsOidcKeyTypeRotateBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/configs/oidc/{key_type}/rotate",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["PostApiConfigsOidcKeyTypeRotateResponse200Item"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PostApiConfigsOidcKeyTypeRotateResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["PostApiConfigsOidcKeyTypeRotateResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_type: PostApiConfigsOidcKeyTypeRotateKeyType,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiConfigsOidcKeyTypeRotateBody,
) -> Response[Union[Any, List["PostApiConfigsOidcKeyTypeRotateResponse200Item"]]]:
    """Rotate OIDC keys

     A new key will be generated and prepend to the list of keys.

    Only two recent keys will be kept. The oldest key will be automatically removed if there are more
    than two keys.

    Args:
        key_type (PostApiConfigsOidcKeyTypeRotateKeyType):
        body (PostApiConfigsOidcKeyTypeRotateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['PostApiConfigsOidcKeyTypeRotateResponse200Item']]]
    """

    kwargs = _get_kwargs(
        key_type=key_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_type: PostApiConfigsOidcKeyTypeRotateKeyType,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiConfigsOidcKeyTypeRotateBody,
) -> Optional[Union[Any, List["PostApiConfigsOidcKeyTypeRotateResponse200Item"]]]:
    """Rotate OIDC keys

     A new key will be generated and prepend to the list of keys.

    Only two recent keys will be kept. The oldest key will be automatically removed if there are more
    than two keys.

    Args:
        key_type (PostApiConfigsOidcKeyTypeRotateKeyType):
        body (PostApiConfigsOidcKeyTypeRotateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['PostApiConfigsOidcKeyTypeRotateResponse200Item']]
    """

    return sync_detailed(
        key_type=key_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    key_type: PostApiConfigsOidcKeyTypeRotateKeyType,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiConfigsOidcKeyTypeRotateBody,
) -> Response[Union[Any, List["PostApiConfigsOidcKeyTypeRotateResponse200Item"]]]:
    """Rotate OIDC keys

     A new key will be generated and prepend to the list of keys.

    Only two recent keys will be kept. The oldest key will be automatically removed if there are more
    than two keys.

    Args:
        key_type (PostApiConfigsOidcKeyTypeRotateKeyType):
        body (PostApiConfigsOidcKeyTypeRotateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['PostApiConfigsOidcKeyTypeRotateResponse200Item']]]
    """

    kwargs = _get_kwargs(
        key_type=key_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_type: PostApiConfigsOidcKeyTypeRotateKeyType,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiConfigsOidcKeyTypeRotateBody,
) -> Optional[Union[Any, List["PostApiConfigsOidcKeyTypeRotateResponse200Item"]]]:
    """Rotate OIDC keys

     A new key will be generated and prepend to the list of keys.

    Only two recent keys will be kept. The oldest key will be automatically removed if there are more
    than two keys.

    Args:
        key_type (PostApiConfigsOidcKeyTypeRotateKeyType):
        body (PostApiConfigsOidcKeyTypeRotateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['PostApiConfigsOidcKeyTypeRotateResponse200Item']]
    """

    return (
        await asyncio_detailed(
            key_type=key_type,
            client=client,
            body=body,
        )
    ).parsed
