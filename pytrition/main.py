def available_items() -> list:
    """Return a list of available items."""
    return ["avocado", "apple", "banana"]


def facts(item: str) -> dict:
    """Return nutrition facts for a given item."""
    print(f"Getting nutrition facts for {item}")
    return {}


if __name__ == "__main__":
    facts("avocado")
