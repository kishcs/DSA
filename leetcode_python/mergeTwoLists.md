You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Example 1
- Input: list1 = [1,2,4], list2 = [1,3,4]
- Output: [1,1,2,3,4,4]

## Example 2:
- Input: list1 = [], list2 = []
- Output: []

## Example 3:
- Input: list1 = [], list2 = [0]
- Output: [0]

```
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        merged = None
        head = None
        f = list1
        s = list2
        while f and s:
            if f.val > s.val:
                if merged is None:
                    merged = ListNode(s.val)
                    head = merged
                else:
                    merged.next = ListNode(s.val)
                    merged = merged.next
                s = s.next
            else:
                if merged is None:
                    merged = ListNode(f.val)
                    head = merged
                else:
                    merged.next = ListNode(f.val)
                    merged = merged.next
                f = f.next
        if not f:
            while s:
                merged.next = ListNode(s.val)
                merged = merged.next
                s = s.next
        if not s:
            while f:
                merged.next = ListNode(f.val)
                merged = merged.next
                f = f.next
        return head

    def printList(self, list: ListNode):
        while list:
            print(list.val, end=' ')
            list = list.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    s = Solution()
    l3 = s.mergeTwoLists(l1, l2)
    s.printList(l3)

```
