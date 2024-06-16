from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_api_interaction_identifiers_body_type_0 import PatchApiInteractionIdentifiersBodyType0
from ...models.patch_api_interaction_identifiers_body_type_1 import PatchApiInteractionIdentifiersBodyType1
from ...models.patch_api_interaction_identifiers_body_type_2 import PatchApiInteractionIdentifiersBodyType2
from ...models.patch_api_interaction_identifiers_body_type_3 import PatchApiInteractionIdentifiersBodyType3
from ...models.patch_api_interaction_identifiers_body_type_4 import PatchApiInteractionIdentifiersBodyType4
from ...models.patch_api_interaction_identifiers_body_type_5 import PatchApiInteractionIdentifiersBodyType5
from ...models.patch_api_interaction_identifiers_body_type_6 import PatchApiInteractionIdentifiersBodyType6
from ...models.patch_api_interaction_identifiers_body_type_7 import PatchApiInteractionIdentifiersBodyType7
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        "PatchApiInteractionIdentifiersBodyType0",
        "PatchApiInteractionIdentifiersBodyType1",
        "PatchApiInteractionIdentifiersBodyType2",
        "PatchApiInteractionIdentifiersBodyType3",
        "PatchApiInteractionIdentifiersBodyType4",
        "PatchApiInteractionIdentifiersBodyType5",
        "PatchApiInteractionIdentifiersBodyType6",
        "PatchApiInteractionIdentifiersBodyType7",
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/api/interaction/identifiers",
    }

    _body: Dict[str, Any]
    if isinstance(body, PatchApiInteractionIdentifiersBodyType0):
        _body = body.to_dict()
    elif isinstance(body, PatchApiInteractionIdentifiersBodyType1):
        _body = body.to_dict()
    elif isinstance(body, PatchApiInteractionIdentifiersBodyType2):
        _body = body.to_dict()
    elif isinstance(body, PatchApiInteractionIdentifiersBodyType3):
        _body = body.to_dict()
    elif isinstance(body, PatchApiInteractionIdentifiersBodyType4):
        _body = body.to_dict()
    elif isinstance(body, PatchApiInteractionIdentifiersBodyType5):
        _body = body.to_dict()
    elif isinstance(body, PatchApiInteractionIdentifiersBodyType6):
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
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
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
        "PatchApiInteractionIdentifiersBodyType0",
        "PatchApiInteractionIdentifiersBodyType1",
        "PatchApiInteractionIdentifiersBodyType2",
        "PatchApiInteractionIdentifiersBodyType3",
        "PatchApiInteractionIdentifiersBodyType4",
        "PatchApiInteractionIdentifiersBodyType5",
        "PatchApiInteractionIdentifiersBodyType6",
        "PatchApiInteractionIdentifiersBodyType7",
    ],
) -> Response[Any]:
    """
    Args:
        body (Union['PatchApiInteractionIdentifiersBodyType0',
            'PatchApiInteractionIdentifiersBodyType1', 'PatchApiInteractionIdentifiersBodyType2',
            'PatchApiInteractionIdentifiersBodyType3', 'PatchApiInteractionIdentifiersBodyType4',
            'PatchApiInteractionIdentifiersBodyType5', 'PatchApiInteractionIdentifiersBodyType6',
            'PatchApiInteractionIdentifiersBodyType7']):

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
        "PatchApiInteractionIdentifiersBodyType0",
        "PatchApiInteractionIdentifiersBodyType1",
        "PatchApiInteractionIdentifiersBodyType2",
        "PatchApiInteractionIdentifiersBodyType3",
        "PatchApiInteractionIdentifiersBodyType4",
        "PatchApiInteractionIdentifiersBodyType5",
        "PatchApiInteractionIdentifiersBodyType6",
        "PatchApiInteractionIdentifiersBodyType7",
    ],
) -> Response[Any]:
    """
    Args:
        body (Union['PatchApiInteractionIdentifiersBodyType0',
            'PatchApiInteractionIdentifiersBodyType1', 'PatchApiInteractionIdentifiersBodyType2',
            'PatchApiInteractionIdentifiersBodyType3', 'PatchApiInteractionIdentifiersBodyType4',
            'PatchApiInteractionIdentifiersBodyType5', 'PatchApiInteractionIdentifiersBodyType6',
            'PatchApiInteractionIdentifiersBodyType7']):

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
