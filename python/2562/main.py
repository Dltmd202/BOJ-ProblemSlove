
data = []

for i in range(9):
    data.append((int(input()), i + 1))

data.sort(reverse=True)
print(data[0][0])
print(data[0][1])