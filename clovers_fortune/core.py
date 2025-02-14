from io import BytesIO
from pathlib import Path


class Manager:
    def __init__(self):
        self.results: dict[str, str] = {}
        self._cache: dict[str, dict[str, str]] = {}

    def divine(self, user_id: str) -> str:
        pass

    def draw(self, result: str, group_id: str) -> BytesIO:
        pass

    def cache(self, group_id: str, user_id: str) -> None | BytesIO:
        file = self._cache.setdefault(group_id, {}).get(user_id)
        if file is None:
            return
        file = Path(file)
        if not file.exists():
            return
        with file.open("rb") as f:
            return BytesIO(f.read())

    def tarot(self, group_id: str, user_id: str) -> None | BytesIO:
        pass


manager = Manager()
