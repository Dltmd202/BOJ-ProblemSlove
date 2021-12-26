import re

s = input()

answer =''
is_tag = False
word =''
for char in s:
    if char == '<':
        is_tag = True
        answer += word[::-1] +'<'
        word =''

    elif char == '>':
        is_tag = False
        answer += '>'

    elif char == ' ':
        if is_tag:
            answer += char
        else:
            answer += word[::-1] + ' '
            word=''
    else:
        if is_tag:
            answer += char
        else:
            word += char
answer += word[::-1]
print(answer)