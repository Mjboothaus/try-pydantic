# generated by datamodel-codegen:
#   filename:  cat.json
#   timestamp: 2022-12-28T09:04:17+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class Address(BaseModel):
    class Config:
        extra = Extra.forbid

    city: Optional[str] = Field(None, description="Cat's city")
    zip_code: Optional[str] = Field(None, description='Postal code')
    number: Optional[int] = Field(None, description='House number')


class CatRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: str = Field(..., description="Cat's name.")
    age: Optional[int] = Field(None, description="Cat's age, in cat years.")
    address: Optional[Address] = Field(
        None, description='Where does the cat live.')
