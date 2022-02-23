total=5
n=total-1
for a in range(0, total):
    for b in range(0, n):
        print(end=" ")
    n = n - 1
    for b in range(0, a + 1):
        print("* ", end="")
    print(" ")
