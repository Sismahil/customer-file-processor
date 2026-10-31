import re

ALLOWED_COUNTRIES = {"NG", "GH", "KE", "ZA", "US", "GB", "CA"}
REQUIRED_FIELDS = ["customerId", "fullName", "email", "age", "country"]


def lambda_handler(event, context):
    row = event.get("row", event)
    if not isinstance(row, dict):
        return {"valid": False, "reasons": ["Customer row must be a JSON object"]}

    customer = {field: row.get(field, "") for field in REQUIRED_FIELDS}
    reasons = []

    if not str(customer["customerId"]).strip():
        reasons.append("customerId is empty")
    if not str(customer["fullName"]).strip():
        reasons.append("fullName is empty")

    email = str(customer["email"]).strip()
    if not re.fullmatch(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        reasons.append("invalid email")

    age = str(customer["age"]).strip()
    if not re.fullmatch(r"\d+", age):
        reasons.append("age must be a whole number")
    elif not 18 <= int(age) <= 100:
        reasons.append("age must be between 18 and 100")

    if str(customer["country"]) not in ALLOWED_COUNTRIES:
        reasons.append("invalid country code")

    return {**customer, "valid": len(reasons) == 0, "reasons": reasons}
