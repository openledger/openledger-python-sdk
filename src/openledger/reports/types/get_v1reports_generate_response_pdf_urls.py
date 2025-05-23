# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetV1ReportsGenerateResponsePdfUrls(UniversalBaseModel):
    profit_loss: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to profit & loss statement PDF
    """

    balance_sheet: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to balance sheet PDF
    """

    cash_flow: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to cash flow statement PDF
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
