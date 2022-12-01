class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data) -> None:
        node = Node(data=data, next=self.head)
        self.head = node

    def print_ll(self) -> None:
        if self.head is None:
            print("No Elements")
            return

        itr = self.head
        while itr:
            print(str(itr.data) + '---->', end=' ')
            itr = itr.next
        print()

    def insert_at_end(self, data) -> None:
        # if the LL is empty:
        if self.head is None:
            self.head = Node(data=data, next=None)
        else:
            itr = self.head
            while itr and itr.next is not None:
                itr = itr.next
            itr.next = Node(data=data, next=None)

    def insert_values(self, arr: list) -> None:
        for value in arr:
            self.insert_at_end(value)

    def len_ll(self) -> int:
        if self.head is None:
            return 0
        counter = 1
        itr = self.head
        while itr and itr.next is not None:
            itr = itr.next
            counter += 1
        return counter

    def remove_index(self, idx: int):
        if idx < 0 or idx >= self.len_ll():
            raise Exception("index out of range")

        if idx == 0:
            self.head = self.head.next
            return

        counter = 0
        itr = self.head
        while itr and counter < idx -1:
            counter += 1
            itr = itr.next
        itr.next = itr.next.next

    def remove_value(self, val):
        if self.head is None:
            print("No Elements")
            return

        itr = self.head
        while itr and itr.next.data != val:
            itr = itr.next

        itr.next = itr.next.next


    def insert_at_index(self, idx: int, data: object):
        if idx == 0 or self.head is None:
            self.insert_at_beginning(data)
            return
        itr = self.head
        counter = 0
        while itr and counter < idx -1:
            counter += 1
            itr = itr.next
        itr.next = Node(data=data, next=itr.next.next)


    def insert_after_value(self, data_after: object, data_to_insert: object):
        if self.head is None:
            self.insert_at_beginning(data_to_insert)
            return

        itr = self.head
        while itr and itr.data =


if __name__ == '__main__':
    ll = LinkedList()
    ll.print_ll()
    print(f'll.len(): {ll.len_ll()}')
    ll.insert_values([22, 33, 44, 34, 36, 76])
    ll.insert_at_index(0, 600)
    ll.print_ll()
    ll.remove_index(3)
    ll.print_ll()
    print(f'll.len(): {ll.len_ll()}')
    ll.insert_at_beginning(33)
    ll.print_ll()
    ll.insert_at_beginning(63)
    ll.print_ll()
    ll.insert_at_beginning(8)
    ll.print_ll()
    ll.insert_at_end(22.2)
    ll.print_ll()
    ll.insert_values([1, 22, 66, 77])
    ll.print_ll()
    ll.remove_value(22)
    ll.remove_value(77)
    ll.print_ll()



