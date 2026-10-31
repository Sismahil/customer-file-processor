# AWS Resource Inventory

The completed project used these resource names in `us-east-1`:

| Service | Resource | Purpose |
|---|---|---|
| S3 | `teamfalcon-customer-files-uniqueid` | CSV input and invalid-row JSON |
| S3 prefixes | `incoming/`, `errors/` | Input and rejected records |
| DynamoDB | `teamfalcon-customers` | Valid customer records |
| DynamoDB key | `customerId` (String) | Partition key |
| Lambda | `teamfalcon-customer-validator` | Validate one row |
| Lambda | `teamfalcon-customer-summary-handler` | Count results and publish summary |
| Step Functions | `teamfalcon-customer-processor` | Standard workflow with Distributed Map |
| SNS | `teamfalcon-customer-summary` | Summary email topic |
| EventBridge | `teamfalcon-customer-upload-trigger` | Trigger workflow for CSV uploads |

This inventory intentionally excludes account IDs, full ARNs, email addresses, and credentials.
