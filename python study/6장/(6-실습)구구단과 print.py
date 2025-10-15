
dan = int(input("몇 단까지 출력할까요? "))

for x in range(1, 10):
    for y in range(1, dan + 1):
        if x == 1:
            print("      %d단\t" % (y),end="")
        else: 
            print("| %d * %d = %2d |" % (y, x, x * y), end="  ")
    print()