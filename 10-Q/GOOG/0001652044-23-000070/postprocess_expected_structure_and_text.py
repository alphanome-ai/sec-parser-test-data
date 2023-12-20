import sys
from collections import Counter
from pathlib import Path
from pprint import pp

from frozendict import frozendict


class RemoveIfTrue:
    def __init__(self, counter):
        self.counter = counter

    def __call__(self, e: dict) -> bool:
        if e.get("text_content", "").isdigit():
            return True
        if (
            e["cls_name"] == "TitleElement"
            and e.get("text_content", "") == "Alphabet Inc."
        ):
            return True
        if (
            self.counter[frozendict(e)] > 2
            and e["cls_name"]
            not in (
                "TableElement",
                "SupplementaryText",
            )
            and "Compared with" not in e.get("text_content", "")
            and e.get("level", 0) < 3
        ):
            return True

        return False


def main(report=None):
    this_path = Path(__file__).parent
    root_path = this_path.parent.parent.parent
    sys.path.insert(0, str(root_path))
    from modification_scripts.remove_elements import ElementRemover  # noqa: E402

    counter = Counter()
    remover = ElementRemover(
        predicate=RemoveIfTrue(counter), report=report, base_path=str(this_path)
    )
    remover.copy_if_not_exists()
    elements = remover.read_elements()
    counter.update([frozendict(e) for e in elements])
    removed, included = remover.remove_elements(elements)

    print("# Removed:")
    pp(Counter(element["cls_name"] for element in removed))

    print("\n# Included:")
    pp(Counter(element["cls_name"] for element in included))


if __name__ == "__main__":
    main()
