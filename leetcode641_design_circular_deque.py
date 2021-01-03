class ListNode:
    def __init__(self,value):
        self.value = value
        self.prev_node = None
        self.next_node = None
        
    def setValue(self,value):
        self.value = value

class MyCircularDeque:

    def __init__(self, k: int):
        self.size, self.length = k, 0
        self.head , self.tail = ListNode(None), ListNode(None)
        self.head.next_node, self.tail.prev_node = self.tail, self.head
        

    def insertFront(self, value: int) -> bool:
        if self.length == self.size:
            return False
        self.head.setValue(value)
        new_head = ListNode(None)
        new_head.next_node, self.head.prev_node = self.head, new_head
        self.head = new_head
        self.length+=1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.length == self.size:
            return False
        self.tail.setValue(value)
        new_tail = ListNode(None)
        new_tail.prev_node, self.tail.next_node = self.tail, new_tail
        self.tail = new_tail
        self.length+=1
        return True
        

    def deleteFront(self) -> bool:
        if self.length == 0:
            return False
        self.head.next_node = self.head.next_node.next_node
        self.head.next_node.prev_node = self.head
        self.length-=1
        return True
        

    def deleteLast(self) -> bool:
        if self.length == 0:
            return False
        self.tail.prev_node = self.tail.prev_node.prev_node
        self.tail.prev_node.next_node = self.tail
        self.length -= 1
        return True
        

    def getFront(self) -> int:
        if self.length == 0:
            return -1
        return self.head.next_node.value
        

    def getRear(self) -> int:
        if self.length == 0:
            return -1
        return self.tail.prev_node.value
        

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def isFull(self) -> bool:
        return self.length == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()