from Node.Node import Node

class LinkedList:
    head: Node | None = None
    length: int = 0
    def __init__(self, head: Node | None = None) -> None:
        self.head = head
    
    def find(self, value) -> None | int:
        current = self.head
        index = 0
        if not current:
            return None
        while current:
            if current.value == value:
                return index
            current = current.nextNode
            index += 1

    def append(self, value) -> None:
        newNode = self.createNode(value)
        currentNode = self.head
        if not currentNode:
            self.head = newNode
            self.length += 1
            return
        while currentNode.nextNode:
            currentNode = currentNode.nextNode
        currentNode.nextNode = newNode
        self.length += 1
    
    def insert(self, position: int, value):
        current = self.head
        newNode: Node | None = None
        prev: Node | None = None
        index = 0
        if not current:
            return None
        newNode = self.createNode(value=value)
        if position == 0:
            newNode.nextNode = current
            self.head = newNode
            self.length += 1
            return
        while current:
            if index == position:
                break
            prev = current
            current = current.nextNode
            index += 1
        prev.nextNode = newNode
        newNode.nextNode = current
        self.length += 1

    def delete(self, value):
        current: Node = self.head
        prev: Node = None
        if not current:
            return
        if current.value == value:
            self.head = current.nextNode
            current = None
            self.length -= 1
            return
        while current:
            if current.value == value:
                break
            prev = current
            current = current.nextNode
        prev.nextNode = current.nextNode
        current = None
        self.length -= 1

    def createNode(self, value) -> Node:
        return Node(value=value)
    
    def __str__(self) -> str:
        linkedListValues = ''
        currentNode: Node = self.head
        if not self.head:
            return ''
        while currentNode:
            linkedListValues += f'{currentNode.value} '
            currentNode = currentNode.nextNode
        return linkedListValues
