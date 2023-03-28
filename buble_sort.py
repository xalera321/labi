n = int(input('Введите кол-во элементов в списке'))
A = [int(input()) for i in range(n)]
for i in range(n):
    for j in range((n-1)):
      if A[j]>A[j+1]:
          A[j],A[j+1] = A[j+1],A[j]
print(A)    

n = int(input('Введите кол-во элементов в списке'))
A = [int(input()) for i in range(n)]
for i in range(n):
    for j in range((n-1)-i):
      if A[j]>A[j+1]:
          A[j],A[j+1] = A[j+1],A[j]
print(A)    

n = int(input('Введите кол-во элементов в списке'))
A = [int(input()) for i in range(n)]
for i in range(n-1):
    for j in range((n-1)-i):
      if A[j]>A[j+1]:
          A[j],A[j+1] = A[j+1],A[j]
print(A)
