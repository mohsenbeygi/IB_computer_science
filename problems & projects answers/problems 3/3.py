n = int(input())

is_prime = True

for number in range(2, n):
    if n % number == 0:
        is_prime = False

if is_prime:
    print("yes")
else:
    print("no")