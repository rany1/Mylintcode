class Solution:
    """
    http://www.lintcode.com/zh-cn/problem/median/
    给定一个未排序的整数数组，找到其中位数。

中位数是排序后数组的中间值，如果数组的个数是偶数个，则返回排序后数组的第N/2个数。
给出数组[4, 5, 1, 2, 3]， 返回 3

给出数组[7, 9, 4, 5]，返回 5
    @param: nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        # write your code here
        length=len(nums);
        count= int((length-1)/2);
        for i in range (length-1,int((length-1)/2-1),-1):
            
            for j in range(length-1,int(length-i-1),-1):
                if nums[j]<nums[j-1]:
                    temp=nums[j];
                    nums[j]=nums[j-1];
                    nums[j-1]=temp;
        return  nums[int((length-1)/2)];
