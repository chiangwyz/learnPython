"""
为了实现两个链表的数字相加，我们可以遍历两个链表，同时将对应位置的数字相加，考虑进位。具体步骤如下：

创建一个新的链表，用于存储结果。
初始化一个变量 carry为0，用于存储进位。
遍历两个链表，直到两个链表都遍历完毕。
在每次迭代中，将两个链表当前节点的值相加，加上前一步的进位 carry。
计算当前和的个位数，将其作为新节点添加到结果链表的末尾。
计算新的进位，即当前和除以10的商。
移动两个链表的指针到下一个节点。
遍历结束后，检查最后的进位，如果 carry 不为0，则在结果链表末尾添加一个节点，值为 carry。
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # 创建一个哑节点，用于简化边界情况的处理
        current = dummy  # 当前节点
        carry = 0  # 进位

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_val = val1 + val2 + carry

            carry = sum_val // 10  # 计算新的进位
            sum_val = sum_val % 10  # 当前位的值
            current.next = ListNode(sum_val)  # 创建新节点并将其添加到结果链表

            current = current.next  # 移动当前节点指针
            if l1:
                l1 = l1.next  # 移动l1指针
            if l2:
                l2 = l2.next  # 移动l2指针

        return dummy.next  # 返回哑节点的下一个节点，即结果链表的头节点
