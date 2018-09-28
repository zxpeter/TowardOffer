#可能旋转过
#也可能没有旋转
#可能有重复数字

def find_min(li):
    left = 0
    right = len(li) - 1
    mid = left
    while li[left] >= li[right]:
        if right - left == 1:
            mid = right # !!!! 两个指针分别从头尾向中间走
            break
        mid = (right + left) // 2 # 两个下标加起来除以二结果是中间的下标！！！！无知

        if li[mid] == li[left] and li[mid] == li[right]:
            return MinOrder(li, left, right)

        if li[mid] > li[left]:
            left = mid
        else:
            right = mid
    return li[mid]

def MinOrder(li, left, right):
    res = li[left]
    for i in range(left, right):
        if li[i] < res:
            res = li[i]
    return res


def find_num(li, num):
    left = 0
    right = len(li) - 1
    while left < right:
        mid = (right + left) // 2
        if li[mid] == num:
            return mid
        elif li[mid] < li[right]:
            if num > li[mid] and num <= li[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if num < li[mid] and num >= li[left]:
                right = mid - 1
            else:
                left = mid + 1


if __name__ == '__main__':

    li = [1, 2, 3, 4, 5]
    li = [3, 4, 5, 1, 2]
    li = [4, 5, 1, 2, 3]
    li = [5, 1, 2, 3, 4]
    # li = [1, 0, 1, 1, 1]
    # li = [1, 1, 1, 0, 1]
    res = find_min(li)
    # print(res)
    print(find_num(li, 5))


