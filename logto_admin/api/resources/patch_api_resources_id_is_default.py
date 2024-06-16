from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_api_resources_id_is_default_body import PatchApiResourcesIdIsDefaultBody
from ...models.patch_api_resources_id_is_default_response_200 import PatchApiResourcesIdIsDefaultResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PatchApiResourcesIdIsDefaultBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/api/resources/{id}/is-default",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PatchApiResourcesIdIsDefaultResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PatchApiResourcesIdIsDefaultResponse200.from_dict(response.json())

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
) -> Response[Union[Any, PatchApiResourcesIdIsDefaultResponse200]]:
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
    body: PatchApiResourcesIdIsDefaultBody,
) -> Response[Union[Any, PatchApiResourcesIdIsDefaultResponse200]]:
    """Set API resource as default

     Set an API resource as the default resource for the current tenant.

    Each tenant can have only one default API resource. If an API resource is set as default, the
    previously set default API resource will be set as non-default. See [this
    section](https://docs.logto.io/docs/references/resources/#default-api) for more information.

    Args:
        id (str):
        body (PatchApiResourcesIdIsDefaultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PatchApiResourcesIdIsDefaultResponse200]]
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
    body: PatchApiResourcesIdIsDefaultBody,
) -> Optional[Union[Any, PatchApiResourcesIdIsDefaultResponse200]]:
    """Set API resource as default

     Set an API resource as the default resource for the current tenant.

    Each tenant can have only one default API resource. If an API resource is set as default, the
    previously set default API resource will be set as non-default. See [this
    section](https://docs.logto.io/docs/references/resources/#default-api) for more information.

    Args:
        id (str):
        body (PatchApiResourcesIdIsDefaultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PatchApiResourcesIdIsDefaultResponse200]
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
    body: PatchApiResourcesIdIsDefaultBody,
) -> Response[Union[Any, PatchApiResourcesIdIsDefaultResponse200]]:
    """Set API resource as default

     Set an API resource as the default resource for the current tenant.

    Each tenant can have only one default API resource. If an API resource is set as default, the
    previously set default API resource will be set as non-default. See [this
    section](https://docs.logto.io/docs/references/resources/#default-api) for more information.

    Args:
        id (str):
        body (PatchApiResourcesIdIsDefaultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PatchApiResourcesIdIsDefaultResponse200]]
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
    body: PatchApiResourcesIdIsDefaultBody,
) -> Optional[Union[Any, PatchApiResourcesIdIsDefaultResponse200]]:
    """Set API resource as default

     Set an API resource as the default resource for the current tenant.

    Each tenant can have only one default API resource. If an API resource is set as default, the
    previously set default API resource will be set as non-default. See [this
    section](https://docs.logto.io/docs/references/resources/#default-api) for more information.

    Args:
        id (str):
        body (PatchApiResourcesIdIsDefaultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PatchApiResourcesIdIsDefaultResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
