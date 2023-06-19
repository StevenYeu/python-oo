from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class ListNode(Generic[T]):
    value: T
    next: Optional[ListNode]


class LinkedList(Generic[T]):
    def __init__(self, head: Optional[ListNode] = None) -> None:
        super().__init__()
        self.head = head

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Node(Generic[T]):
    def __init__(self, value: T, next: Optional[Node] = None) -> None:
        super().__init__()
        self.value = value
        self.next: Optional[Node] = next

    def __iter__(self):
        node = self
        while node:
            yield node
            node = node.next


class LinkedListIterator:
    def __init__(self, node: ListNode) -> None:
        self.current: Optional[ListNode] = node

    def __iter__(self):
        return self

    def __next__(self) -> ListNode:
        if self.current is not None:
            cur = self.current
            self.current = self.current.next
            return cur
        else:
            raise StopIteration()


class LNode(Generic[T]):
    def __init__(self, value: T, next: Optional[LNode] = None) -> None:
        super().__init__()
        self.value = value
        self.next: Optional[LNode] = next


def main():
    # Using DataClass and LinkedList Container
    third = ListNode(value=3, next=None)
    second = ListNode(value=2, next=third)
    head = ListNode(value=1, next=second)
    myList = LinkedList(head=head)
    myIter = LinkedListIterator(head)

    print("Using a LinkedList Container with Iterable Protocol")
    for node in myList:
        print(f"Node value is: {node.value}")

    print("Using Separate Iterator")
    for node in myIter:
        print(f"Node vaue is: {node.value}")

    third = Node(value="c")
    second = Node(value="b", next=third)
    head = Node(value="a", next=second)

    print("Using Node with Iterable Protocol")
    for node in head:
        print(f"Node value is: {node.value}")


if __name__ == "__main__":
    main()
