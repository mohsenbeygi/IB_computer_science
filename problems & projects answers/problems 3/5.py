# solution 1 
n = int(input())

count = 0

for number in range(1, n + 1):
    if number % 3 == 0:
        count += 1

print(count)

# solution 2
n = int(input())
print(n // 3)