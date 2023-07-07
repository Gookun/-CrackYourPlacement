class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            index = abs(n) - 1
            if nums[index] > 0: 
                nums[index] = -nums[index]
            else:     
                res.append(abs(n))
        return res
# negative marking technique