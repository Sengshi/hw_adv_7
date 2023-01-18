class Stack:

    def __init__(self, items):
        self.items = items

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def isBalanced(text):
    brackets = "()[]{}"
    opening = brackets[::2]
    closing = brackets[1::2]
    check = []
    stack = Stack(check)
    for character in text:
        if character in opening:
            stack.push(opening.index(character))
        elif character in closing:
            if check and check[-1] == closing.index(character):
                stack.pop()
            else:
                return 'Несбалансированно'
    return 'Сбалансированно'


if __name__ == '__main__':
    print(isBalanced('(((([{}]))))'))
    print(isBalanced('[([])((([[[]]])))]{()}'))
    print(isBalanced('{{[()]}}'))
    print(isBalanced('}{}'))
    print(isBalanced('{{[(])]}}'))
    print(isBalanced('[[{())}]'))


