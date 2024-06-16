from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_api_sign_in_exp_body import PatchApiSignInExpBody
from ...models.patch_api_sign_in_exp_response_200 import PatchApiSignInExpResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PatchApiSignInExpBody,
    remove_unused_demo_social_connector: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["removeUnusedDemoSocialConnector"] = remove_unused_demo_social_connector

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/api/sign-in-exp",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PatchApiSignInExpResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PatchApiSignInExpResponse200.from_dict(response.json())

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
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PatchApiSignInExpResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiSignInExpBody,
    remove_unused_demo_social_connector: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PatchApiSignInExpResponse200]]:
    """Update default sign-in experience settings

     Update the default sign-in experience settings with the provided data.

    Args:
        remove_unused_demo_social_connector (Union[Unset, str]):
        body (PatchApiSignInExpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PatchApiSignInExpResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        remove_unused_demo_social_connector=remove_unused_demo_social_connector,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiSignInExpBody,
    remove_unused_demo_social_connector: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PatchApiSignInExpResponse200]]:
    """Update default sign-in experience settings

     Update the default sign-in experience settings with the provided data.

    Args:
        remove_unused_demo_social_connector (Union[Unset, str]):
        body (PatchApiSignInExpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PatchApiSignInExpResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
        remove_unused_demo_social_connector=remove_unused_demo_social_connector,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiSignInExpBody,
    remove_unused_demo_social_connector: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PatchApiSignInExpResponse200]]:
    """Update default sign-in experience settings

     Update the default sign-in experience settings with the provided data.

    Args:
        remove_unused_demo_social_connector (Union[Unset, str]):
        body (PatchApiSignInExpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PatchApiSignInExpResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        remove_unused_demo_social_connector=remove_unused_demo_social_connector,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchApiSignInExpBody,
    remove_unused_demo_social_connector: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PatchApiSignInExpResponse200]]:
    """Update default sign-in experience settings

     Update the default sign-in experience settings with the provided data.

    Args:
        remove_unused_demo_social_connector (Union[Unset, str]):
        body (PatchApiSignInExpBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PatchApiSignInExpResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            remove_unused_demo_social_connector=remove_unused_demo_social_connector,
        )
    ).parsed
