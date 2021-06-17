a, c = map(int,input().split())
d = a - c
g = []
for i in range(1, d + 1):
  if d % i == 0 and i > c:
    g.append(i)
print(g)
