from typing import List
def maxScore(cardPoints: List[int], k: int) -> int:
    l, r = 0, len(cardPoints) - k
    curSumWindow = sum(cardPoints[r:])
    res = curSumWindow
    while r < len(cardPoints):
        curSumWindow += cardPoints[l] - cardPoints[r]
        res = max(curSumWindow,res)
        l += 1
        r += 1
    return res

if __name__ == '__main__':
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    ans = maxScore(cardPoints,k)
    print(ans)