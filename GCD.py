def gcd(a, b):
    if a > b:
        greater = a
        smaller = b
    else:
        greater = b
        smaller = a
    r = greater % smaller
    if r == 0:
        print(smaller)
    else:
        gcd(smaller, r)


gcd(66528, 52920)
