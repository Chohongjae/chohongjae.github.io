---
title: "Add Two Numbers"
categories: 
  - Algorithm
last_modified_at: 2021-02-03T23:00:00+09:00
---

- [https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        next = None
        for i in list(str(self.join_val(l1) + self.join_val(l2))):
            next = ListNode(i, next)
        return next

    def join_val(self, listNode):
        result = ""
        while True:
            result += str(listNode.val)
            if listNode.next is None:
                break
            listNode = listNode.next
        return int(''.join(reversed(result)))


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    result = Solution().addTwoNumbers(l1, l2)
```