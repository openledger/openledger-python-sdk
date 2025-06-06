# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..types.bank_account import BankAccount
from .types.get_v1banks_create_link_response import GetV1BanksCreateLinkResponse
from .types.get_v1banks_sync_status_response import GetV1BanksSyncStatusResponse
from .types.post_v1banks_sync_response import PostV1BanksSyncResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawBanksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_a_bank_link(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetV1BanksCreateLinkResponse]:
        """
        Creates a new Plaid link token for connecting a bank account

        Parameters
        ----------
        entity_id : str
            The ID of the entity to create the link token for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetV1BanksCreateLinkResponse]
            Bank link created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/banks/create-link",
            method="GET",
            params={
                "entityId": entity_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1BanksCreateLinkResponse,
                    parse_obj_as(
                        type_=GetV1BanksCreateLinkResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_bank_accounts_for_an_entity(
        self, *, entity_id: str, public_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[BankAccount]]:
        """
        Adds bank accounts to an entity using a Plaid public token obtained from the Plaid Link interface

        Parameters
        ----------
        entity_id : str
            The ID of the entity to add bank accounts for

        public_token : str
            The public token obtained from Plaid Link

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[BankAccount]]
            Bank accounts added successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/banks/accounts",
            method="PUT",
            params={
                "entityId": entity_id,
                "public_token": public_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BankAccount],
                    parse_obj_as(
                        type_=typing.List[BankAccount],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def sync_plaid_accounts_for_an_entity(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV1BanksSyncResponse]:
        """
        Synchronizes transaction data for all connected Plaid accounts belonging to an entity

        Parameters
        ----------
        entity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV1BanksSyncResponse]
            Accounts synced successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/banks/sync",
            method="POST",
            json={
                "entityId": entity_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV1BanksSyncResponse,
                    parse_obj_as(
                        type_=PostV1BanksSyncResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def check_sync_status_of_bank_accounts(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetV1BanksSyncStatusResponse]:
        """
        Check the synchronization status of bank accounts for an entity

        Parameters
        ----------
        entity_id : str
            The ID of the entity to check sync status for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetV1BanksSyncStatusResponse]
            Sync status retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/banks/sync-status",
            method="GET",
            params={
                "entityId": entity_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1BanksSyncStatusResponse,
                    parse_obj_as(
                        type_=GetV1BanksSyncStatusResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawBanksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_a_bank_link(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetV1BanksCreateLinkResponse]:
        """
        Creates a new Plaid link token for connecting a bank account

        Parameters
        ----------
        entity_id : str
            The ID of the entity to create the link token for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetV1BanksCreateLinkResponse]
            Bank link created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/banks/create-link",
            method="GET",
            params={
                "entityId": entity_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1BanksCreateLinkResponse,
                    parse_obj_as(
                        type_=GetV1BanksCreateLinkResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_bank_accounts_for_an_entity(
        self, *, entity_id: str, public_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[BankAccount]]:
        """
        Adds bank accounts to an entity using a Plaid public token obtained from the Plaid Link interface

        Parameters
        ----------
        entity_id : str
            The ID of the entity to add bank accounts for

        public_token : str
            The public token obtained from Plaid Link

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[BankAccount]]
            Bank accounts added successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/banks/accounts",
            method="PUT",
            params={
                "entityId": entity_id,
                "public_token": public_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BankAccount],
                    parse_obj_as(
                        type_=typing.List[BankAccount],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def sync_plaid_accounts_for_an_entity(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV1BanksSyncResponse]:
        """
        Synchronizes transaction data for all connected Plaid accounts belonging to an entity

        Parameters
        ----------
        entity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV1BanksSyncResponse]
            Accounts synced successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/banks/sync",
            method="POST",
            json={
                "entityId": entity_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostV1BanksSyncResponse,
                    parse_obj_as(
                        type_=PostV1BanksSyncResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def check_sync_status_of_bank_accounts(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetV1BanksSyncStatusResponse]:
        """
        Check the synchronization status of bank accounts for an entity

        Parameters
        ----------
        entity_id : str
            The ID of the entity to check sync status for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetV1BanksSyncStatusResponse]
            Sync status retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/banks/sync-status",
            method="GET",
            params={
                "entityId": entity_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV1BanksSyncStatusResponse,
                    parse_obj_as(
                        type_=GetV1BanksSyncStatusResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
