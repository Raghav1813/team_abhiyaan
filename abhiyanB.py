from binascii import a2b_base64
import math

k = int(input('Enter the value of k : '))

m = int(input("Enter the number of rows:"))
n = int(input("Enter the number of columns:"))
  
matrix = []
print("Enter the entries rowwise:")
  
for i in range(m):
    a =[]
    for j in range(n):
         a.append(int(input()))
    matrix.append(a)
  
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end = "\n")
    print()

if k==matrix[i][j]:
    print("True", end = "\n")
    print(i, j, end = "\n")
else:
    print("False", end = "\n")