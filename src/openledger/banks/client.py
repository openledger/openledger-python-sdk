# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBanksClient, RawBanksClient
from .types.get_v1banks_create_link_response import GetV1BanksCreateLinkResponse
from .types.put_v1banks_accounts_response import PutV1BanksAccountsResponse


class BanksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBanksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBanksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBanksClient
        """
        return self._raw_client

    def create_a_bank_link(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1BanksCreateLinkResponse:
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
        GetV1BanksCreateLinkResponse
            Bank link created successfully

        Examples
        --------
        from openledger import OpenLedgerClient

        client = OpenLedgerClient(
            token="YOUR_TOKEN",
        )
        client.banks.create_a_bank_link(
            entity_id="ent_123456",
        )
        """
        _response = self._raw_client.create_a_bank_link(entity_id=entity_id, request_options=request_options)
        return _response.data

    def add_bank_accounts(
        self, *, entity_id: str, public_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PutV1BanksAccountsResponse:
        """
        Adds new bank accounts using a Plaid public token

        Parameters
        ----------
        entity_id : str
            The ID of the entity to add the bank accounts for

        public_token : str
            The Plaid public token received from the Plaid Link onSuccess callback

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutV1BanksAccountsResponse
            Bank accounts added successfully

        Examples
        --------
        from openledger import OpenLedgerClient

        client = OpenLedgerClient(
            token="YOUR_TOKEN",
        )
        client.banks.add_bank_accounts(
            entity_id="ent_123456",
            public_token="public-sandbox-123456-abcdef",
        )
        """
        _response = self._raw_client.add_bank_accounts(
            entity_id=entity_id, public_token=public_token, request_options=request_options
        )
        return _response.data


class AsyncBanksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBanksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBanksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBanksClient
        """
        return self._raw_client

    async def create_a_bank_link(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1BanksCreateLinkResponse:
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
        GetV1BanksCreateLinkResponse
            Bank link created successfully

        Examples
        --------
        import asyncio

        from openledger import AsyncOpenLedgerClient

        client = AsyncOpenLedgerClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.banks.create_a_bank_link(
                entity_id="ent_123456",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_bank_link(entity_id=entity_id, request_options=request_options)
        return _response.data

    async def add_bank_accounts(
        self, *, entity_id: str, public_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PutV1BanksAccountsResponse:
        """
        Adds new bank accounts using a Plaid public token

        Parameters
        ----------
        entity_id : str
            The ID of the entity to add the bank accounts for

        public_token : str
            The Plaid public token received from the Plaid Link onSuccess callback

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutV1BanksAccountsResponse
            Bank accounts added successfully

        Examples
        --------
        import asyncio

        from openledger import AsyncOpenLedgerClient

        client = AsyncOpenLedgerClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.banks.add_bank_accounts(
                entity_id="ent_123456",
                public_token="public-sandbox-123456-abcdef",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_bank_accounts(
            entity_id=entity_id, public_token=public_token, request_options=request_options
        )
        return _response.data
