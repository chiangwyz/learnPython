"""
合并k个有序数组，使用数组法。
"""


class Solution:
    def merge_two_sorted_arrays(self, arr1: list[int], arr2: list[int]):
        # 合并两个有序数组
        result = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        # 添加剩余的元素
        result.extend(arr1[i:])
        result.extend(arr2[j:])

        # 返回结果
        return result

    def merge_k_sorted_arrays_sequential(self, arrays: list[list[int]]):
        if not arrays:
            return []
        merged_array = arrays[0]
        for i in range(1, len(arrays)):
            merged_array = self.merge_two_sorted_arrays(merged_array, arrays[i])
        return merged_array


# test
solution = Solution()
arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]

# 再次使用相同的示例输入
print(solution.merge_k_sorted_arrays_sequential(arrays))
