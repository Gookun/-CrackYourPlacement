# TC: O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, FirstE in enumerate(nums):
            if i > 0 and FirstE == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                ThreeSum = FirstE + nums[L] + nums[R]
                if ThreeSum > 0:
                    R -= 1
                elif ThreeSum < 0:
                    L += 1
                else:
                    res.append([FirstE, nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return res