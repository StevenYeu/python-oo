from __future__ import annotations
from typing import Optional


class LinkedListIterator:
    def __init__(self, current: Optional[ListNode]) -> None:
        self.current: Optional[ListNode] = current

    def __iter__(self):
        return self.current

    def __next__(self):
        if self.current:
            node = self.current.next
            self.current = node
            return node
        else:
            raise StopIteration


class ListNode:
    def __init__(self, val: int) -> None:
        self.next: Optional[ListNode] = None
        self.val = val


class LinkedList:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.interator = LinkedListIterator(current=self.head)

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next


def main():
    head = ListNode(1)
    head.next = ListNode(val=2)

    # # head.next.next = ListNode(val=3)
    # for node in head:
    #     if node:
    #         print(node.val)


if __name__ == "__main__":
    main()
