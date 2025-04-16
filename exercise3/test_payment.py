import pytest
from unittest import mock
from payment import process_payment, InvalidPaymentDetails, PaymentGatewayError

def test_invalid_user_id():
    with pytest.raises(InvalidPaymentDetails, match="Invalid user ID or amount."):
        process_payment(user_id=None, amount=100)

def test_invalid_amount():
    with pytest.raises(InvalidPaymentDetails, match="Invalid user ID or amount."):
        process_payment(user_id="user123", amount=0)

def test_unsupported_currency():
    with pytest.raises(InvalidPaymentDetails, match="Unsupported currency: BRL"):
        process_payment(user_id="user123", amount=100, currency="BRL")

def test_successful_payment():
    with mock.patch("random.random", return_value=0.5), \
         mock.patch("random.randint", return_value=123456):
        result = process_payment(user_id="user123", amount=100, currency="USD")
        assert result["status"] == "success"
        assert result["transaction_id"] == "TXN-123456"
        assert result["amount_charged"] == 100.0
        assert result["currency"] == "USD"

def test_currency_conversion_eur():
    with mock.patch("random.random", return_value=0.5), \
         mock.patch("random.randint", return_value=654321):
        result = process_payment(user_id="user123", amount=100, currency="EUR")
        assert result["amount_charged"] == 90.0

def test_currency_conversion_jpy():
    with mock.patch("random.random", return_value=0.5), \
         mock.patch("random.randint", return_value=111111):
        result = process_payment(user_id="user123", amount=1, currency="JPY")
        assert result["amount_charged"] == 110.0

def test_retry_and_success_on_second_attempt():
    # Simula falha na primeira tentativa e sucesso na segunda
    with mock.patch("random.random", side_effect=[0.1, 0.5]), \
         mock.patch("random.randint", return_value=222222):
        result = process_payment(user_id="user123", amount=50)
        assert result["status"] == "success"
        assert result["transaction_id"] == "TXN-222222"

def test_retry_exceeds_and_fails():
    # Força sempre falha
    with mock.patch("random.random", side_effect=[0.1, 0.1, 0.1]):
        with pytest.raises(PaymentGatewayError, match="Payment failed after 3 attempts."):
            process_payment(user_id="user123", amount=100, retries=3)
