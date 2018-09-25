class Queue():
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, item):
        self.stackA.append(item)

    def pop(self):
        if not self.stackB:
            if self.stackA:
                self.stackB.append(self.stackA.pop())
            else:
                return None
        return self.stackB.pop()

if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.pop())


