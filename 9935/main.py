
s = input()
bomb = input()
stack = []
last_char = bomb[-1]

for char in s:
    stack.append(char)
    if char == last_char and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]





if stack:
    print(''.join(stack))
else:
    print("FRULA")


