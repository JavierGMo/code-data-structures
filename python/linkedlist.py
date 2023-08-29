class Node:
    value = None
    nextNode = None
    def __init__(self, value) -> None:
        self.value = value
        self.nextNode = None

class LinkedList:
    head: Node = None
    length: int = 0
    def __init__(self, head: Node = None) -> None:
        self.head = head
    
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
    def createNode(self, value) -> Node:
        return Node(value=value)
    
    def __str__(self) -> str:
        linkedListValues = ''
        currentNode: Node = self.head
        if not self.head:
            return ''
        while currentNode:
            linkedListValues += f'{currentNode.value}'
            currentNode = currentNode.nextNode
        return linkedListValues

linkedList = LinkedList()
linkedList.append(5)

print(linkedList)
