# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIntegrationsClient, RawIntegrationsClient
from .types.get_v1integrations_status_response import GetV1IntegrationsStatusResponse
from .types.post_v1integrations_connect_response import PostV1IntegrationsConnectResponse
from .types.post_v1integrations_disconnect_response import PostV1IntegrationsDisconnectResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class IntegrationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIntegrationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIntegrationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIntegrationsClient
        """
        return self._raw_client

    def get_integration_status(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1IntegrationsStatusResponse:
        """
        Retrieves the status of all integrations for an entity

        Parameters
        ----------
        entity_id : str
            The ID of the entity to get integration status for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1IntegrationsStatusResponse
            Integration status retrieved successfully

        Examples
        --------
        from openledger import OpenLedgerClient

        client = OpenLedgerClient(
            token="YOUR_TOKEN",
        )
        client.integrations.get_integration_status(
            entity_id="entityId",
        )
        """
        _response = self._raw_client.get_integration_status(entity_id=entity_id, request_options=request_options)
        return _response.data

    def connect_an_integration(
        self,
        *,
        provider: str,
        entity_id: str,
        connection_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1IntegrationsConnectResponse:
        """
        Initiates the connection process for a third-party integration using the Unified API

        Parameters
        ----------
        provider : str
            The integration provider (e.g., quickbooks, xero)

        entity_id : str
            The ID of the entity to connect the integration for

        connection_type : typing.Optional[str]
            The type of connection to establish (used as scope in Unified API)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1IntegrationsConnectResponse
            Integration connection initiated successfully

        Examples
        --------
        from openledger import OpenLedgerClient

        client = OpenLedgerClient(
            token="YOUR_TOKEN",
        )
        client.integrations.connect_an_integration(
            provider="quickbooks",
            entity_id="entityId",
        )
        """
        _response = self._raw_client.connect_an_integration(
            provider=provider, entity_id=entity_id, connection_type=connection_type, request_options=request_options
        )
        return _response.data

    def disconnect_an_integration(
        self, *, entity_id: str, integration_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1IntegrationsDisconnectResponse:
        """
        Disconnects an existing integration for an entity by removing it from the Unified Connections table

        Parameters
        ----------
        entity_id : str
            The ID of the entity that owns the integration

        integration_type : str
            The type of integration to disconnect (must match connectionType in Unified Connections)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1IntegrationsDisconnectResponse
            Integration disconnected successfully

        Examples
        --------
        from openledger import OpenLedgerClient

        client = OpenLedgerClient(
            token="YOUR_TOKEN",
        )
        client.integrations.disconnect_an_integration(
            entity_id="entityId",
            integration_type="integrationType",
        )
        """
        _response = self._raw_client.disconnect_an_integration(
            entity_id=entity_id, integration_type=integration_type, request_options=request_options
        )
        return _response.data


class AsyncIntegrationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIntegrationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIntegrationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIntegrationsClient
        """
        return self._raw_client

    async def get_integration_status(
        self, *, entity_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1IntegrationsStatusResponse:
        """
        Retrieves the status of all integrations for an entity

        Parameters
        ----------
        entity_id : str
            The ID of the entity to get integration status for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1IntegrationsStatusResponse
            Integration status retrieved successfully

        Examples
        --------
        import asyncio

        from openledger import AsyncOpenLedgerClient

        client = AsyncOpenLedgerClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.integrations.get_integration_status(
                entity_id="entityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_integration_status(entity_id=entity_id, request_options=request_options)
        return _response.data

    async def connect_an_integration(
        self,
        *,
        provider: str,
        entity_id: str,
        connection_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1IntegrationsConnectResponse:
        """
        Initiates the connection process for a third-party integration using the Unified API

        Parameters
        ----------
        provider : str
            The integration provider (e.g., quickbooks, xero)

        entity_id : str
            The ID of the entity to connect the integration for

        connection_type : typing.Optional[str]
            The type of connection to establish (used as scope in Unified API)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1IntegrationsConnectResponse
            Integration connection initiated successfully

        Examples
        --------
        import asyncio

        from openledger import AsyncOpenLedgerClient

        client = AsyncOpenLedgerClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.integrations.connect_an_integration(
                provider="quickbooks",
                entity_id="entityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connect_an_integration(
            provider=provider, entity_id=entity_id, connection_type=connection_type, request_options=request_options
        )
        return _response.data

    async def disconnect_an_integration(
        self, *, entity_id: str, integration_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PostV1IntegrationsDisconnectResponse:
        """
        Disconnects an existing integration for an entity by removing it from the Unified Connections table

        Parameters
        ----------
        entity_id : str
            The ID of the entity that owns the integration

        integration_type : str
            The type of integration to disconnect (must match connectionType in Unified Connections)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1IntegrationsDisconnectResponse
            Integration disconnected successfully

        Examples
        --------
        import asyncio

        from openledger import AsyncOpenLedgerClient

        client = AsyncOpenLedgerClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.integrations.disconnect_an_integration(
                entity_id="entityId",
                integration_type="integrationType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disconnect_an_integration(
            entity_id=entity_id, integration_type=integration_type, request_options=request_options
        )
        return _response.data
