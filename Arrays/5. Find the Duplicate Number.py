"""
TC: O(nlogn)
SC: O(1)
step 1: find the smallest number such that 
the count of numbers less than or equal to it 
is greater than the number itself.

step 2: Apply binary search 
and start with the entire range of numbers [1,n].

step 3: Find the mid-point (cur).

step 4: For cur, count 
how many numbers in the input array 
are less than or equal to it.

If that number strictly exceeds curcurcur, 
then store that as the answer and 
continue to look for a smaller number 
that satisfies the condition by narrowing 
the window to the left [low,cur−1].

Otherwise, narrow down the window 
to the right [cur+1,high].

Step 5: Repeat step 3 until we've exhausted 
the search range (i.e. until lowlowlow > highhighhigh) 
and return the lowest value that met the aforementioned condition.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums)-1
        while low <= high:
            cur =(low + high) // 2
            count = 0
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
        return duplicate