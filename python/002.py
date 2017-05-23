import sys
import os

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        d1 = self.list_to_int(l1)
        d2 = self.list_to_int(l2)
        s = d1 + d2
        return self.int_to_list(s)

    def list_to_int(self, l_input):
        l = l_input
        ret_val = 0
        digit_count = 0
        while True:
            ret_val += l.val * 10 ** digit_count
            if not l.next:
                break
            else:
                digit_count += 1
                l = l.next
        return ret_val

    def int_to_list(self, d):
        ret_node = ListNode(d % 10)
        if d < 10:
            return ret_node
        else:
            ret_node.next = self.int_to_list(d / 10)
        return ret_node


if '__main__' == __name__:
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solver = Solution()
    ret_list = solver.addTwoNumbers(l1, l2)
    print ret_list.val, ret_list.next.val, ret_list.next.next.val
