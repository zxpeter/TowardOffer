class Stack():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def add(self, item):
        self.queue1.append(item)

    def pop(self):
        if not self.queue1:
            return None
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.pop()

if __name__ == '__main__':
    s = Stack()
    s.add(1)
    s.add(2)
    s.add(3)
    print(s.pop())
    print(s.pop())







