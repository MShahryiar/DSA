class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def Perpend(self, data):
        newNode = Node(data)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    def traverse(self):
        currNode = self._head
        while currNode is not None:
            print(currNode.data, " -> ",end="")
            currNode = currNode.next
        print("End!")

    def contains(self, target):
        curNode = self._head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next

        assert curNode is not None, "Target must be in the list!"
        print(f"Target '{target}' : Found")

    def remove(self, target):
        predNode = None
        curNode = self._head
        while curNode is not None and curNode.data is not target:
            predNode = curNode
            curNode = curNode.next
        
        assert curNode is not None, "Item must be in the List."
        self._size -= 1
        if curNode is self._head:
            self._head = curNode.next
        else:
            predNode.next = curNode.next
        print("Removing : ",curNode.data)

# ll = LinkedList()
# print("Initial Length",ll.__len__())
# ll.Perpend(0)
# ll.Perpend(1)
# ll.Perpend(2)
# ll.Perpend(3)
# ll.Perpend(4)
# print("Length after adding Elements",ll.__len__())
# ll.traverse()
# ll.contains(4)
# ll.remove(3)
# ll.traverse()