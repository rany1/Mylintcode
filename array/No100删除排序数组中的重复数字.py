class Solution:
    """
    删除排序数组中的重复数字
    http://www.lintcode.com/zh-cn/problem/remove-duplicates-from-sorted-array/
    给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。
不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。
给出数组A =[1,1,2]，你的函数应该返回长度2，此时A=[1,2]。
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        pos=0;
        count= 1 if len(A)>0 else 0;

        for index in range(0,len(A)-1):
            if(A[index]==A[index+1]):
                if(pos==0):
                    pos=index+1;
            else:
                count=count+1
                if(pos>0):
                    A[pos]=A[index+1];
                    pos=pos+1;

        return count;
s=Solution();
a=[1,2,3,3,5,5,6];
print(s.removeDuplicates(a)) ;
print(a);
