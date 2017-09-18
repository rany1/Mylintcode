
class Solution:
    """
    http://www.lintcode.com/zh-cn/problem/partition-array/
    给出一个整数数组 nums 和一个整数 k。划分数组（即移动数组 nums 中的元素），使得：

所有小于k的元素移到左边
所有大于等于k的元素移到右边
返回数组划分的位置，即数组中第一个位置 i，满足 nums[i] 大于等于 k。
给出数组 nums = [3,2,2,1] 和 k = 2，返回 1.
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        count=len(nums);
        arr=[k];
        result=0;
        for index in range(0,count):
            if nums[index]>=k:#右边
               arr.append(nums[index]);
            else:#左边
                arr.insert(0,nums[index]);
                result=result+1;
        for index in range(0,count):
            nums[index]=arr[index];
        return  result;
