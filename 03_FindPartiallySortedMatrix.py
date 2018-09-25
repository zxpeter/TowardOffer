# array and 2d array

class solution():
    def find(self, matrix, num):
        row, col = 0, len(matrix[0])-1
        while matrix and row >= 0 and col >= 0:
            last = matrix[row][col]
            if num == last:
                return True
            elif num < last:
                col -= 1
            else:
                row += 1
        return False


if __name__ == '__main__':
    sol = solution()
    num = 6
    matrix = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    # print(len(matrix))
    print(sol.find(matrix, num))
