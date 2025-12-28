class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    # Reverse
    @staticmethod
    def reverse(head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    # Merge sort
    @staticmethod
    def sort(head):
        if head is None or head.next is None:
            return head

        middle = LinkedList.get_middle(head)
        right_head = middle.next
        middle.next = None

        left = LinkedList.sort(head)
        right = LinkedList.sort(right_head)

        return LinkedList.merge(left, right)

    @staticmethod
    def get_middle(head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Merge two sorted lists
    @staticmethod
    def merge(l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next


def main():
    list1 = LinkedList()
    for x in [4, 2, 1, 3]:
        list1.insert_at_end(x)

    print("Original:")
    list1.print_list()

    list1.head = LinkedList.reverse(list1.head)
    print("Reversed:")
    list1.print_list()

    list1.head = LinkedList.sort(list1.head)
    print("Sorted:")
    list1.print_list()

    list2 = LinkedList()
    for x in [0, 5, 6]:
        list2.insert_at_end(x)

    print("Merged:")
    merged = LinkedList()
    merged.head = LinkedList.merge(list1.head, list2.head)
    merged.print_list()


main()
