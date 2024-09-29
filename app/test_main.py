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
    "mocked_today, expected",
    [
        (datetime.date(2022, 2, 2), ["duck"]),
        (datetime.date(2022, 1, 31), []),
        (datetime.date(2022, 2, 11), ["salmon", "chicken", "duck"])
    ]
)
@patch("app.main.datetime.date")
def test_outdated_products(
        mock_date: patch, mocked_today: datetime.date,
        expected: list[str], products: list[dict]) -> None:
    mock_date.today.return_value = mocked_today
    mock_date.side_effect = lambda *args, **kw: datetime.date(*args, **kw)
    assert outdated_products(products) == expected
