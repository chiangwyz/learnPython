"""
为了实现两个链表的数字相加，我们可以遍历两个链表，同时将对应位置的数字相加，考虑进位。

具体步骤如下：

1. 创建一个新的链表，用于存储结果。
2. 初始化一个变量 carry 为0，用于存储进位。
3. 遍历两个链表，直到两个链表都遍历完毕。
    在每次迭代中，将两个链表当前节点的值相加，加上前一步的进位 carry。
    计算当前和的个位数，将其作为新节点添加到结果链表的末尾。
    计算新的进位，即当前和除以10的商。
4. 移动两个链表的指针到下一个节点。
5. 遍历结束后，检查最后的进位，如果 carry 不为0，则在结果链表末尾添加一个节点，值为 carry。
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个哑节点，用于简化边界情况的处理
        dummy = ListNode(0)
        # 当前节点
        current = dummy
        # 进位
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_val = val1 + val2 + carry

            # 计算新的进位
            carry = sum_val // 10
            # 当前位的值
            sum_val = sum_val % 10
            # 创建新节点并将其添加到结果链表
            current.next = ListNode(sum_val)

            # 移动当前节点指针
            current = current.next

            # 移动l1指针
            if l1:
                l1 = l1.next

            # 移动l2指针
            if l2:
                l2 = l2.next

        # 返回哑节点的下一个节点，即结果链表的头节点
        return dummy.next


def create_linked_list(arr: list[int]) -> Optional[ListNode]:
    """根据给定的列表创建链表"""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def print_linked_list(head: Optional[ListNode]):
    """打印链表的内容"""
    current = head
    res = []
    while current:
        res.append(current.val)
        current = current.next
    print(res)


# 示例数据和分割值
l1 = [2,4,3]
l2 = [5,6,4]

l1_head = create_linked_list(l1)
l2_head = create_linked_list(l2)

solution = Solution()
print_linked_list(solution.addTwoNumbers(l1_head, l2_head))


l3 = [9,9,9,9,9,9,9]
l4 = [9,9,9,9]
l3_head = create_linked_list(l3)
l4_head = create_linked_list(l4)
print_linked_list(solution.addTwoNumbers(l3_head, l4_head))