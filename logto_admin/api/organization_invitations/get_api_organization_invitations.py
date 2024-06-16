from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_organization_invitations_response_200_item import GetApiOrganizationInvitationsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    organization_id: Union[Unset, str] = UNSET,
    inviter_id: Union[Unset, str] = UNSET,
    invitee: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["organizationId"] = organization_id

    params["inviterId"] = inviter_id

    params["invitee"] = invitee

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/organization-invitations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["GetApiOrganizationInvitationsResponse200Item"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetApiOrganizationInvitationsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["GetApiOrganizationInvitationsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_id: Union[Unset, str] = UNSET,
    inviter_id: Union[Unset, str] = UNSET,
    invitee: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["GetApiOrganizationInvitationsResponse200Item"]]]:
    """Get organization invitations

     Get organization invitations.

    Args:
        organization_id (Union[Unset, str]):
        inviter_id (Union[Unset, str]):
        invitee (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetApiOrganizationInvitationsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        inviter_id=inviter_id,
        invitee=invitee,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_id: Union[Unset, str] = UNSET,
    inviter_id: Union[Unset, str] = UNSET,
    invitee: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["GetApiOrganizationInvitationsResponse200Item"]]]:
    """Get organization invitations

     Get organization invitations.

    Args:
        organization_id (Union[Unset, str]):
        inviter_id (Union[Unset, str]):
        invitee (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetApiOrganizationInvitationsResponse200Item']]
    """

    return sync_detailed(
        client=client,
        organization_id=organization_id,
        inviter_id=inviter_id,
        invitee=invitee,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_id: Union[Unset, str] = UNSET,
    inviter_id: Union[Unset, str] = UNSET,
    invitee: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["GetApiOrganizationInvitationsResponse200Item"]]]:
    """Get organization invitations

     Get organization invitations.

    Args:
        organization_id (Union[Unset, str]):
        inviter_id (Union[Unset, str]):
        invitee (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['GetApiOrganizationInvitationsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        inviter_id=inviter_id,
        invitee=invitee,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    organization_id: Union[Unset, str] = UNSET,
    inviter_id: Union[Unset, str] = UNSET,
    invitee: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["GetApiOrganizationInvitationsResponse200Item"]]]:
    """Get organization invitations

     Get organization invitations.

    Args:
        organization_id (Union[Unset, str]):
        inviter_id (Union[Unset, str]):
        invitee (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['GetApiOrganizationInvitationsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            client=client,
            organization_id=organization_id,
            inviter_id=inviter_id,
            invitee=invitee,
        )
    ).parsed
