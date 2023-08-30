from Node.Node import Node

class Queue:
    head: Node | None = None
    length: int = 0
    def __init__(self, head: Node | None = None) -> None:
        self.head = head
    
    def enqueue(self, value):
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
    
    def dequeue(self):
        if not self.head:
            print("Queue is empty")
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
