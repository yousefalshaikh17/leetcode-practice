# 2. Add Two Numbers
# Topics: Linked List, Math, Recursion
# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        solution = None
        solution_start = None
        add_next = 0

        while True:
            if l1 is not None and l2 is not None:
                result = l1.val + l2.val + add_next
                add_next = 0
                if result > 9:
                     add_next = 1
                     result -= 10
                new_node = ListNode(result)
            else:
                if l1 is None and l2 is None:
                    if add_next > 0:
                        new_node = ListNode(add_next)
                        add_next = 0
                else:
                    result = (l1.val if l1 else l2.val) + add_next
                    add_next = 0
                    if result > 9:
                        add_next = 1
                        result -= 10
                    new_node = ListNode(result)

            if new_node is None:
                break
            if solution is None and solution_start is None:
                solution = new_node
                solution_start = new_node
            else:
                solution.next = new_node
                solution = new_node
            new_node = None
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return solution_start
        