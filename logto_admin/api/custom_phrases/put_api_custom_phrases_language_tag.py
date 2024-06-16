from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_api_custom_phrases_language_tag_language_tag import PutApiCustomPhrasesLanguageTagLanguageTag
from ...models.translation_object import TranslationObject
from ...types import Response


def _get_kwargs(
    language_tag: PutApiCustomPhrasesLanguageTagLanguageTag,
    *,
    body: TranslationObject,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/custom-phrases/{language_tag}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.CREATED:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
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
    language_tag: PutApiCustomPhrasesLanguageTagLanguageTag,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TranslationObject,
) -> Response[Any]:
    """Upsert custom phrases

     Upsert custom phrases for the specified language tag. Upsert means that if the custom phrases
    already exist, they will be updated. Otherwise, they will be created.

    Args:
        language_tag (PutApiCustomPhrasesLanguageTagLanguageTag):
        body (TranslationObject):  Example: {'input': {'username': 'Username', 'password':
            'Password'}, 'action': {'sign_in': 'Sign In', 'continue': 'Continue'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        language_tag=language_tag,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    language_tag: PutApiCustomPhrasesLanguageTagLanguageTag,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TranslationObject,
) -> Response[Any]:
    """Upsert custom phrases

     Upsert custom phrases for the specified language tag. Upsert means that if the custom phrases
    already exist, they will be updated. Otherwise, they will be created.

    Args:
        language_tag (PutApiCustomPhrasesLanguageTagLanguageTag):
        body (TranslationObject):  Example: {'input': {'username': 'Username', 'password':
            'Password'}, 'action': {'sign_in': 'Sign In', 'continue': 'Continue'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        language_tag=language_tag,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)