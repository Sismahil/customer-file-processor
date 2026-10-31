import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "lambda" / "validator" / "lambda_function.py"
spec = importlib.util.spec_from_file_location("validator", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def good_row():
    return {
        "customerId": "C001",
        "fullName": "Ada Obi",
        "email": "ada.obi@example.com",
        "age": "29",
        "country": "NG",
    }


def test_valid_customer():
    result = validator.lambda_handler(good_row(), None)
    assert result["valid"] is True
    assert result["reasons"] == []


def test_empty_customer_id():
    row = good_row()
    row["customerId"] = " "
    assert "customerId is empty" in validator.lambda_handler(row, None)["reasons"]


def test_empty_full_name():
    row = good_row()
    row["fullName"] = ""
    assert "fullName is empty" in validator.lambda_handler(row, None)["reasons"]


def test_invalid_email():
    row = good_row()
    row["email"] = "not-an-email"
    assert "invalid email" in validator.lambda_handler(row, None)["reasons"]


def test_age_whole_number_and_range():
    for age in ("17", "101", "29.5", "abc", ""):
        row = good_row()
        row["age"] = age
        assert validator.lambda_handler(row, None)["valid"] is False


def test_country_must_be_allowed_uppercase_code():
    row = good_row()
    row["country"] = "ng"
    assert "invalid country code" in validator.lambda_handler(row, None)["reasons"]


def test_collects_all_failure_reasons():
    row = {"customerId": "", "fullName": "", "email": "bad", "age": "17", "country": "XX"}
    result = validator.lambda_handler(row, None)
    assert result["valid"] is False
    assert len(result["reasons"]) == 5
