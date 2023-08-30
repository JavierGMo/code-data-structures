from typing_extensions import Self

class Node:
    value = None
    nextNode: Self = None
    def __init__(self, value) -> None:
        self.value = value
        self.nextNode = None

    def __str__(self) -> str:
        return f'Value: {self.value} | Next node: {self.nextNode.value if self.nextNode else None}'