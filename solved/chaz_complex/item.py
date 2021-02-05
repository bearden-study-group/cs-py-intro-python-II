from typing import Optional


class Item:
    def __init__(self,
                 name: str,
                 weight: float = 10,
                 description: Optional[str] = None,
                 ):
        self.name = name
        self.description = description if description is not None else "No description given!"
        self.weight = weight

    def __repr__(self):
        return f"Item({self.name}, {self.weight})"

    def __str__(self):
        return f"{self.name}, {self.description}"
