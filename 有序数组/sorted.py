from sortedcontainers import SortedSet

ss = SortedSet([5, 1, 3, 3])
print(ss)  # 输出: SortedSet([1, 3, 5])

ss.add(2)
print(ss)  # 输出: SortedSet([1, 2, 3, 5])

ss.discard(3)
print(ss)  # 输出: SortedSet([1, 2, 5])

print(ss[1])  # 输出: 2

print("self defined compared to sorted set!")


# 定义自定义比较逻辑
class CustomSortedSet:
    def __init__(self, iterable=None, key=None):
        self.key = key
        # 如果提供了 key 函数，使用它来创建排序键
        if key:
            self._sorted_set = SortedSet((key(item), item) for item in iterable)
        else:
            self._sorted_set = SortedSet(iterable)

    def __iter__(self):
        if self.key:
            # 返回原始值
            return (item[1] for item in self._sorted_set)
        else:
            return iter(self._sorted_set)

    def add(self, item):
        if self.key:
            self._sorted_set.add((self.key(item), item))
        else:
            self._sorted_set.add(item)

    def __len__(self):
        return len(self._sorted_set)

    def __contains__(self, item):
        if self.key:
            return any(x[1] == item for x in self._sorted_set)
        else:
            return item in self._sorted_set

# 示例数据：一组包含数值的列表
data = [25, 20, 500, 10, 1, 0, -12]

# 创建一个 CustomSortedSet 实例，按绝对值排序
sorted_set = CustomSortedSet(data, key=abs)

# 打印排序后的结果
for item in sorted_set:
    print(item)