# GitHub Publishing Checklist

- [ ] Review README and resource inventory.
- [ ] Keep AWS account IDs and full ARNs out of public source files.
- [ ] Confirm no credentials, access keys, session tokens, private keys, or `.env` files are present.
- [ ] Confirm no real customer data or source CSV files are included.
- [ ] Review screenshots for account IDs, private email addresses, execution IDs, and customer information.
- [ ] Review the AI usage log for accuracy and team approval.
- [ ] Replace placeholders before reusing state-machine or IAM templates.
- [ ] Review IAM policies for least privilege.
- [ ] Decide whether the repository should be private or public.
- [ ] Add a license only if the team has chosen one.
