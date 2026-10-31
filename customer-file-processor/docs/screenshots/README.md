# Screenshot Evidence

Screenshots captured during the AWS implementation:

| File | Evidence |
|---|---|
| `01-validator-invalid-row-test.png` | Validator returns invalid status and multiple reasons |
| `02-step-functions-workflow-design.png` | Step Functions workflow design |
| `03-dynamodb-valid-customer-records.png` | Valid customer records in DynamoDB |
| `04-clean-file-map-results.png` | Clean CSV Map results |
| `05-mixed-file-invalid-records-in-s3.png` | Five invalid-row JSON objects in S3 |
| `06-clean-summary-email.png` | SNS summary: 10 total, 10 valid, 0 invalid |
| `07-mixed-summary-email.png` | SNS summary: 12 total, 7 valid, 5 invalid |
| `08-messy-summary-email.png` | SNS summary: 15 total, 4 valid, 11 invalid |
| `09-eventbridge-initial-prefix-filter.png` | Initial EventBridge pattern showing the bucket and `incoming/` prefix; the checked-in JSON adds the `.csv` suffix filter |
| `10-eventbridge-rule-enabled-sanitized.png` | EventBridge rule enabled; account number redacted |

Review all images before making the repository public.
