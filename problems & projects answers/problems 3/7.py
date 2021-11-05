# lcm: least common multiple
# gcd: greatest common divisor
a = int(input())
b = int(input())

for i in range(1, b):
    if a % i == 0 and b % i == 0:
        gcd = i

lcm = a * b // gcd

print(lcm)

print(gcd)
