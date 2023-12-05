# sec-parser-test-data

This repository complements the [sec-parser](https://github.com/alphanome-ai/sec-parser) project by storing raw SEC EDGAR documents for various quality assurance tasks. These tasks include end-to-end testing and evaluation tests. For guidelines on contributing, please consult the [Contribution Guide](https://github.com/alphanome-ai/sec-parser/blob/main/CONTRIBUTING.md).

## How This Repository Helps

- **End-to-End Testing**: Maintains manually reviewed snapshots of parser outputs. These snapshots serve as a benchmark for validating the latest outputs from the parser, ensuring it accurately processes a selected subset of documents.
- **Generalization Testing**: Keeps a wide range of SEC documents on hand. Unlike tests that only use a few hand-picked documents, it's aimed to allow testing the parser on a much larger and diverse set of reports. By doing so, it checks if the parser can handle different types of documents effectively. For extra trust in the test results, they may also be compared to data from third-party services.

Keeping this data separate ensures a clean and manageable main code repository, aiding in maintenance and efficiency.

## How To Add New Items

### Option A. Auto-download filings

1. Add new lines in `00_report-list.csv`, then run `00_download-reports-from-report-list.ipynb`. 
    - The first CSV column values (`comment`) are ignored.
    - The `query` column value has to be in the format `AAPL` to download the latest 10-Q report (will work only if the folder doesn't exist), or `AAPL/0000320193-23-000077` for a specific report.
2. Add the new reports to the `.yaml` files in the `sec-parser` repository (e.g. [`e2e_test_data.yaml`](https://github.com/alphanome-ai/sec-parser/blob/c101a1a6b0ccd6c38efa7ad24de497ef3d2a0afb/tests/e2e/e2e_test_data.yaml), to include them in the tests.

### Option B. Copy paste filings

1. Download the filings yourself and copy-paste it to the repo, while keeping the correct format.

## Contributing

When submitting changes, please include the git hash of the `sec-parser` repository in your commit message or pull request for version tracking.

## Feedback

For questions or discussions, use [Discussions](https://github.com/orgs/alphanome-ai/discussions). For issues, [open an issue](https://github.com/alphanome-ai/sec-parser/issues).
