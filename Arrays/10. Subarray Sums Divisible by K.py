class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixMod, result = 0, 0
        modGroups = [0] * k
        modGroups[0] = 1
        for num in nums:
            prefixMod = (prefixMod + num) % k
            '''
            prefixMod calculation is simplified, 
            as remainders modulo k > 0 are always 
            positive in Python.
            '''
            result += modGroups[prefixMod]
            modGroups[prefixMod] += 1
        return result
'''
Algorithm
1) Initialize an integer prefixMod = 0 to store the remainder when the 
sum of the elements of a array till the current index when divided by k, 
and the answer variable result = 0 to store the number of subarrays divisible by k.
2) Initialize an array, modGroups[k] where modGroup[R] stores the number of subarrays 
encountered with the sum of elements having a remainder R when divided by k. Set modGroups[0] = 1.
3) Iterate over all the elements of num.For each index i, 
compute the prefix modulo as prefixMod = (prefixMod + num[i] % k + k) % k. 
We take modulo twice in (prefixMod + num[i] % k + k) % k to remove negative numbers since num[i] can be a negative number 
and the sum prefixMod + nums[i] % k can turn out to be negative. To remove the negative number we add k to make it positive and then takes its modulo again with k.
Add the number of subarrays encountered till now that have the same remainder to the result: result = result + modGroups[prefixMod].
In the end, we include the remainder of the subarray in the modGroups, i.e., modGroups[prefixMod] = modGroups[prefixMod] + 1 for future matches.
Return result.
'''