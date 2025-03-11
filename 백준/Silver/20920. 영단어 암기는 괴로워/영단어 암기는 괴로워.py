from collections import Counter
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    words = list(filter(lambda x: len(x) >= m, list(input().strip() for _ in range(n))))
    words_counter = Counter(words)

    sorted_words = sorted(list(set(words)), key=lambda x: (-words_counter[x], -len(x), x))
    print("\n".join(sorted_words))
