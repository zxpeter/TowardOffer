Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        res = []
        m = len(matrix)  
        n = len(matrix[0])
        l, r, u, d = 0, n-1, 0, m-1
        while l < r and u < d:
            for j in range(l, r):
                res.append(matrix[u][j])
            for i in range(u, d):
                res.append(matrix[i][r])
            for j in range(r, l, -1):
                res.append(matrix[d][j])
            for i in range(d, u, -1):
                res.append(matrix[i][l])
            l += 1
            r -= 1
            u += 1
            d -= 1
        # print(res)
        if l == r:
            for i in range(u, d+1):
                res.append(matrix[i][r])
        elif u==d:
            for j in range(l, r+1):
                res.append(matrix[u][j])
        return res   
        
59. Spiral Matrix II        
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
class Solution(object):
    def generateMatrix(self, n):
        result = [[0 for i in range(n)] for j in range(n)]
        coord = [[(i,j) for j in range(n)] for i in range(n)]
        count = 1
        while coord:
            for x, y in coord.pop(0):
                result[x][y] = count
                count += 1
            print(coord)
            coord = zip(*coord)[::-1]
            print(coord)
        return result
        
885. Spiral Matrix III     
    def spiralMatrixIII(self, R, C, r, c):
        res = [[r, c]]
        x, y, n, i = 0, 1, 0, 0
        while len(res) < R * C:
            r, c, i = r + x, c + y, i + 1
            if 0 <= r < R and 0 <= c < C:
                res.append([r, c])
            if i == n / 2 + 1:
                x, y, n, i = y, -x, n + 1, 0
        return res
       
# 对角线打印matrix
    if not matrix:
        return []
    row = len(matrix)
    col = len(matrix[0])
    col2 = col
    result = []
    for i in range(row):
        for j in range(col2 - 1, -1, -1): #j倒序遍历
            lst = []
            i1,j1 = i,j #i1,j1用于方便同一对角线元素的添加，否则改变i,j影响开头元素的选择
            while i1 <= row - 1 and j1 <= col - 1:
                lst.append(matrix[i1][j1])
                j1 += 1
                i1 += 1
            result.append(lst)
            if i == 0 and j == 0:#当遍历完(0,0)开头的一条对角线后，让j固定为0
                col2 = 1
    return('the result is: %s'%result,'end')



