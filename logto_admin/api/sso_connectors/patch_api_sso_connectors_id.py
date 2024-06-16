from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_api_sso_connectors_id_body import PatchApiSsoConnectorsIdBody
from ...models.patch_api_sso_connectors_id_response_200 import PatchApiSsoConnectorsIdResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PatchApiSsoConnectorsIdBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/api/sso-connectors/{id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PatchApiSsoConnectorsIdResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PatchApiSsoConnectorsIdResponse200.from_dict(response.json())

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
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PatchApiSsoConnectorsIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiSsoConnectorsIdBody,
) -> Response[Union[Any, PatchApiSsoConnectorsIdResponse200]]:
    """Update SSO connector

     Update an SSO connector by ID. This method performs a partial update.

    Args:
        id (str):
        body (PatchApiSsoConnectorsIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PatchApiSsoConnectorsIdResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiSsoConnectorsIdBody,
) -> Optional[Union[Any, PatchApiSsoConnectorsIdResponse200]]:
    """Update SSO connector

     Update an SSO connector by ID. This method performs a partial update.

    Args:
        id (str):
        body (PatchApiSsoConnectorsIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PatchApiSsoConnectorsIdResponse200]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiSsoConnectorsIdBody,
) -> Response[Union[Any, PatchApiSsoConnectorsIdResponse200]]:
    """Update SSO connector

     Update an SSO connector by ID. This method performs a partial update.

    Args:
        id (str):
        body (PatchApiSsoConnectorsIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PatchApiSsoConnectorsIdResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiSsoConnectorsIdBody,
) -> Optional[Union[Any, PatchApiSsoConnectorsIdResponse200]]:
    """Update SSO connector

     Update an SSO connector by ID. This method performs a partial update.

    Args:
        id (str):
        body (PatchApiSsoConnectorsIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PatchApiSsoConnectorsIdResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
