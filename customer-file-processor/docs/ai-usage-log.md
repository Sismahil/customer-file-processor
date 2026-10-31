# AI Usage Log

The project brief requires at least three entries, including one example where an initial answer was incomplete or did not work. These entries summarize actual troubleshooting from the build; review them as a team and edit if needed to reflect your own record.

## Entry 1 — EventBridge target input

**Problem we had:** The EventBridge target initially passed the entire matched S3 event, while the Step Functions state machine expected only `bucket` and `key`.

**Tool and prompt/search used:** ChatGPT assistance while configuring the EventBridge target input.

**What it gave us:** An input transformer using `$.detail.bucket.name` and `$.detail.object.key`, with a JSON template containing those two fields.

**Did it work? If not, what was wrong:** The original matched-event input did not have the shape expected by the state machine.

**How we fixed it:** Changed the target to an input transformer and verified that the execution input contained the bucket and `incoming/<filename>.csv`.

## Entry 2 — Missing S3 ListBucket permission

**Problem we had:** The Distributed Map ItemReader failed with `States.ItemReaderFailed` and AccessDenied for `s3:ListBucket`.

**Tool and prompt/search used:** ChatGPT assistance with the exact AWS error and S3 bucket/prefix configuration.

**What it gave us:** A policy granting `s3:ListBucket` on the project bucket, restricted to the `incoming/` prefix.

**Did it work? If not, what was wrong:** Earlier object-read permissions did not include the bucket-listing permission required by the CSV ItemReader.

**How we fixed it:** Added the scoped permission to the Step Functions execution role and reran the workflow. The messy-file test completed with 15 total, 4 valid, and 11 invalid.

## Entry 3 — EventBridge file-type filter

**Problem we had:** The initial EventBridge pattern matched objects under `incoming/` but did not limit matches to CSV files.

**Tool and prompt/search used:** ChatGPT assistance reviewing the event pattern against the requirement to trigger only for CSV uploads.

**What it gave us:** A revised pattern using the object-key wildcard `incoming/*.csv`.

**Did it work? If not, what was wrong:** The initial prefix-only pattern was too broad and could match non-CSV objects in `incoming/`.

**How we fixed it:** Updated the pattern to match the bucket and `incoming/*.csv`, then verified that uploading a CSV automatically started the state machine.

## Verification note

AI-generated code, policies, and console guidance were checked against AWS execution results and the three supplied test files. The team is responsible for reviewing the implementation and confirming this log accurately represents its work.
