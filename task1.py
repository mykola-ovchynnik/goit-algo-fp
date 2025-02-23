class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=", " if current.next else "\n")
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def merge_sort(self, h):
        if h is None or h.next is None:
            return h

        middle = self.get_middle(h)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(h)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sort(self):
        self.head = self.merge_sort(self.head)

    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node(0)
        tail = dummy
        a = list1.head
        b = list2.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a or b
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


if __name__ == "__main__":
    list1 = LinkedList()
    for value in [3, 1, 5, 2]:
        list1.append(value)
    print("Initial list 1:")
    list1.print_list()

    list1.reverse()
    print("Reversed list:")
    list1.print_list()

    list1.sort()
    print("Sorted list:")
    list1.print_list()

    list2 = LinkedList()
    for value in [4, 6, 7]:
        list2.append(value)
    print("Sorted list 2:")
    list2.print_list()

    merged_list = LinkedList.merge_sorted_lists(list1, list2)
    print("Merged list:")
    merged_list.print_list()
