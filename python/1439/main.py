
data = input()
cnt = 1
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        cnt += 1

print(cnt // 2)