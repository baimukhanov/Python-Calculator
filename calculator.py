expression = input("Enter your expression: ")

def tokenize(expr):
    token = []
    num = ''

    for i in expr:
        if i.isdigit() or '.' in i:
            num += i
        else:
            if num != '':
                token.append(num)
                num = ''
            if i in '+-/*()^':
                token.append(i)
    if num != '':
        token.append(num)
    return token

def precedence(op):
    if op in '+-':
        return 1
    if op in '*/':
        return 2
    if op == '^':
        return 3
    return 0

def calculate(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '/':
        return a / b
    if op == '*':
        return a * b
    if op == '^':
        return a ** b
    return None

def execution(token):
    nums = []
    ops = []
    i = 0

    while i < len(token):
        t = token[i]

        if t == '(':
            ops.append(t)
        if t.isdigit():
            nums.append(float(t))
        if t == ')':
            while ops and ops[-1] != '(':
                b = nums.pop()
                a = nums.pop()
                op = ops.pop()
                nums.append(calculate(a, b, op))
            ops.pop()
        if t in '+-/*^':
            while ops and precedence(ops[-1]) >= precedence(t):
                b = nums.pop()
                a = nums.pop()
                op = ops.pop()
                nums.append(calculate(a, b, op))
            ops.append(t)
        i += 1

    while ops:
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        nums.append(calculate(a, b, op))

    return nums[0]

print(execution(tokenize(expression)))