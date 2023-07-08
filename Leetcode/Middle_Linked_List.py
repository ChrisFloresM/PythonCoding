#Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
        node = ListNode(value)
        if self.head == None:
            self.head = node
            return
        current_node = self.head
        while True:
            if current_node.next == None:
                current_node.next = node
                break
            current_node = current_node.next
    
    def showList(self):
        current_node = self.head
        while current_node != None:
            print(current_node.val, "->", end=" ")
            current_node = current_node.next
        print("None")
                    
class Solution(object):
    def middleNode(self, head):
        middle = head
        end = head
        while(end != None and end.next != None):
            middle = middle.next 
            end = end.next.next 
        return middle 
        """
        :type head: ListNode
        :rtype: ListNode
        """
"""         
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
while True:
    print(head.val, "->", end=" ")
    if head.next == None:
        print("End")
        break
    head = head.next     """
    
myLinkedList = LinkedList()
myLinkedList.showList()
myLinkedList.insert(4)
myLinkedList.showList()
myLinkedList.insert(5)
myLinkedList.showList()
myLinkedList.insert(6)
myLinkedList.showList()
myLinkedList.insert(7)
myLinkedList.showList()
myLinkedList.insert(8)
myLinkedList.showList()

mySolution = Solution()
print(mySolution.middleNode(myLinkedList.head).val)



