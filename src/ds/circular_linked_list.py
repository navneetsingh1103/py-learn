from ds.linked_list import LinkedList
from ds.node import Node


class CircularLinkedList(LinkedList):

    def __init__(self):
        super().__init__()

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            return
        last_node = self.head
        new_node = Node(data)
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head


    def delete_node(self, data):
        if self.head:
            if self.head.data == data:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head
                prev = None
                while cur:
                    prev = cur
                    cur = cur.next
                    if cur.data == data:
                        prev.next = cur.next
                        cur = cur.next
