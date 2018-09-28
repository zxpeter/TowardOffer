def Fibonacci(n):
    a0 = 1
    a1 = 1
    fn = 0
    if n < 2:
        return 1
    for i in range(1, n):
        print(i)
        fn = a0 + a1
        a1 = fn
        a0 = a1
    return fn

if __name__ == '__main__':
    print(Fibonacci(3))



