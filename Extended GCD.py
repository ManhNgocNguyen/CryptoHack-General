def find_inverse(a, b):
    if a > b:
        greater = a
        smaller = b
    else:
        greater = b
        smaller = a
    t = int(greater / smaller)
    r = greater % smaller
    print(str(greater) + " = " + str(t) + " * " + str(smaller) + " + " + str(r))
    print(str(r) + " = " + "-" + str(t) + " * " + str(smaller) + " + " + str(greater))
    if r == 0:
        print("End")
    else:
        find_inverse(smaller, r)


find_inverse(26513, 32321)
