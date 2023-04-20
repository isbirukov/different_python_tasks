n = int(input())
cnt_simple = 0
for i in range(n + 1, 2 * n):
    if i % 2 != 0:
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                cnt += 1
        if cnt == 1:
            cnt_simple += 1

print(cnt_simple)