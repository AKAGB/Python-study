class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode((l1.val + l2.val) % 10)
        p = result
        ex_in = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + ex_in) % 10)
            ex_in = (l1.val + l2.val + ex_in) // 10
            p = p.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            p.next = ListNode((l1.val + ex_in) % 10)
            ex_in = (l1.val + ex_in) // 10
            p = p.next
            l1 = l1.next
        while l2:
            p.next = ListNode((l2.val + ex_in) % 10)
            ex_in = (l2.val + ex_in) // 10
            p = p.next
            l2 = l2.next
        if ex_in:
            p.next = ListNode(1)
        return result