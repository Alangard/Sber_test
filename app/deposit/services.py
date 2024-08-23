from typing import Union
from datetime import datetime
from dateutil.relativedelta import relativedelta
from app.deposit.schemas import (
    DepositRequestData,
    SuccessDepositResponse,
    ErrorDepositResponse,
)


async def calculate_deposit_service(
    deposit_data: DepositRequestData,
) -> Union[SuccessDepositResponse, ErrorDepositResponse]:

    result = {}
    current_amount = deposit_data.amount
    current_date = deposit_data.date

    for period in range(1, deposit_data.periods + 1):
        current_amount = current_amount * (1 + deposit_data.rate / 12 / 100)
        result[current_date] = round(current_amount, 2)
        start_date_datetime = datetime.strptime(deposit_data.date, "%d.%m.%Y")
        current_date = start_date_datetime + relativedelta(months=period)
        current_date = current_date.strftime("%d.%m.%Y")

    return SuccessDepositResponse(root=result)
