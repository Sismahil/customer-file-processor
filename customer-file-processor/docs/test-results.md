# Test Results

All three supplied CSV files were processed. Observed results matched the expected counts in the project brief.

| Input | Expected total | Expected valid | Expected invalid | Observed | Status |
|---|---:|---:|---:|---|---|
| `customers_clean.csv` | 10 | 10 | 0 | 10 / 10 / 0 | Passed |
| `customers_mixed.csv` | 12 | 7 | 5 | 12 / 7 / 5 | Passed |
| `customers_messy.csv` | 15 | 4 | 11 | 15 / 4 / 11 | Passed |

## Automatic trigger test

A new upload of `customers_clean.csv` to S3 `incoming/` automatically started the state machine. The execution input contained the expected bucket and key. The execution completed successfully with:

```json
{
  "status": "SUCCESS",
  "summary": {
    "fileName": "incoming/customers_clean.csv",
    "totalRows": 10,
    "validRows": 10,
    "invalidRows": 0
  }
}
```

## Screenshots to add

- S3 bucket layout (`incoming/`, `errors/`).
- Validator Lambda and test output.
- Step Functions workflow graph.
- Successful clean, mixed, and messy executions.
- DynamoDB valid records.
- S3 invalid-record objects and one JSON record with reasons.
- SNS summary emails.
- EventBridge rule and automatic-trigger execution.

Redact AWS account IDs, email addresses, execution IDs, and customer data before publishing publicly.
