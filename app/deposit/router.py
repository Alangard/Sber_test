from typing import Union
from fastapi import APIRouter

from app.deposit.schemas import DepositRequestData, SuccessDepositResponse, ErrorDepositResponse
from app.deposit.services import calculate_deposit_service

router = APIRouter()


@router.post(
        "/deposit_calc", 
        response_model=Union[SuccessDepositResponse, ErrorDepositResponse],
        responses={
            200: {
                "description": "Successful response",
                "model": SuccessDepositResponse,
            },
            422: {
                "description": "Validation error response",
                "model": ErrorDepositResponse,
            },
        },
)
async def deposit_calc(deposit_data: DepositRequestData):
    response = await calculate_deposit_service(deposit_data)
    return response
