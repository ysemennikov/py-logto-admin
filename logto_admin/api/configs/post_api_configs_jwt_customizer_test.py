from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_configs_jwt_customizer_test_body_type_0 import PostApiConfigsJwtCustomizerTestBodyType0
from ...models.post_api_configs_jwt_customizer_test_body_type_1 import PostApiConfigsJwtCustomizerTestBodyType1
from ...models.post_api_configs_jwt_customizer_test_response_200 import PostApiConfigsJwtCustomizerTestResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: Union["PostApiConfigsJwtCustomizerTestBodyType0", "PostApiConfigsJwtCustomizerTestBodyType1"],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/configs/jwt-customizer/test",
    }

    _body: Dict[str, Any]
    if isinstance(body, PostApiConfigsJwtCustomizerTestBodyType0):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostApiConfigsJwtCustomizerTestResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostApiConfigsJwtCustomizerTestResponse200.from_dict(response.json())

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
) -> Response[Union[Any, PostApiConfigsJwtCustomizerTestResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["PostApiConfigsJwtCustomizerTestBodyType0", "PostApiConfigsJwtCustomizerTestBodyType1"],
) -> Response[Union[Any, PostApiConfigsJwtCustomizerTestResponse200]]:
    """Test JWT customizer

     Test the JWT customizer script with the given sample context and sample token payload.

    Args:
        body (Union['PostApiConfigsJwtCustomizerTestBodyType0',
            'PostApiConfigsJwtCustomizerTestBodyType1']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostApiConfigsJwtCustomizerTestResponse200]]
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
    body: Union["PostApiConfigsJwtCustomizerTestBodyType0", "PostApiConfigsJwtCustomizerTestBodyType1"],
) -> Optional[Union[Any, PostApiConfigsJwtCustomizerTestResponse200]]:
    """Test JWT customizer

     Test the JWT customizer script with the given sample context and sample token payload.

    Args:
        body (Union['PostApiConfigsJwtCustomizerTestBodyType0',
            'PostApiConfigsJwtCustomizerTestBodyType1']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostApiConfigsJwtCustomizerTestResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["PostApiConfigsJwtCustomizerTestBodyType0", "PostApiConfigsJwtCustomizerTestBodyType1"],
) -> Response[Union[Any, PostApiConfigsJwtCustomizerTestResponse200]]:
    """Test JWT customizer

     Test the JWT customizer script with the given sample context and sample token payload.

    Args:
        body (Union['PostApiConfigsJwtCustomizerTestBodyType0',
            'PostApiConfigsJwtCustomizerTestBodyType1']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostApiConfigsJwtCustomizerTestResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["PostApiConfigsJwtCustomizerTestBodyType0", "PostApiConfigsJwtCustomizerTestBodyType1"],
) -> Optional[Union[Any, PostApiConfigsJwtCustomizerTestResponse200]]:
    """Test JWT customizer

     Test the JWT customizer script with the given sample context and sample token payload.

    Args:
        body (Union['PostApiConfigsJwtCustomizerTestBodyType0',
            'PostApiConfigsJwtCustomizerTestBodyType1']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostApiConfigsJwtCustomizerTestResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
