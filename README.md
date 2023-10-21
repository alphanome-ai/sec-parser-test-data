# sec-parser-validation-data

This repository complements the [sec-parser](https://github.com/alphanome-ai/sec-parser) project by storing raw SEC EDGAR documents for various quality assurance tasks. These tasks include end-to-end testing and evaluation tests. For guidelines on contributing, please consult the [Contribution Guide](https://github.com/alphanome-ai/sec-parser/blob/main/CONTRIBUTING.md).

## How This Repository Helps

- **End-to-End Testing**: Maintains manually reviewed snapshots of parser outputs. These snapshots serve as a benchmark for validating the latest outputs from the parser, ensuring it accurately processes a selected subset of documents.
- **Generalization Testing**: Keeps a wide range of SEC documents on hand. Unlike tests that only use a few hand-picked documents, it's aimed to allow testing the parser on a much larger and diverse set of reports. By doing so, it checks if the parser can handle different types of documents effectively. For extra trust in the test results, they may also be compared to data from third-party services.

Keeping this data separate ensures a clean and manageable main code repository, aiding in maintenance and efficiency.

## Contributing

When submitting changes, please include the git hash of the `sec-parser` repository in your commit message or pull request for version tracking.

## Feedback

For questions or discussions, use [Discussions](https://github.com/orgs/alphanome-ai/discussions). For issues, [open an issue](https://github.com/alphanome-ai/sec-parser/issues).
