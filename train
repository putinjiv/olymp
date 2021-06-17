#40.5 0.5 0.6 3 7.5
#20.5 0.5 0.6 3 7.5
def calc(L, a1, a2, v, t):
  t1 = v / a1
  t2 = v / a2
  t3 = (L - t1 * v / 2 - t2 * v / 2) / v
  return t1, t2, t3

numbers = input().split()
for i, el in enumerate(numbers):
  numbers[i] = float(el)

L, a1, a2, v, t = numbers
t1, t2, t3 = calc(L, a1, a2, v, t)
if t3 >= t:
  print(t1 + t2 + t3)
else:
  st = (t ** 2 + 2 * L * (a1 + a2) / a1 / a2) ** 0.5 
  sr = st - t
  u = sr * a1 * a2 / (a1 + a2)
  t1, t2, t3 = calc(L, a1, a2, u, t)
  print(t1 + t2 + t3)
