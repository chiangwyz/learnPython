"""
1. 迭代原始链表：
对于原始链表的每个节点，创建一个新节点，其值与原始节点相同。将新节点插入到原始节点和其下一个节点之间。

2. 更新随机指针：
迭代修改后的链表，设置每个新节点的随机指针。如果原始节点 A 的随机指针指向节点 B，那么复制的节点 A' 的随机指针应指向复制的节点 B'。

3. 拆分链表：
最后，将修改后的链表拆分为原始链表和复制链表。

这个过程中的关键在于保持原始链表不变，同时创建新链表的副本。
"""

from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val: int, next: Node = None, random: Node = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # 第一步：复制每个节点，并将复制节点放置在原节点后面
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            # 这一步是关键，用老节点继续复制。
            current = new_node.next

        # 第二步：设置新节点的随机指针
        current = head
        while current:
            if current.random:
                # 将老节点的随机指针下后续指针复制给新节点的随机指针
                current.next.random = current.random.next
            current = current.next.next

        # 第三步：拆分链表
        old_list = head
        new_list = head.next
        new_head = head.next
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next

        return new_head


