# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostV1TransactionsSearchResponseTransactionsItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    amount: typing.Optional[float] = None
    description: typing.Optional[str] = None
    status: typing.Optional[str] = None
    timestamp: typing.Optional[dt.datetime] = None
    entity_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="entityId")] = None
    debit_account_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="debitAccountId")] = None
    credit_account_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="creditAccountId")] = None
    currency: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    created_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="createdAt")] = None
    updated_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
