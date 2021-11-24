def load_text(path: str) -> str:
    with open(path, "r") as f:
        text = f.read()
    return text
