#program to create an array of N integers entered by the user and display its elements.
arr=[]
num=int(input("Enter the no. Element in Array:"))

for i in range(num):
    element=int(input("Enter THe element of Array:"))
    arr.append(element)

print("Array of Element are:",arr)

