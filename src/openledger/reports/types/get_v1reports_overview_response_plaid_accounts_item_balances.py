# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetV1ReportsOverviewResponsePlaidAccountsItemBalances(UniversalBaseModel):
    available: typing.Optional[float] = None
    current: typing.Optional[float] = None
    iso_currency_code: typing.Optional[str] = None
    limit: typing.Optional[float] = None
    unofficial_currency_code: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
