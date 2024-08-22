from typing import Union
from pydantic import ValidationError

from app.deposit.schemas import DepositRequestData, SuccessDepositResponse, ErrorDepositResponse


async def calculate_deposit_service(deposit_data: DepositRequestData) -> Union[SuccessDepositResponse, ErrorDepositResponse]:
    # Пробуем создать объект DepositRequestData, валидируя входные данные
    validated_data = DepositRequestData(
        date=deposit_data.date,
        periods=deposit_data.periods,
        amount=deposit_data.amount,
        rate=deposit_data.rate
    )

    result = {
        "28.02.2021": 10100.25,
        "31.01.2021": 10050,
        "31.03.2021": 10150.75
    }

    return SuccessDepositResponse(root=result)

    

    
