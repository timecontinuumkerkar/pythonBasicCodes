"""10 8 7 6
    5 4 3
     2 1
      0
      """

n = 4
k = 0
for a in range(n):
    k = k + a
m = n + k
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for p in range(i, n):
        print(m, end=" ")
        m = m-1
    print()

