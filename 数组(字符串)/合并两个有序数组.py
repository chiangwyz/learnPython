"""
这种解法非常巧妙，所以记录下来，从后往前合并，而且考虑了m=0或者n=0的情况
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 从后向前合并，先填充nums1的后半部分
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        # 如果nums2还有剩余，直接复制到nums1的前面，nums1剩余的部分不需要操作，因为它们已经在正确的位置
        nums1[:n] = nums2[:n]
        
