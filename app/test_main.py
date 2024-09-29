import datetime
from app.main import outdated_products
import pytest
from unittest.mock import patch


@pytest.fixture
def products() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    ("mock_today", "expected"), [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 1, 31), []),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"])
    ]
)
def test_outdated_products(
        products: list, mock_today: datetime.date, expected: list
) -> None:
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = mock_today
        assert outdated_products(products) == expected
