# https://leetcode.com/problems/add-two-numbers/#/description


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        i = l1
        j = l2
        return_head = ListNode(0)
        q = return_head
        while i is not None and j is not None:
            temp = i.val + j.val + carry
            carry = temp // 10
            num = temp % 10
            p = ListNode(num)
            q.next = p
            q = p
            i = i.next
            j = j.next

        return_head = return_head.next

        if i is not None:
            while i is not None:
                temp = i.val + carry
                carry = temp // 10
                num = temp % 10
                p = ListNode(num)
                q.next = p
                q = p
                i = i.next
        elif j is not None:
            while j is not None:
                temp = j.val + carry
                carry = temp // 10
                num = temp % 10
                p = ListNode(num)
                q.next = p
                q = p
                j = j.next
        if carry != 0:
            q.next = ListNode(carry)

        return return_head

a = ListNode(3)
b = ListNode(4)
c = ListNode(2)
b.next = a
c.next = b

a = ListNode(4)
y = ListNode(6)
xx = ListNode(5)
y.next = a
xx.next = y

test = Solution()
print(test.addTwoNumbers(c, xx))

