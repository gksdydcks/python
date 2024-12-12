            #실습 4  스택
import sys
n = int(sys.stdin.readline())

stack=[]

def push(num):
    stack.append(num)

def pop():
    if len(stack)==0:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack)==0:
        print(1)
    else:
        print(0)

def top():
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])

for _ in range(n):
    command = sys.stdin.readline().split()
    cmd = command[0]

    if cmd == 'push':
        push(command[1])
    elif cmd == 'pop':
        pop()
    elif cmd == 'size':
        size()
    elif cmd == 'empty':
        empty()
    elif cmd == 'top':
        top()

    # match cmd:
    #     case 'push':
    #         push(command[1])
    #     case 'pop':
    #         pop()
    #     case 'size':
    #         size()
    #     case 'empty':
    #         empty()
    #     case 'top':
    #         top()