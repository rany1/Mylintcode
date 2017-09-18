class Solution:
    """
    http://www.lintcode.com/zh-cn/problem/maximum-subarray/
    给定一个整数数组，找到一个具有最大和的子数组，返回其最大和。
    样例
给出数组[−2,2,−3,4,−1,2,1,−5,3]，符合要求的子数组为[4,−1,2,1]，其最大和为6
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        maxTotal=nums[0];
        currSum=nums[0];
        length=len(nums);
        for index in range(1,length):
            currSum = currSum+ nums[index];
            if currSum<nums[index]:
                currSum=nums[index];
            if currSum>maxTotal:
                maxTotal=currSum;
        return  maxTotal;
