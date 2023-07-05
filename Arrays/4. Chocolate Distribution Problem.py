class Solution:

    def findMinDiff(self, A,N,M):

    # if there are no chocolates or number
    # of students is 0
        if (M == 0 or N == 0):
            return 0
            
        A.sort()
    # Number of students cannot be more than
    # number of packets
        if(N < M):
            return -1
        # Largest number of chocolates
        minDiff = A[N-1] - A[0]
    # Find the subarray of size m such that
    # difference between last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.
        for i in range(len(A) - M + 1):
            minDiff = min(minDiff,  A[i + M - 1] - A[i])
        return minDiff
