def get_fabric_square(matr, i, j):
  s = matr[i-1][j-1] + matr[i-1][j] + matr[i-1][j+1] + matr[i][j-1] + matr[i][j] + matr[i][j+1] + matr[i+1][j-1] + matr[i+1][j] + matr[i+1][j+1]
  return s


m, n = map(int,input().split())
matr = []
for i in range(m):
  matr.append(list(map(int,input().split())))
  assert len(matr[i]) == n
  
for i in range(m):
  print(matr[i])
x = []
for i in range(1, m-1):
  for j in range(1, n-1):
    x.append(get_fabric_square(matr, i, j))
    
print(min(x))
