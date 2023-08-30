from Node.Node import Node

class Stack:
    head: Node | None = None
    length: int = 0
    
    def __init__(self, firstNode: Node | None = None) -> None:
        self.head = firstNode
    def append(self, value):
        newNode = self.createNode(value=value)
        newNode.nextNode = self.head
        self.head = newNode
        self.length += 1
    
    def pop(self):
        if not self.head:
            print("Stack is empty")
            return
        current = self.head
        self.head = self.head.nextNode
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