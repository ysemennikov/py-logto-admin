from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_users_user_id_identities_body import PostApiUsersUserIdIdentitiesBody
from ...models.post_api_users_user_id_identities_response_200 import PostApiUsersUserIdIdentitiesResponse200
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: PostApiUsersUserIdIdentitiesBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/users/{user_id}/identities",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostApiUsersUserIdIdentitiesResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostApiUsersUserIdIdentitiesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, PostApiUsersUserIdIdentitiesResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiUsersUserIdIdentitiesBody,
) -> Response[Union[Any, PostApiUsersUserIdIdentitiesResponse200]]:
    """Link social identity to user

     Link authenticated user identity from a social platform to a Logto user.

    The usage of this API is usually coupled with `POST /connectors/:connectorId/authorization-uri`.
    With the help of these pair of APIs, you can implement a user profile page with the link social
    account feature in your application.

    Note: Currently due to technical limitations, this API does not support the following connectors
    that rely on Logto interaction session: `@logto/connector-apple`, `@logto/connector-saml`,
    `@logto/connector-oidc` and `@logto/connector-oauth`.

    Args:
        user_id (str):
        body (PostApiUsersUserIdIdentitiesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostApiUsersUserIdIdentitiesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiUsersUserIdIdentitiesBody,
) -> Optional[Union[Any, PostApiUsersUserIdIdentitiesResponse200]]:
    """Link social identity to user

     Link authenticated user identity from a social platform to a Logto user.

    The usage of this API is usually coupled with `POST /connectors/:connectorId/authorization-uri`.
    With the help of these pair of APIs, you can implement a user profile page with the link social
    account feature in your application.

    Note: Currently due to technical limitations, this API does not support the following connectors
    that rely on Logto interaction session: `@logto/connector-apple`, `@logto/connector-saml`,
    `@logto/connector-oidc` and `@logto/connector-oauth`.

    Args:
        user_id (str):
        body (PostApiUsersUserIdIdentitiesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostApiUsersUserIdIdentitiesResponse200]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiUsersUserIdIdentitiesBody,
) -> Response[Union[Any, PostApiUsersUserIdIdentitiesResponse200]]:
    """Link social identity to user

     Link authenticated user identity from a social platform to a Logto user.

    The usage of this API is usually coupled with `POST /connectors/:connectorId/authorization-uri`.
    With the help of these pair of APIs, you can implement a user profile page with the link social
    account feature in your application.

    Note: Currently due to technical limitations, this API does not support the following connectors
    that rely on Logto interaction session: `@logto/connector-apple`, `@logto/connector-saml`,
    `@logto/connector-oidc` and `@logto/connector-oauth`.

    Args:
        user_id (str):
        body (PostApiUsersUserIdIdentitiesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostApiUsersUserIdIdentitiesResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiUsersUserIdIdentitiesBody,
) -> Optional[Union[Any, PostApiUsersUserIdIdentitiesResponse200]]:
    """Link social identity to user

     Link authenticated user identity from a social platform to a Logto user.

    The usage of this API is usually coupled with `POST /connectors/:connectorId/authorization-uri`.
    With the help of these pair of APIs, you can implement a user profile page with the link social
    account feature in your application.

    Note: Currently due to technical limitations, this API does not support the following connectors
    that rely on Logto interaction session: `@logto/connector-apple`, `@logto/connector-saml`,
    `@logto/connector-oidc` and `@logto/connector-oauth`.

    Args:
        user_id (str):
        body (PostApiUsersUserIdIdentitiesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostApiUsersUserIdIdentitiesResponse200]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
