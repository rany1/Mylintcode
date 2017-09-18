class Solution:
    """
    不同的路径 II
    http://www.lintcode.com/zh-cn/problem/unique-paths-ii/
    "不同的路径" 的跟进问题：
现在考虑网格中有障碍物，那样将会有多少条不同的路径？
网格中的障碍和空位置分别用 1 和 0 来表示。
如下所示在3x3的网格中有一个障碍物：

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
    @param: obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        index=len(obstacleGrid);
        jndex =len(obstacleGrid[0]);
        count =0;
        changei=False;
        changej=False;
        if (obstacleGrid[0][0]==1):
            return count
        for i in range(0,index):
            for j in range(0,jndex):

                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
                    if i==0:
                        changei=True;
                    if j==0:
                        changej=True;
                else:
                    if changei==True and i==0:
                        obstacleGrid[i][j]=0;
                        continue;
                    if changej==True and j==0:
                        obstacleGrid[i][j]=0;
                        continue;
                    if i==0 or j==0:
                        obstacleGrid[i][j]=1;
                    else:
                        obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1];
        print(obstacleGrid)
        return obstacleGrid[index-1][jndex-1];
