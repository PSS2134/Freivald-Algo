
import random
import time;
 
Start_Time=time.time()
# Function to check if ABx = Cx
def freivald(a, b, c,N) :
     
    #   Generate a random vector
    r = [0] * N
     
    for i in range(0, N) :
        r[i] = (int)(random.randrange(509090009) % 2)
 
    #  Now compute B*r for evaluating  expression A * (B*r) - (C*r)
    br = [0] * N
     
    for i in range(0, N) :
        for j in range(0, N) :
            br[i] = br[i] + b[i][j] * r[j]
 
    #   Now compute C*r for evaluating expression A * (B*r) - (C*r)
    cr = [0] * N
    for i in range(0, N) :
        for j in range(0, N) :
            cr[i] = cr[i] + c[i][j] * r[j]
 
    #   Now compute A* (B*r) for evaluating expression A * (B*r) - (C*r)
    axbr = [0] * N
    for i in range(0, N) :
        for j in range(0, N) :
            axbr[i] = axbr[i] + a[i][j] * br[j]
 
    #   Finally check if value of expression A * (B*r) - (C*r) is 0 or not
    for i in range(0, N) :
        if (axbr[i] - cr[i] != 0) :
            return False
             
    return True
 
#   Runs k iterations Freivald. The value of k determines accuracy. 
#   Higher value means higher accuracy.
def isProduct(a, b, c, k) :
     
    for i in range(0, k) :
        if (freivald(a, b, c,N) == False) :
            return False
    return True
#defining the order of matrix:
N=int(input("Enter the order of matrix:\n"))
# defining the matrix;
print("input the a matrix:\n")
a = []
for i in range(N):
    sub_matrix=[]
    for j in range(N):
        sub_matrix.append(int(input()))
    a.append(sub_matrix)
print("input the b matrix:\n")
b = []
for i in range(N):
    sub_matrix=[]
    for j in range(N):
        sub_matrix.append(int(input()))
    b.append(sub_matrix)
print("input the c matrix:\n")
c = []
for i in range(N):
    sub_matrix=[]
    for j in range(N):
        sub_matrix.append(int(input()))
    c.append(sub_matrix)
print("input the k value:\n")
k=int(input())

#printing the final result!!!
print(isProduct(a,b,c,k))
End_Time=time.time()
print(End_Time-Start_Time)
