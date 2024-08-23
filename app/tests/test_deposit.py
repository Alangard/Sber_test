import pytest
from httpx import AsyncClient
from fastapi import status

from app.deposit.schemas import DepositRequestData, SuccessDepositResponse
from app.deposit.services import calculate_deposit_service


# Unit test
@pytest.mark.asyncio
async def test_calculate_deposit_service():
    data = DepositRequestData(date="31.01.2021", periods=3, amount=10000, rate=6)
    result = await calculate_deposit_service(data)

    expected_result = SuccessDepositResponse(root={
        "31.01.2021": 10050.0,
        "28.02.2021": 10100.25,
        "31.03.2021": 10150.75
    })
    assert result == expected_result

# Test API and schemas 
@pytest.mark.asyncio
async def test_deposit_calc_success(ac: AsyncClient):
    response = await ac.post("/deposit_calc", json={
        "date": "31.01.2021",
        "periods": 3,
        "amount": 10000,
        "rate": 6
    })
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "31.01.2021": 10050.0,
        "28.02.2021": 10100.25,
        "31.03.2021": 10150.75
    }


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "payload, error_field",
    [
        ({"date": "2021-01-31", "periods": 3, "amount": 10000, "rate": 6}, "date"),
        ({"date": "31.01.2021", "periods": 0, "amount": 10000, "rate": 6}, "periods"),
        ({"date": "31.01.2021", "periods": 3, "amount": 5000, "rate": 6}, "amount"),
        ({"date": "31.01.2021", "periods": 3, "amount": 10000, "rate": 10}, "rate"),
    ]
)
async def test_deposit_calc_invalid_cases(ac: AsyncClient, payload, error_field):
    response = await ac.post("/deposit_calc", json=payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert f"Field {error_field}" in response.json()["error"]