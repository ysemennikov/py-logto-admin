from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_api_configs_jwt_customizer_token_type_path_body import (
    PatchApiConfigsJwtCustomizerTokenTypePathBody,
)
from ...models.patch_api_configs_jwt_customizer_token_type_path_response_200_type_0 import (
    PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0,
)
from ...models.patch_api_configs_jwt_customizer_token_type_path_response_200_type_1 import (
    PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1,
)
from ...models.patch_api_configs_jwt_customizer_token_type_path_token_type_path import (
    PatchApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
)
from ...types import Response


def _get_kwargs(
    token_type_path: PatchApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
    *,
    body: PatchApiConfigsJwtCustomizerTokenTypePathBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/api/configs/jwt-customizer/{token_type_path}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        Union[
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ],
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1.from_dict(data)

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
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
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
    token_type_path: PatchApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiConfigsJwtCustomizerTokenTypePathBody,
) -> Response[
    Union[
        Any,
        Union[
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ],
    ]
]:
    """Update JWT customizer

     Update the JWT customizer for the given token type.

    Args:
        token_type_path (PatchApiConfigsJwtCustomizerTokenTypePathTokenTypePath):
        body (PatchApiConfigsJwtCustomizerTokenTypePathBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0', 'PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1']]]
    """

    kwargs = _get_kwargs(
        token_type_path=token_type_path,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    token_type_path: PatchApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiConfigsJwtCustomizerTokenTypePathBody,
) -> Optional[
    Union[
        Any,
        Union[
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ],
    ]
]:
    """Update JWT customizer

     Update the JWT customizer for the given token type.

    Args:
        token_type_path (PatchApiConfigsJwtCustomizerTokenTypePathTokenTypePath):
        body (PatchApiConfigsJwtCustomizerTokenTypePathBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0', 'PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1']]
    """

    return sync_detailed(
        token_type_path=token_type_path,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    token_type_path: PatchApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiConfigsJwtCustomizerTokenTypePathBody,
) -> Response[
    Union[
        Any,
        Union[
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ],
    ]
]:
    """Update JWT customizer

     Update the JWT customizer for the given token type.

    Args:
        token_type_path (PatchApiConfigsJwtCustomizerTokenTypePathTokenTypePath):
        body (PatchApiConfigsJwtCustomizerTokenTypePathBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0', 'PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1']]]
    """

    kwargs = _get_kwargs(
        token_type_path=token_type_path,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    token_type_path: PatchApiConfigsJwtCustomizerTokenTypePathTokenTypePath,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiConfigsJwtCustomizerTokenTypePathBody,
) -> Optional[
    Union[
        Any,
        Union[
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0",
            "PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1",
        ],
    ]
]:
    """Update JWT customizer

     Update the JWT customizer for the given token type.

    Args:
        token_type_path (PatchApiConfigsJwtCustomizerTokenTypePathTokenTypePath):
        body (PatchApiConfigsJwtCustomizerTokenTypePathBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type0', 'PatchApiConfigsJwtCustomizerTokenTypePathResponse200Type1']]
    """

    return (
        await asyncio_detailed(
            token_type_path=token_type_path,
            client=client,
            body=body,
        )
    ).parsed
