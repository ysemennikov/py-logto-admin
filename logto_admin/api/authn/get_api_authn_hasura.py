from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_authn_hasura_response_200 import GetApiAuthnHasuraResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    resource: str,
    unauthorized_role: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["resource"] = resource

    params["unauthorizedRole"] = unauthorized_role

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/authn/hasura",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetApiAuthnHasuraResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetApiAuthnHasuraResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetApiAuthnHasuraResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    resource: str,
    unauthorized_role: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetApiAuthnHasuraResponse200]]:
    """Hasura auth hook endpoint

     The `HASURA_GRAPHQL_AUTH_HOOK` endpoint for Hasura auth. Use this endpoint to integrate Hasura's
    [webhook authentication flow](https://hasura.io/docs/latest/auth/authentication/webhook/).

    Args:
        resource (str):
        unauthorized_role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiAuthnHasuraResponse200]]
    """

    kwargs = _get_kwargs(
        resource=resource,
        unauthorized_role=unauthorized_role,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    resource: str,
    unauthorized_role: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetApiAuthnHasuraResponse200]]:
    """Hasura auth hook endpoint

     The `HASURA_GRAPHQL_AUTH_HOOK` endpoint for Hasura auth. Use this endpoint to integrate Hasura's
    [webhook authentication flow](https://hasura.io/docs/latest/auth/authentication/webhook/).

    Args:
        resource (str):
        unauthorized_role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiAuthnHasuraResponse200]
    """

    return sync_detailed(
        client=client,
        resource=resource,
        unauthorized_role=unauthorized_role,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    resource: str,
    unauthorized_role: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetApiAuthnHasuraResponse200]]:
    """Hasura auth hook endpoint

     The `HASURA_GRAPHQL_AUTH_HOOK` endpoint for Hasura auth. Use this endpoint to integrate Hasura's
    [webhook authentication flow](https://hasura.io/docs/latest/auth/authentication/webhook/).

    Args:
        resource (str):
        unauthorized_role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetApiAuthnHasuraResponse200]]
    """

    kwargs = _get_kwargs(
        resource=resource,
        unauthorized_role=unauthorized_role,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    resource: str,
    unauthorized_role: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetApiAuthnHasuraResponse200]]:
    """Hasura auth hook endpoint

     The `HASURA_GRAPHQL_AUTH_HOOK` endpoint for Hasura auth. Use this endpoint to integrate Hasura's
    [webhook authentication flow](https://hasura.io/docs/latest/auth/authentication/webhook/).

    Args:
        resource (str):
        unauthorized_role (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetApiAuthnHasuraResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            resource=resource,
            unauthorized_role=unauthorized_role,
        )
    ).parsed
