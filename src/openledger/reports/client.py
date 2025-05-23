# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawReportsClient, RawReportsClient
from .types.get_v1reports_general_ledger_response import GetV1ReportsGeneralLedgerResponse
from .types.get_v1reports_generate_request_type import GetV1ReportsGenerateRequestType
from .types.get_v1reports_generate_response import GetV1ReportsGenerateResponse
from .types.get_v1reports_overview_request_interval import GetV1ReportsOverviewRequestInterval
from .types.get_v1reports_overview_request_status_filter import GetV1ReportsOverviewRequestStatusFilter
from .types.get_v1reports_overview_response import GetV1ReportsOverviewResponse


class ReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReportsClient
        """
        return self._raw_client

    def generate_financial_reports(
        self,
        *,
        entity_id: str,
        month: typing.Optional[int] = None,
        year: typing.Optional[int] = None,
        type: typing.Optional[GetV1ReportsGenerateRequestType] = None,
        ledger_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ReportsGenerateResponse:
        """
        Generates comprehensive financial statements for an entity, including balance sheet, income statement, and cash flow statement

        Parameters
        ----------
        entity_id : str
            The ID of the entity to generate reports for

        month : typing.Optional[int]
            Month number (1-12) for the report period

        year : typing.Optional[int]
            Year for the report period (e.g., 2024)

        type : typing.Optional[GetV1ReportsGenerateRequestType]
            Type of report to generate

        ledger_id : typing.Optional[str]
            Optional ledger ID (if not provided, will use entityId)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ReportsGenerateResponse
            Reports generated successfully

        Examples
        --------
        from openledger import OpenLedgerClient

        client = OpenLedgerClient(
            token="YOUR_TOKEN",
        )
        client.reports.generate_financial_reports(
            entity_id="entityId",
        )
        """
        _response = self._raw_client.generate_financial_reports(
            entity_id=entity_id, month=month, year=year, type=type, ledger_id=ledger_id, request_options=request_options
        )
        return _response.data

    def get_general_ledger_report(
        self,
        *,
        entity_id: str,
        month: typing.Optional[int] = None,
        year: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ReportsGeneralLedgerResponse:
        """
        Generates a detailed general ledger report with account balances and journal entries

        Parameters
        ----------
        entity_id : str
            The ID of the entity to generate the report for

        month : typing.Optional[int]
            Month number (1-12) for the report period

        year : typing.Optional[int]
            Year for the report period (e.g., 2024)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ReportsGeneralLedgerResponse
            General ledger report generated successfully

        Examples
        --------
        from openledger import OpenLedgerClient

        client = OpenLedgerClient(
            token="YOUR_TOKEN",
        )
        client.reports.get_general_ledger_report(
            entity_id="entityId",
        )
        """
        _response = self._raw_client.get_general_ledger_report(
            entity_id=entity_id, month=month, year=year, request_options=request_options
        )
        return _response.data

    def get_financial_overview(
        self,
        *,
        entity_id: str,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        interval: typing.Optional[GetV1ReportsOverviewRequestInterval] = None,
        status_filter: typing.Optional[GetV1ReportsOverviewRequestStatusFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ReportsOverviewResponse:
        """
        Retrieves a high-level overview of financial data including balances, trends, and key metrics

        Parameters
        ----------
        entity_id : str
            The ID of the entity to get the overview for

        start_date : typing.Optional[dt.datetime]
            Start date for the report period

        end_date : typing.Optional[dt.datetime]
            End date for the report period (defaults to current date)

        interval : typing.Optional[GetV1ReportsOverviewRequestInterval]
            Time interval for aggregating data

        status_filter : typing.Optional[GetV1ReportsOverviewRequestStatusFilter]
            Filter transactions by their status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ReportsOverviewResponse
            Financial overview retrieved successfully

        Examples
        --------
        from openledger import OpenLedgerClient

        client = OpenLedgerClient(
            token="YOUR_TOKEN",
        )
        client.reports.get_financial_overview(
            entity_id="entityId",
        )
        """
        _response = self._raw_client.get_financial_overview(
            entity_id=entity_id,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            status_filter=status_filter,
            request_options=request_options,
        )
        return _response.data


class AsyncReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReportsClient
        """
        return self._raw_client

    async def generate_financial_reports(
        self,
        *,
        entity_id: str,
        month: typing.Optional[int] = None,
        year: typing.Optional[int] = None,
        type: typing.Optional[GetV1ReportsGenerateRequestType] = None,
        ledger_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ReportsGenerateResponse:
        """
        Generates comprehensive financial statements for an entity, including balance sheet, income statement, and cash flow statement

        Parameters
        ----------
        entity_id : str
            The ID of the entity to generate reports for

        month : typing.Optional[int]
            Month number (1-12) for the report period

        year : typing.Optional[int]
            Year for the report period (e.g., 2024)

        type : typing.Optional[GetV1ReportsGenerateRequestType]
            Type of report to generate

        ledger_id : typing.Optional[str]
            Optional ledger ID (if not provided, will use entityId)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ReportsGenerateResponse
            Reports generated successfully

        Examples
        --------
        import asyncio

        from openledger import AsyncOpenLedgerClient

        client = AsyncOpenLedgerClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reports.generate_financial_reports(
                entity_id="entityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_financial_reports(
            entity_id=entity_id, month=month, year=year, type=type, ledger_id=ledger_id, request_options=request_options
        )
        return _response.data

    async def get_general_ledger_report(
        self,
        *,
        entity_id: str,
        month: typing.Optional[int] = None,
        year: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ReportsGeneralLedgerResponse:
        """
        Generates a detailed general ledger report with account balances and journal entries

        Parameters
        ----------
        entity_id : str
            The ID of the entity to generate the report for

        month : typing.Optional[int]
            Month number (1-12) for the report period

        year : typing.Optional[int]
            Year for the report period (e.g., 2024)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ReportsGeneralLedgerResponse
            General ledger report generated successfully

        Examples
        --------
        import asyncio

        from openledger import AsyncOpenLedgerClient

        client = AsyncOpenLedgerClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reports.get_general_ledger_report(
                entity_id="entityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_general_ledger_report(
            entity_id=entity_id, month=month, year=year, request_options=request_options
        )
        return _response.data

    async def get_financial_overview(
        self,
        *,
        entity_id: str,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        interval: typing.Optional[GetV1ReportsOverviewRequestInterval] = None,
        status_filter: typing.Optional[GetV1ReportsOverviewRequestStatusFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetV1ReportsOverviewResponse:
        """
        Retrieves a high-level overview of financial data including balances, trends, and key metrics

        Parameters
        ----------
        entity_id : str
            The ID of the entity to get the overview for

        start_date : typing.Optional[dt.datetime]
            Start date for the report period

        end_date : typing.Optional[dt.datetime]
            End date for the report period (defaults to current date)

        interval : typing.Optional[GetV1ReportsOverviewRequestInterval]
            Time interval for aggregating data

        status_filter : typing.Optional[GetV1ReportsOverviewRequestStatusFilter]
            Filter transactions by their status

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1ReportsOverviewResponse
            Financial overview retrieved successfully

        Examples
        --------
        import asyncio

        from openledger import AsyncOpenLedgerClient

        client = AsyncOpenLedgerClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.reports.get_financial_overview(
                entity_id="entityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_financial_overview(
            entity_id=entity_id,
            start_date=start_date,
            end_date=end_date,
            interval=interval,
            status_filter=status_filter,
            request_options=request_options,
        )
        return _response.data
