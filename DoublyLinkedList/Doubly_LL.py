class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLL:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            return

        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
        return

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beg(data)
            return
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next

            node = Node(data, None, itr)
            itr.next = node
        return

    def insert_at_pos(self, data, pos):
        if pos == 1:
            self.insert_at_beg(data)
            return
        else:
            itr = self.head
            for i in range(1, pos-1):
                itr = itr.next
            node = Node(data, itr.next, itr)
            if itr.next is None:
                itr.next = node
            else:
                itr.next = node
                node.next.prev = node
        return

    def delete_from_pos(self, pos):
        if self.head is None:
            print("linked list is empty!!")
            return
        else:
            temp = self.head
            for i in range(1, pos):
                temp = temp.next
            if temp.next is None:
                temp.prev.next = None
            else:
                temp.next.prev = temp.prev
                temp.prev.next = temp.next

            print(f"<Node containing data '{temp.data}' at position {pos} is deleted> ")
            del temp
        return

    def display(self):
        itr = self.head
        dllist = ''
        while itr is not None:
            dllist += str(itr.data) + ' ---> '
            itr = itr.next

        print(dllist)


if __name__ == "__main__":
    dll = DoublyLL()
    dll.insert_at_beg(3)
    dll.insert_at_beg(2)
    dll.insert_at_beg(1)
    dll.insert_at_end(5)
    dll.insert_at_end(6)
    dll.insert_at_pos('At4', 4)
    dll.insert_at_pos('At7', 7)
    dll.insert_at_pos('At8', 8)
    dll.display()
    dll.delete_from_pos(5)
    print("New List after deletion is: \n")
    dll.display()
    dll.delete_from_pos(7)
    print("\nNew List after deletion is: \n")
    dll.display()