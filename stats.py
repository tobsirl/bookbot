def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for ch in text:
        key = ch.lower()
        counts[key] = counts.get(key, 0) + 1
    return counts

def _get_num(item: dict[str, int]) -> int:
    return item["num"]

def sort_character_counts(char_counts: dict[str, int]) -> list[dict[str, int]]:
    items: list[dict[str, int]] = [
        {"char": ch, "num": num} for ch, num in char_counts.items()
    ]
    items.sort(key=_get_num, reverse=True)
    return items