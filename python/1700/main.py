
n, k = map(int, input().split())
data = list(map(int, input().split()))
plug = []
cnt = 0

for i in range(k):
    if data[i] in plug:
        continue
    elif len(plug) < n:
        plug.append(data[i])
        continue
    near_idx = -1
    for j in range(n):
        try:
            if near_idx < data[i + 1:].index(plug[j]):
                near_idx = data[i + 1:].index(plug[j])
                idx = j
        except:
            near_idx = -1
            idx = j
            break
    plug[idx] = data[i]
    cnt += 1
print(cnt)
