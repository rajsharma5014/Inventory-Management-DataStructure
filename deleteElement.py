#program to delete an element from a specified position in an array
arr=[]
num=int(input("Enter the no. of element of Array:"))

for i in range(num):
    element=int(input("Enter the element of array:"))
    arr.append(element)

position=int(input("Enter the postion of element to delete:"))
print("array before deletion:",arr)
arr.pop(position)
print("Array After deletion:",arr)
