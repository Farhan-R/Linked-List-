class Node:
    # Function to initialize the node object
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLL:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next

            itr.next = Node(data, None)

    def insert_at_pos(self, data, pos):
        if pos == 1:
            self.insert_at_beg(data)
            return
        else:
            itr = self.head  # iterator
            for i in range(1, pos-1):  # iterating till the node just before position
                itr = itr.next
            node = Node(data, itr.next)  # creating node with its 'next' containing address of node currently at pos
            itr.next = node  # linking node at 'pos-1' to newly created node

    def delete_from_pos(self, pos):
        if self.head is None:
            print("Linked lis is Empty!")
        elif pos == 1:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            itr = self.head
            temp = self.head
            for i in range(1, pos-1):
                itr = itr.next
                temp = itr.next
            itr.next = temp.next
            del temp

    def display(self):
        if self.head is None:
            print("Linked list is empty!!")
            return

        itr = self.head
        llist = ''

        while itr:
            llist += str(itr.data) + ' ---> '
            itr = itr.next

        print(llist)


if __name__ == "__main__":
    sll = SinglyLL()
    sll.insert_at_beg(13)
    sll.insert_at_beg(10)
    sll.insert_at_beg(28)
    sll.insert_at_end(8)
    sll.insert_at_end(7)
    sll.insert_at_end(8)
    sll.insert_at_end('Good')
    sll.insert_at_pos('Very', 1)
    sll.insert_at_pos('At2', 2)
    sll.insert_at_pos('At3', 3)
    sll.insert_at_pos('At7', 7)
    sll.delete_from_pos(11)
    sll.insert_at_end('Nice')
    sll.display()
