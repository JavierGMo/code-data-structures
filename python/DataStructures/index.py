from LinkedList import LinkedList
from Queue import Queue
from Stack import Stack

linkedList = LinkedList()
queue = Queue()
stack = Stack()
for i in range(10):
    linkedList.append(i*2)
    queue.enqueue(i*10)
    stack.append(i*4)
    print(i*4)
# linkedList.append(5)

linkedList.insert(position=0, value=90)

print(linkedList)
print(queue)
print(stack.head)
print(f"Stack: {stack}")
