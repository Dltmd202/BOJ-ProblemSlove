

document = input()
pattern = input()
i = 0
answer = 0
while i <= len(document) - len(pattern):
    if document[i: i + len(pattern)] == pattern:
        answer += 1
        i += len(pattern)
    else:
        i += 1

print(answer)