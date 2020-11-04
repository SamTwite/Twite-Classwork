import sys
lines = sys.stdin.readlines()
T = int(lines[0])
# temp = 0
for t in range(T):
    (N, B) = map(int, lines[2 * t + 1].strip().split(" "))
    As = list(map(int, lines[2*t+2].strip().split(" ")))
    As.sort()
    c = 0
    total = 0
    while c < N and total + As[c] <= B:
        total += As[c]
        c += 1
    print("Case #{}: {}".format(t+1, c))
