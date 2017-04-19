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

    # 网络版本，非常简洁
    # carry, val = divmod(v1 + v2 + carry, 10)
    # 学习了 divmod(a,b) 方法返回的是a//b（除法取整）以及a对b的余数

    # @return a ListNode
    def addTwoNumbers_new(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


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

