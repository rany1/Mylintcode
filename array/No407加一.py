class Solution:
    """
    http://www.lintcode.com/zh-cn/problem/plus-one/
    给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。
    该数字按照大小进行排列，最大的数在列表的最前面。
    给定 [1,2,3] 表示 123, 返回 [1,2,4].
    给定 [9,9,9] 表示 999, 返回 [1,0,0,0].
    @param: digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        arr = [0] * (len(digits)+1);
        addnumber=1;
        for index in range(len(digits)-1,-1,-1):
            result=digits[index]+addnumber;
            if result>9:
                addnumber=1;
                digits[index]=0;
                arr[index+1]=0;
            else:
                digits[index]=result;
                arr[index+1]= result;
                addnumber=0;
        if addnumber>0:
            arr[0]=1;
        if arr[0]==0:
            return arr[1:];
        return arr;
