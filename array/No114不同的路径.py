class Solution:
    """
    不同的路径
    http://www.lintcode.com/zh-cn/problem/unique-paths/
    有一个机器人的位于一个 m × n 个网格左上角。
机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角。
问有多少条不同的路径？n和m均不超过100
给出 m = 3 和 n = 3, 返回 6.
给出 m = 4 和 n = 5, 返回 35.
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        arr=[[0 for i in range(n)] for i in range(m)];
        for i in range(0,m):
            for j in range(0,n):
                if i==0 or j==0:
                    arr[i][j]=1;
                else:
                    arr[i][j]=arr[i-1][j]+arr[i][j-1];
        return arr[m-1][n-1];

s=Solution();
print(s.uniquePaths(2,62))
