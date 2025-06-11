def find(l: list, item: str) -> str:
    return next((x for x in l if item in x), None)