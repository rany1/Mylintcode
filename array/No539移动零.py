class Solution:
    """
    http://www.lintcode.com/zh-cn/problem/move-zeroes/
    给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序
    注意事项
        1.必须在原数组上操作
        2.最小化操作数
    例：给出 nums = [0, 1, 0, 3, 12], 调用函数之后, nums = [1, 3, 12, 0, 0].
    @param: nums: an integer array
    @return:
    """
    def moveZeroes(self, nums):
        # write your code here
        pos=-1;
        for index in range(0,len(nums)):
            if nums[index]==0:
                if pos==-1:
                    pos=index;
            else:
                if pos>=0:
                    nums[pos]=nums[index];
                    nums[index]=0;
                    pos=pos+1;
