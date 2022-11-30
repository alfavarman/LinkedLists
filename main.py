class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data=data, next=self.head)
        self.head = node

    def print_ll(self):
        if self.head is None:
            print("No Elements")
            return

        itr = self.head
        while itr:
            print(str(itr.data) + '---->', end=' ')
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(33)
    ll.insert_at_beginning(63)
    ll.insert_at_beginning(8)
    ll.print_ll()



