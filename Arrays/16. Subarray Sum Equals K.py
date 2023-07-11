from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    res = 0
    curSum = 0
    PrefixSums = { 0 : 1}
    for n in nums:
        curSum += n
        diff = curSum - k
        res += PrefixSums.get(diff, 0)
        PrefixSums[curSum] = 1 + PrefixSums.get(curSum, 0)
    return res



if __name__ == '__main__':
    nums = [3,1,2,4]
    k = 6
    ans = subarraySum(nums,k)
    print("The number of subarrays is:", ans)       