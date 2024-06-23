class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        self.__stack = list([value,]) + self.__stack


def main():
    stack = MyStack(capacity=5)
    stack.push(1)
    assert stack.is_full() == False
    stack.push(2)
    print(stack.is_full())


if __name__ == '__main__':
    main()
