class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            #check if the values are unique
            if nums[r] != nums[r-1]:
            #pushing the value to its correct space
                nums[l] = nums[r]
            #increamenting pointer to new place to place the new value
                l +=1
        #returning the position from which there will be duplicates
        return l
