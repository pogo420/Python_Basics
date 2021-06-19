from json import JSONEncoder

# customer json encoder
from typing import Any


class CustomJsonEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return super().default(o)

