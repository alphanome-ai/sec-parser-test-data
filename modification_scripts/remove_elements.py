import importlib
import json
import shutil
import sys
from pathlib import Path


class ElementRemover:
    def __init__(
        self,
        predicate,
        report=None,
        base_path=None,
        sec_parser_path="/Users/user/Development/sec-parser",
        report_module="tests.types",
    ):
        self.predicate = predicate
        if not report:
            if sec_parser_path:
                sys.path.insert(0, str(Path(sec_parser_path).resolve()))
            Report = getattr(importlib.import_module(report_module), "Report")
            assert base_path
            self.path = Path(base_path).resolve()
            self.report = Report(
                document_type=self.path.parent.parent.name,
                company_name=self.path.parent.name,
                accession_number=self.path.name,
                path=self.path,
            )
        else:
            self.report = report
        self.input_filename = (
            self.report.path
            / "postprocess_expected_structure_and_text.py.original.json"
        )
        self.output_filename = self.report.path / "expected-structure-and-text.json"
        self.removed_elems_filename = (
            self.report.path / "postprocess_expected_structure_and_text.py.removed.json"
        )

    def copy_if_not_exists(self):
        if not self.input_filename.exists():
            shutil.copy(self.output_filename, self.input_filename)
            print(f"Copied {self.output_filename} to {self.input_filename}")

    def read_elements(self):
        with self.input_filename.open("r") as file:
            return json.load(file)

    def _write_elements(self, elements, filename):
        with filename.open("w") as file:
            json.dump(elements, file, indent=4)

    def remove_elements(self, elements=None, dont_write=False):
        self.copy_if_not_exists()
        if not elements:
            elements = self.read_elements()

        included_elements = []
        removed_elements = []
        for element in elements:
            if not self.predicate(element):
                included_elements.append(element)
            else:
                removed_elements.append(element)

        if not dont_write:
            self.write_elements(included_elements, removed_elements)

        return removed_elements, included_elements

    def write_elements(self, included_elements, removed_elements):
        self._write_elements(included_elements, self.output_filename)
        self._write_elements(removed_elements, self.removed_elems_filename)
