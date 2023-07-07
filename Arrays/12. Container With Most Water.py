# two pointer approach
# TC: O(N)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxA = 0
        while L <= R:
            area = (R - L) * min(height[L], height[R])
            maxA = max(maxA, area)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return maxA