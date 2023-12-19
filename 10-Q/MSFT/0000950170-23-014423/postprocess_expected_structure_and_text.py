import sys
from collections import Counter
from pathlib import Path
from pprint import pp


class RemoveIfTrue:
    def __init__(self):
        pass

    def __call__(self, e: dict) -> bool:
        if text := e.get("text_content"):
            if text.isdigit():
                return True
        return False


def main(report=None):
    this_path = Path(__file__).parent
    root_path = this_path.parent.parent.parent
    sys.path.insert(0, str(root_path))
    from modification_scripts.remove_elements import ElementRemover  # noqa: E402

    remover = ElementRemover(
        predicate=RemoveIfTrue(), report=report, base_path=str(this_path)
    )
    removed, included = remover.remove_elements()

    print("# Removed:")
    pp(Counter(element["cls_name"] for element in removed))

    print("\n# Included:")
    pp(Counter(element["cls_name"] for element in included))


if __name__ == "__main__":
    main()
