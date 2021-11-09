n = int(input())
# answer = n!
answer = 1
for i in range(1, n + 1):
    answer *= i
print(answer)