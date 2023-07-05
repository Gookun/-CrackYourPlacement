"""
TC: O(N)
SC: O(1)
dutch national flag algorithm variation
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        p = 0
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1