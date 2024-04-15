from ds.node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    '''
    Insertion 
    '''
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = Node(data)

    '''
        Prepend
    '''
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    '''
        Insert after given node data
    '''
    def insert_after_node(self, pre_node, data):
        if not pre_node:
            print("Previous node does not exists")
            return
        new_node = Node(data)
        new_node.next = pre_node.next
        pre_node.next = new_node

    '''
        delete node by node data
    '''
    def delete_node(self, data):
        curr_node = self.head

        if curr_node and curr_node.data == data:
            self.head = curr_node.next
            curr_node = None
            return
        prev_node = None
        while curr_node and curr_node.data != data:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is Node:
            return
        prev_node.next = curr_node.next
        curr_node = None

    '''
        delete node by node pos
    '''
    def delete_node_by_pos(self, pos):
        curr_node = self.head

        if pos == 0:
            self.head = curr_node.next
            curr_node = None
            return
        prev_node = None
        count = 0
        while curr_node and pos != count:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1

        if curr_node is None:
            return

        prev_node.next = curr_node.next
        curr_node = None

    '''
        length by iterative method
    '''
    def len_iterative(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    '''
        length by recursive method
    '''
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    '''
        node swap
    '''
    def node_swap(self, data_01, data_02):

        if data_01 == data_02:
            return

        prev_node_01 = None
        curr_node_01 = self.head

        while curr_node_01 and curr_node_01.data != data_01:
            prev_node_01 = curr_node_01
            curr_node_01 = curr_node_01.next

        prev_node_02 = None
        curr_node_02 = self.head
        while curr_node_02 and curr_node_02.data != data_02:
            prev_node_02 = curr_node_02
            curr_node_02 = curr_node_02.next

        if not curr_node_01 or not curr_node_02:
            return

        if prev_node_01:
            prev_node_01.next = curr_node_02
        else:
            self.head = curr_node_02

        if prev_node_02:
            prev_node_02.next = curr_node_01
        else:
            self.head = curr_node_01

        curr_node_01.next, curr_node_02.next = curr_node_02.next, curr_node_01.next

    '''
        printing list
    '''
    def linked_list_data(self):
        curr_node = self.head
        nodes = []
        while curr_node:
            nodes.append(curr_node.data)
            curr_node = curr_node.next
        return nodes

    '''
        reversing list by iterative method
    '''
    def reverse_iterative(self):
        curr_node = self.head
        prev_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
    '''
        reversing list by recursive method
    '''
    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)
        self.head = _reverse_recursive(cur = self.head, prev=None)

    ''' 
    Mege sort linked list
    '''
    def merge_sort_list(self, list):
        p = self.head
        q = list.head
        s = None

        if not p:
            return s
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = q.next
        new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q

        if not q:
            s.next = p

        self.head = new_head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def get_nth_from_last(self, n):
        cur = self.head
        total_len = self.len_iterative()
        while cur:
            if total_len == n:
                return cur.data
            total_len -= 1
            cur = cur.next

        if cur is None:
            return

    def count_occuerences(self, data):
        cur = self.head
        count = 0
        while cur:
            if cur.data == data:
                count += 1
            cur =cur.next
        return count

    def rotate(self, pivot):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < pivot:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None


    def is_plaindrome(self):
        pass