"""
LRU是Least Recently Used的缩写，即最近最少使用，是一种常用的页面置换算法，
选择最近最久未使用的页面予以淘汰。该算法赋予每个页面一个访问字段，用来记录一个页面自上次被访问以来所经历的时间 t，
当须淘汰一个页面时，选择现有页面中其 t 值最大的，即最近最少使用的页面予以淘汰。

我们还需要一个辅助的双向链表节点类 DLinkedNode，用于实现 LRU 缓存。

1. 双向链表节点类 (DLinkedNode)：这是一个内部类，用于创建缓存中的节点。每个节点包含键、值、前驱节点引用 prev 和后继节点引用 next。
2. 构造器 (__init__)：初始化容量、哈希表和双向链表的头尾哨兵节点。
3. 获取数据 (get)：如果键存在于缓存中，则返回相应的值并将其移动到链表头部（表示最近使用过）。如果键不存在，则返回 -1。
4. 添加/更新数据 (put)：如果键已存在，更新其值并移动到链表头部。如果是新键，需要添加新节点到链表头部。
    如果添加新节点后超出容量，需要删除链表尾部节点（最少使用的节点）并从哈希表中移除对应的键。
"""

class LRUCache:
    class DLinkedNode:
        # 双向链表的节点类
        def __init__(self, key: int=0, value: int=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        # 初始化LRU缓存
        # 哈希表用于存储键和节点
        self.cache = {}
        # 缓存容量
        self.capacity = capacity
        # 使用两个哨兵节点head和tail简化边界条件处理
        self.head = self.DLinkedNode()
        self.tail = self.DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # 获取键值
        if key not in self.cache:
            # 如果键不存在返回-1
            return -1
        # 获取节点
        node = self.cache[key]
        # 将节点移动到头部表示最近访问
        self.moveToHead(node)
        # 返回节点值
        return node.value

    def put(self, key: int, value: int) -> None:
        # 添加或更新键值
        if key in self.cache:
            # 如果键已存在，更新值并移动到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            # 如果是新键，添加新节点到头部
            newNode = self.DLinkedNode(key, value)
            self.cache[key] = newNode
            self.addToHead(newNode)
            # 如果超出容量，移除尾部节点
            if len(self.cache) > self.capacity:
                tail = self.removeTail()
                del self.cache[tail.key]

    def addToHead(self, node: DLinkedNode):
        # 将节点添加到头部
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node: DLinkedNode):
        # 从链表中移除一个节点
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node: DLinkedNode):
        # 将一个节点移动到头部
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self) -> DLinkedNode:
        # 移除尾部节点
        res = self.tail.prev
        self.removeNode(res)
        return res

# 定义LRUCache类（假设已经实现）

# 测试用例
operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
expected_outputs = [None, None, None, 1, None, -1, None, -1, 3, 4]

# 实例化LRUCache和执行操作
obj = None
actual_outputs = []
for op, val in zip(operations, values):
    if op == "LRUCache":
        obj = LRUCache(*val)
        actual_outputs.append(None)
    elif op == "put":
        obj.put(*val)
        actual_outputs.append(None)
    elif op == "get":
        result = obj.get(*val)
        actual_outputs.append(result)

# 检查实际输出是否符合预期输出
assert actual_outputs == expected_outputs, f"Test failed! Expected {expected_outputs}, got {actual_outputs}"

print("Test passed!")
