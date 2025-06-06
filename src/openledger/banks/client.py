# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bank_account import BankAccount
from .raw_client import AsyncRawBanksClient, RawBanksClient
from .types.get_v1banks_create_link_response import GetV1BanksCreateLinkResponse
from .types.get_v1banks_sync_status_response import GetV1BanksSyncStatusResponse
from .types.post_v1banks_sync_response import PostV1BanksSyncResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


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

    def add_bank_accounts_for_an_entity(
        self, *, entity_id: str, public_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BankAccount]:
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
        typing.List[BankAccount]
            Bank accounts added successfully

        Examples
        --------
        from openledger import OpenLedgerClient

        client = OpenLedgerClient(
            token="YOUR_TOKEN",
        )
        client.banks.add_bank_accounts_for_an_entity(
            entity_id="entityId",
            public_token="public_token",
        )
        """
        _response = self._raw_client.add_bank_accounts_for_an_entity(
            entity_id=entity_id, public_token=public_token, request_options=request_options
        )
        return _response.data

    def sync_plaid_accounts_for_an_entity(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1BanksSyncResponse:
        """
        Synchronizes transaction data for all connected Plaid accounts belonging to an entity

        Parameters
        ----------
        entity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1BanksSyncResponse
            Accounts synced successfully

        Examples
        --------
        from openledger import OpenLedgerClient

        client = OpenLedgerClient(
            token="YOUR_TOKEN",
        )
        client.banks.sync_plaid_accounts_for_an_entity(
            entity_id="entityId",
        )
        """
        _response = self._raw_client.sync_plaid_accounts_for_an_entity(
            entity_id=entity_id, request_options=request_options
        )
        return _response.data

    def check_sync_status_of_bank_accounts(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1BanksSyncStatusResponse:
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
        GetV1BanksSyncStatusResponse
            Sync status retrieved successfully

        Examples
        --------
        from openledger import OpenLedgerClient

        client = OpenLedgerClient(
            token="YOUR_TOKEN",
        )
        client.banks.check_sync_status_of_bank_accounts(
            entity_id="entityId",
        )
        """
        _response = self._raw_client.check_sync_status_of_bank_accounts(
            entity_id=entity_id, request_options=request_options
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

    async def add_bank_accounts_for_an_entity(
        self, *, entity_id: str, public_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BankAccount]:
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
        typing.List[BankAccount]
            Bank accounts added successfully

        Examples
        --------
        import asyncio

        from openledger import AsyncOpenLedgerClient

        client = AsyncOpenLedgerClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.banks.add_bank_accounts_for_an_entity(
                entity_id="entityId",
                public_token="public_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_bank_accounts_for_an_entity(
            entity_id=entity_id, public_token=public_token, request_options=request_options
        )
        return _response.data

    async def sync_plaid_accounts_for_an_entity(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1BanksSyncResponse:
        """
        Synchronizes transaction data for all connected Plaid accounts belonging to an entity

        Parameters
        ----------
        entity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1BanksSyncResponse
            Accounts synced successfully

        Examples
        --------
        import asyncio

        from openledger import AsyncOpenLedgerClient

        client = AsyncOpenLedgerClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.banks.sync_plaid_accounts_for_an_entity(
                entity_id="entityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sync_plaid_accounts_for_an_entity(
            entity_id=entity_id, request_options=request_options
        )
        return _response.data

    async def check_sync_status_of_bank_accounts(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1BanksSyncStatusResponse:
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
        GetV1BanksSyncStatusResponse
            Sync status retrieved successfully

        Examples
        --------
        import asyncio

        from openledger import AsyncOpenLedgerClient

        client = AsyncOpenLedgerClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.banks.check_sync_status_of_bank_accounts(
                entity_id="entityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_sync_status_of_bank_accounts(
            entity_id=entity_id, request_options=request_options
        )
        return _response.data
