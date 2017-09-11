#给定一个整数数组（下标从 0 到 n-1， n 表示整个数组的规模），请找出该数组中的最长上升连续子序列。（最长上升连续子序列可以定义为从右到左或从左到右的序列。）
给定 [5, 4, 2, 1, 3], 其最长上升连续子序列（LICS）为 [5, 4, 2, 1], 返回 4.

给定 [5, 1, 2, 3, 4], 其最长上升连续子序列（LICS）为 [1, 2, 3, 4], 返回 4.

class Solution:
    """
    @param: A: An array of Integer
    @return: an integer
    [5, 4, 2, 1, 3]
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        length=len(A);
        maxcount=1;#最长上升连续子序列
        countleft=1;#从左到右最长上升连续子序列
        countright=1;#从右到左最长上升连续子序列
        if length==0 or length==1:
            return length;
        for index in range(1,length):
            if A[index]>A[index-1]:
                countleft=countleft+1;
            else:
                countleft=1;
            if countleft>maxcount:
                maxcount=countleft;
            if A[index]<A[index-1]:
                countright=countright+1;
            else:
                countright=1;
            if countright>maxcount:
                maxcount=countright;
        return maxcount
