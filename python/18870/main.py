n = int(input())
data = list(map(int, input().split()))
set_data = set(data)
sorted_set_data = sorted(list(set_data))
hash_map = dict()
hash_map[sorted_set_data[0]] = 0
for i in range(1, len(sorted_set_data)):
    hash_map[sorted_set_data[i]] = hash_map[sorted_set_data[i - 1]] + 1

print(' '.join(str(hash_map[d]) for d in data))
