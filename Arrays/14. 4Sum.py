#Brute force approach
# TC : n^4 
#SC : O(2 * no. of the quadruplets) as we are using a set data structure and a list to store the quads.
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        st = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1, len(nums)):
                        sum = nums[i] + nums[j]
                        sum += nums[k]
                        sum += nums[l]
                        if sum == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            st.add(tuple(temp))
        ans = [list(x) for x in st]
        return ans
#optimal solution
#n^3
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, quad = [], []
        nums.sort()
        # generic solution k amount of sums
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target - nums[i])
                    quad.pop()
                return
            # base case, two sum
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l] , nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        kSum(4, 0, target)
        return res