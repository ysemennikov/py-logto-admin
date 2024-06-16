from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_configs_jwt_customizer_token_type_path_response_200_type_0 import (
    GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0,
)
from ...models.get_api_configs_jwt_customizer_token_type_path_response_200_type_1 import (
    GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1,
)
from ...models.get_api_configs_jwt_customizer_token_type_path_token_type_path import (
    GetApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
)
from ...types import Response


def _get_kwargs(
    token_type_path: GetApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/configs/jwt-customizer/{token_type_path}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        Union[
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ],
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[
    Union[
        Any,
        Union[
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token_type_path: GetApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        Any,
        Union[
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ],
    ]
]:
    """Get JWT customizer

     Get the JWT customizer for the given token type.

    Args:
        token_type_path (GetApiConfigsJwtCustomizerTokenTypePathTokenTypePath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0', 'GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1']]]
    """

    kwargs = _get_kwargs(
        token_type_path=token_type_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token_type_path: GetApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        Any,
        Union[
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ],
    ]
]:
    """Get JWT customizer

     Get the JWT customizer for the given token type.

    Args:
        token_type_path (GetApiConfigsJwtCustomizerTokenTypePathTokenTypePath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0', 'GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1']]
    """

    return sync_detailed(
        token_type_path=token_type_path,
        client=client,
    ).parsed


async def asyncio_detailed(
    token_type_path: GetApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        Any,
        Union[
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ],
    ]
]:
    """Get JWT customizer

     Get the JWT customizer for the given token type.

    Args:
        token_type_path (GetApiConfigsJwtCustomizerTokenTypePathTokenTypePath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0', 'GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1']]]
    """

    kwargs = _get_kwargs(
        token_type_path=token_type_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_type_path: GetApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        Any,
        Union[
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ],
    ]
]:
    """Get JWT customizer

     Get the JWT customizer for the given token type.

    Args:
        token_type_path (GetApiConfigsJwtCustomizerTokenTypePathTokenTypePath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['GetApiConfigsJwtCustomizerTokenTypePathResponse200Type0', 'GetApiConfigsJwtCustomizerTokenTypePathResponse200Type1']]
    """

    return (
        await asyncio_detailed(
            token_type_path=token_type_path,
            client=client,
        )
    ).parsed
