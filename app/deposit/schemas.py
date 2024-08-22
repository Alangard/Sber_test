from typing import Dict
from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field, RootModel, ValidationError, field_validator
from datetime import datetime

class SuccessDepositResponse(RootModel):
    root: Dict[str, float] = Field(
        ...,
        example={
            "31.01.2021": 10050.0,
            "28.02.2021": 10100.25,
            "31.03.2021": 10150.75
        }
    )

class ErrorDepositResponse(BaseModel):
    error: str = Field(
        ...,
        example='Field "date". Must be in the format dd.mm.YYYY'
    )


class DepositRequestData(BaseModel):
    date: str
    periods: int = Field(..., ge=1, le=60) 
    amount: int = Field(..., ge=10000, le=3000000)
    rate: float = Field(..., ge=1, le=8)

    model_config = ConfigDict(
        from_attributes=True, 
        json_schema_extra={
            "examples": [
                {
                    "date": datetime.now().strftime("%d.%m.%Y"),
                    "periods": 3,
                    "amount": 10000,
                    "rate": 6,
                }
            ]
    })

    
    @field_validator('date')
    def check_date_not_in_past(cls, date_str: str) -> str:
        try:
            datetime.strptime(date_str, "%d.%m.%Y")
        except ValueError:
            raise ValueError('Must be in the format dd.mm.YYYY')
        
        # Validator to verify that the date is not earlier than today
        # if input_date < datetime.now():
        #     raise ValueError('Date cannot be in the past.')

        return date_str