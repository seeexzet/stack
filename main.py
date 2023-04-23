# is_empty — проверка стека на пустоту. Метод возвращает True или False;
# push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
# pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
# peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
# size — возвращает количество элементов в стеке.

class Stack:

    def __init__(self):
         self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


def balanced(str):
    stack = Stack()
    balance = True
    i = 0
    while i < len(str) and balance:
        symbol = str[i]
        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balance = False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    balance = False
        i += 1
    if balance and stack.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

strings = ['(((([{}]))))',
          '[([])((([[[]]])))]{()}',
           '{{[()]}}',
           '}{}',
           '{{[(])]}}',
           '[[{())}]']

for string in strings:
    if balanced(string):
        print(f'{string} - сбалансированная последовательность')
    else:
        print(f'{string} - несбалансированная последовательность')

