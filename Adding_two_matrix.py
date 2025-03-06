# matrix addition by basic method
r1 =[12,45,88]
r2 =[45,85,95]
r3 =[65,45,1]

a1 =[15,45,98]
a2 =[45,85,95]
a3 =[65,45,1]

A=[]
A.append(r1)
A.append(r2)
A.append(r3)

B=[]
B.append(a1)
B.append(a2)
B.append(a3)

C= [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(B)):
        C[i][j] = A[i][j] + B[i][j]
print(C)