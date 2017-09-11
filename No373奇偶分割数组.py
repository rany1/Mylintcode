#分割一个整数数组，使得奇数在前偶数在后。给定 [1, 2, 3, 4]，返回 [1, 3, 2, 4]。
class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        length=len(nums);
        posi=0;
        posj=length-1;
        while posi<posj:
            while nums[posi] %2==1:
                posi=posi+1;
            while nums[posj]%2==0:
                posj=posj-1;
            if posi<posj:
                temp= nums[posi];
                nums[posi]=nums[posj];
                nums[posj]=temp;
                posi=posi+1;
                posj=posj-1;
