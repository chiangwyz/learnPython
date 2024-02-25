"""
关键知识点：
self.num_to_index = {} 这个字典（也称为哈希表）在 RandomizedSet 类中的主要作用是确保 insert 和 remove 操作可以在 O(1) 时间复杂度内完成。
它通过将每个值映射到其在 self.num_list 列表中的索引来实现这一点。

1. 在 insert 操作中，我们可以通过检查字典来快速确定一个值是否已经存在于集合中，从而保持 O(1) 的时间复杂度。
2. 在 remove 操作中，我们需要能够快速找到要删除元素的位置，并且在删除它之后还要保持列表的连续性。
    这就需要将最后一个元素移动到被删除元素的位置，这样就不会留下空位。字典使我们能够在 O(1) 时间内找到这两个元素的索引，从而快速进行这个操作。
3. getRandom 操作则是通过随机选择 self.num_list 列表中的一个索引来返回一个元素，因为列表的随机访问也是 O(1) 的。
"""

import random

class RandomizedSet:
    def __init__(self):
        # 用于存储元素的列表
        self.num_list = []
        # 哈希表，键为元素，值为该元素在列表中的索引
        self.num_to_index = {}

    def insert(self, val: int) -> bool:
        # 如果元素已存在，返回 False
        if val in self.num_to_index:
            return False
        # 在哈希表中记录元素的索引
        self.num_to_index[val] = len(self.num_list)
        # 在列表中添加元素
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        # 如果元素不存在，返回 False
        if val not in self.num_to_index:
            return False
        # 获取要删除元素的索引
        idx_to_remove = self.num_to_index[val]
        # 获取列表中的最后一个元素
        last_element = self.num_list[-1]
        # 将最后一个元素移动到要删除元素的位置
        self.num_list[idx_to_remove] = last_element
        # 更新哈希表中最后一个元素的索引
        self.num_to_index[last_element] = idx_to_remove
        # 从列表中移除最后一个元素
        self.num_list.pop()
        # 从哈希表中删除要移除的元素
        del self.num_to_index[val]
        return True

    def getRandom(self) -> int:
        # 随机返回列表中的一个元素
        return random.choice(self.num_list)
