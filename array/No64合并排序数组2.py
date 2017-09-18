class Solution:
    """
    http://www.lintcode.com/zh-cn/problem/merge-sorted-array/
    合并两个排序的整数数组A和B变成一个新的数组。

 注意事项

你可以假设A具有足够的空间（A数组的大小大于或等于m+n）去添加B中的元素。
样例
给出 A = [1, 2, 3, empty, empty], B = [4, 5]

合并之后 A 将变成 [1,2,3,4,5]
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        
        pos =m+n-1;
        posA= m-1;
        posB=n-1;
        while posA>=0 and posB>=0:
            if A[posA]>B[posB]:
                A[pos]=A[posA];
                posA=posA-1;
                pos=pos-1;
            else:
                A[pos]=B[posB];
                posB=posB-1;
                pos=pos-1;
        while (posA >= 0) :
            A[pos] = A[posA];
            posA=posA-1;
            pos=pos-1;
        while (posB >= 0) :
            A[pos] = B[posB];
            posB=posB-1;
            pos=pos-1;
