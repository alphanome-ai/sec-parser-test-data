# sec-parser-e2e-data

This repository houses the end-to-end (e2e) testing data for the [sec-parser](https://github.com/alphanome-ai/sec-parser) project. For detailed instructions on using the e2e data for testing, please refer to the [Contribution Guide](https://github.com/alphanome-ai/sec-parser/blob/main/CONTRIBUTING.md).

## Purpose

The `sec-parser` project aims to robustly and efficiently parse SEC EDGAR HTML documents into semantic elements and trees. This e2e data repository provides sample input documents and their expected output results, serving as a benchmark for ensuring consistent and accurate parsing performance.

The data is kept separate from the code to avoid bloating the code repository with data. This ensures that the code repository remains lightweight and manageable, improving the efficiency of codebase operations and maintenance.

## Contribution & Testing

If you're a contributor to `sec-parser`, you can utilize this dataset to run e2e tests and ensure that changes don't introduce regressions. For detailed instructions on using this data for testing, please refer to the main [sec-parser repository](https://github.com/alphanome-ai/sec-parser).

When submitting results by creating new commits in this repository, it's highly recommended to include the git hash of the `sec-parser` repository in your commit message. This practice helps us track the specific version of `sec-parser` that produced the results.

## Feedback & Issues

For asking questions and discussing potential improvements, use [Discussions](https://github.com/orgs/alphanome-ai/discussions). For any issues, please [open an issue](https://github.com/alphanome-ai/sec-parser/issues).
