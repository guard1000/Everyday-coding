infix = ['2', '+', '3', '*', '4']
postfix = []
stack = []
operator = ['*', '/', '+', '-']
bracket = ['(', ')']

def is_number(x):
    if x not in operator and x not in bracket:
        return True
    else:
        return False

def pref(x):
    if x is '*' or x is '/':
        return 1
    elif x is '+' or x is '-':
        return 0

for c in infix:
    if is_number(c):
        postfix.append(c)
    elif c in operator:
        p = pref(c)
        while len(stack) > 0:
            top = stack[-1]
            if pref(top) <= p:
                break
            postfix.append(stack.pop())
        stack.append(c)

    elif c == '(':
        stack.append(c)
    elif c == ')':
        while True:
            x = stack.pop()
            if x == '(':
                break
            postfix.append(x)

while len(stack) > 0:
    postfix.append(stack.pop())

print(postfix)
i = 0
while len(postfix) > 1:
    if postfix[i] == '+':
        postfix[i] = int(postfix[i-2]) + int(postfix[i-1])
        postfix.pop(i-1)
        i = i-1
        postfix.pop(i-1)
        i = i-1
    elif postfix[i] == '-':
        postfix[i-2] = int(postfix[i-2]) - int(postfix[i-1])
        postfix.pop(i-1)
        postfix.pop(i-1)
        i = i - 1
    elif postfix[i] == '*':
        postfix[i-2] = int(postfix[i-2]) * int(postfix[i-1])
        postfix.pop(i-1)
        postfix.pop(i-1)
        i = i - 1
    elif postfix[i] == '/':
        postfix[i-2] = int(postfix[i-2]) / int(postfix[i-1])
        postfix.pop(i-1)
        postfix.pop(i-1)
        i = i - 1
    i = i+1


print(postfix)