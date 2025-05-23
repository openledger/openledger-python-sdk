# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetV1ReportsGenerateResponseReportPeriod(UniversalBaseModel):
    month: typing.Optional[int] = pydantic.Field(default=None)
    """
    Month of the report period
    """

    year: typing.Optional[int] = pydantic.Field(default=None)
    """
    Year of the report period
    """

    start_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="startDate")] = (
        pydantic.Field(default=None)
    )
    """
    Start date of the report period
    """

    end_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="endDate")] = (
        pydantic.Field(default=None)
    )
    """
    End date of the report period
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
