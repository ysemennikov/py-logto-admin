from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_users_user_id_mfa_verifications_body import PostApiUsersUserIdMfaVerificationsBody
from ...models.post_api_users_user_id_mfa_verifications_response_200_type_0 import (
    PostApiUsersUserIdMfaVerificationsResponse200Type0,
)
from ...models.post_api_users_user_id_mfa_verifications_response_200_type_1 import (
    PostApiUsersUserIdMfaVerificationsResponse200Type1,
)
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: PostApiUsersUserIdMfaVerificationsBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/users/{user_id}/mfa-verifications",
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
            "PostApiUsersUserIdMfaVerificationsResponse200Type0", "PostApiUsersUserIdMfaVerificationsResponse200Type1"
        ],
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "PostApiUsersUserIdMfaVerificationsResponse200Type0", "PostApiUsersUserIdMfaVerificationsResponse200Type1"
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = PostApiUsersUserIdMfaVerificationsResponse200Type0.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = PostApiUsersUserIdMfaVerificationsResponse200Type1.from_dict(data)

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
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
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
            "PostApiUsersUserIdMfaVerificationsResponse200Type0", "PostApiUsersUserIdMfaVerificationsResponse200Type1"
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
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiUsersUserIdMfaVerificationsBody,
) -> Response[
    Union[
        Any,
        Union[
            "PostApiUsersUserIdMfaVerificationsResponse200Type0", "PostApiUsersUserIdMfaVerificationsResponse200Type1"
        ],
    ]
]:
    """Create an MFA verification for a user

     Create a new MFA verification for a given user ID.

    Args:
        user_id (str):
        body (PostApiUsersUserIdMfaVerificationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['PostApiUsersUserIdMfaVerificationsResponse200Type0', 'PostApiUsersUserIdMfaVerificationsResponse200Type1']]]
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
    body: PostApiUsersUserIdMfaVerificationsBody,
) -> Optional[
    Union[
        Any,
        Union[
            "PostApiUsersUserIdMfaVerificationsResponse200Type0", "PostApiUsersUserIdMfaVerificationsResponse200Type1"
        ],
    ]
]:
    """Create an MFA verification for a user

     Create a new MFA verification for a given user ID.

    Args:
        user_id (str):
        body (PostApiUsersUserIdMfaVerificationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['PostApiUsersUserIdMfaVerificationsResponse200Type0', 'PostApiUsersUserIdMfaVerificationsResponse200Type1']]
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
    body: PostApiUsersUserIdMfaVerificationsBody,
) -> Response[
    Union[
        Any,
        Union[
            "PostApiUsersUserIdMfaVerificationsResponse200Type0", "PostApiUsersUserIdMfaVerificationsResponse200Type1"
        ],
    ]
]:
    """Create an MFA verification for a user

     Create a new MFA verification for a given user ID.

    Args:
        user_id (str):
        body (PostApiUsersUserIdMfaVerificationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['PostApiUsersUserIdMfaVerificationsResponse200Type0', 'PostApiUsersUserIdMfaVerificationsResponse200Type1']]]
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
    body: PostApiUsersUserIdMfaVerificationsBody,
) -> Optional[
    Union[
        Any,
        Union[
            "PostApiUsersUserIdMfaVerificationsResponse200Type0", "PostApiUsersUserIdMfaVerificationsResponse200Type1"
        ],
    ]
]:
    """Create an MFA verification for a user

     Create a new MFA verification for a given user ID.

    Args:
        user_id (str):
        body (PostApiUsersUserIdMfaVerificationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['PostApiUsersUserIdMfaVerificationsResponse200Type0', 'PostApiUsersUserIdMfaVerificationsResponse200Type1']]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
