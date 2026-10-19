import json


def chunked(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]


def retry(fn, attempts=3):
    last = None
    for _ in range(attempts):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001
            last = exc
    raise last


def load(path="config/client.json"):
    return json.load(open(path))


def main():
    cfg = load()
    for batch in chunked(list(range(50)), 10):
        retry(lambda: len(batch))
    print(bool(cfg))


if __name__ == "__main__":
    main()
