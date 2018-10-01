def BST_post(li):
    if not li:
        return False
    root = li[-1]
    i = 0
    for i in range(0, len(li)-1):
        if li[i] > root:
            break
    for j in range(i, len(li)-1):
        if li[j] < root:
            return False
    left = True
    if i > 0:
        left = BST_post(li[0:i])
    right = True
    if i < len(li)-1:
        right = BST_post(li[i:-1])
    return left and right


if __name__ == '__main__':
    li = [7,4,6,5]
    li2 = [5,7,6,9,11,10,8]
    print(BST_post(li2))
    print(BST_post(li))


