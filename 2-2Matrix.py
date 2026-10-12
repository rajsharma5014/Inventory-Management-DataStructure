# Create two 3-3 matrix and perform arithmethic operation

A=[]
for i in range(3):
    row=[]
    for j in range(3):
        value=int(input("Enter the Element of Matrix A:"))
        row.append(value)
    A.append(row) 
# Display Matrix A
print("Matrix A=")
for i in A:
    print(i)
B=[]
for i in range(3):
    row=[]
    for j in range(3):
        value=int(input("Enter the element of Matrix B:"))
        row.append(value)
    B.append(row)
# Display matrix B
print("Matrix B=")
for i in B:
    print(i)
# Multipplication
M=[]
for i in range(3):
    row=[]
    for j in range(3):
        total=0
        for k in range(3):
            total+=A[i][k]*B[k][j]
        row.append(total)
    M.append(row)
# display Multiplication Matrix
print("Multiplication of Matrix")
print("Matrix M=")
for i in M:
    print(i)

    
