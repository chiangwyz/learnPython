
# 简介
Kadane算法是一种用于找出一个给定数组的最大子数组和的高效算法。这个算法非常适合于解决"最大子数组和"问题，即在一个整数数组中找出具有最大和的连续子数组。

# 内容
Kadane算法的核心思想是遍历数组，同时跟踪两个变量：当前位置的最大子数组和（max_ending_here）和到目前为止的全局最大子数组和（max_so_far）。
算法的基本步骤如下：

1. 初始化两个变量：max_ending_here 和 max_so_far，都设为数组的第一个元素。
   
2. 遍历数组中的每个元素，对于每个元素执行以下步骤：

  更新 max_ending_here：max_ending_here = max(current_element, max_ending_here + current_element)。这里的关键是比较当前元素自身和当前元素加上之前的最大子数组和，取二者中的较大者作为新的max_ending_here。

  更新 max_so_far：如果 max_ending_here 大于 max_so_far，则将 max_so_far 更新为 max_ending_here 的值。

3. 完成遍历后，max_so_far 即为整个数组的最大子数组和。

Kadane算法的优势在于其高效性——时间复杂度为O(n)，其中n是数组的长度。这种算法非常适用于大型数组，因为它只需要一次遍历即可找到最大子数组和。此外，Kadane算法也很容易理解和实现。

# 示例

举个简单的例子：

假设有数组 [-2, 1, -3, 4, -1, 2, 1, -5, 4]，最大子数组和是 [4, -1, 2, 1]，其和为 6。使用Kadane算法，我们可以有效地找到这个子数组和其和。
