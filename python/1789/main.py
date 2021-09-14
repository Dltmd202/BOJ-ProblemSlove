n = int(input())
s = 0
idx = 1
while True:
    s += idx
    if n < s:
        break
    idx += 1
print(idx - 1)