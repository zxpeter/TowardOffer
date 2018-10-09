horizontal lines (same rows) are handled because we don't even try to put queens into the same row. In every DFS call we choose the next row, and on that row, we are trying to find a place where the queen can be.

So p is a row number, and q is a column number. And as you can see we choose p as:

p = len(queens)
So it is always new one.

P.S. We check vertical line (same column) by q not in queens.
def solveNQueens(self, n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
    result = []
    DFS([],[],[])
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
