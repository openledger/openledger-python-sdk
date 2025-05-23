# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_v1transactions_by_month_response_item_plaid_account_breakdown_item import (
    GetV1TransactionsByMonthResponseItemPlaidAccountBreakdownItem,
)


class GetV1TransactionsByMonthResponseItem(UniversalBaseModel):
    year: typing.Optional[int] = pydantic.Field(default=None)
    """
    The year of the transactions
    """

    month: typing.Optional[int] = pydantic.Field(default=None)
    """
    The month of the transactions (1-12)
    """

    delta: typing.Optional[float] = pydantic.Field(default=None)
    """
    The net change in balance for the month
    """

    plaid_account_breakdown: typing_extensions.Annotated[
        typing.Optional[typing.List[GetV1TransactionsByMonthResponseItemPlaidAccountBreakdownItem]],
        FieldMetadata(alias="plaidAccountBreakdown"),
    ] = pydantic.Field(default=None)
    """
    Breakdown of transactions by Plaid account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
