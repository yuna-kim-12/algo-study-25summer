T = int(input())
for _ in range(T):
    brackets = input()
    stack = []
    is_answered = False
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                print("NO")
                is_answered = True
                break
            stack.pop()

    if not is_answered:
        if stack:
            print("NO")
        else:
            print("YES")
