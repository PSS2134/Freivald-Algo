
import time;
start=time.time()
#defining the order of matrix:
N=int(input("Enter the order of matrix:\n"))
# defining the matrix;
print("input the a matrix:\n")
A = []
for i in range(N):
    sub_matrix=[]
    for j in range(N):
        sub_matrix.append(int(input()))
    A.append(sub_matrix)
print("input the b matrix:\n")
B = []
for i in range(N):
    sub_matrix=[]
    for j in range(N):
        sub_matrix.append(int(input()))
    B.append(sub_matrix)
print("input the c matrix:\n")
C = []
for i in range(N):
    sub_matrix=[]
    for j in range(N):
        sub_matrix.append(int(input()))
    C.append(sub_matrix)


#now compute AB 
AB = [ [0]*N for i in range(N)]
for i in range(N):
     for j in range(N):
          for k in range(N):
            AB[i][j]+=A[i][k]*B[k][j]


#finally we check if AB=C is true or false
count=0
for i in range(0, N) :
       for j in range(0,N):
            if(AB[i][j]-C[i][j]!=0):
                 count=1
                 print("False")
                 break

if(count!=1):
     print("True")

end=time.time()
print(end-start)