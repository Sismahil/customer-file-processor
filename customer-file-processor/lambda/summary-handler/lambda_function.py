import os
import boto3

sns = boto3.client("sns")


def lambda_handler(event, context):
    file_name = event.get("fileName", "Unknown file")
    results = event.get("results", [])
    total = len(results)
    valid_count = sum(1 for row in results if row.get("valid") is True)
    invalid_count = total - valid_count

    summary = {
        "fileName": file_name,
        "totalRows": total,
        "validRows": valid_count,
        "invalidRows": invalid_count
    }

    message = f"""CUSTOMER FILE PROCESSING REPORT

File: {file_name}

Total customers: {total}
Valid customers: {valid_count}
Invalid customers: {invalid_count}

Processing completed successfully.
"""

    sns.publish(
        TopicArn=os.environ["SNS_TOPIC_ARN"],
        Subject="Customer File Processing Summary",
        Message=message
    )

    return {"status": "SUCCESS", "summary": summary}
