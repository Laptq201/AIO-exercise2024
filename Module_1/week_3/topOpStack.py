class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.stack = []

    def is_full(self):
        return len(self.stack) == self.__capacity

    def push(self, value):
        self.stack = list([value,]) + self.stack

    def top(self):
        return self.stack[0]


def main():
    stack = MyStack(capacity=5)
    stack.push(1)
    assert stack.is_full() == False
    stack.push(2)
    print(stack.top())


if __name__ == '__main__':
    main()
