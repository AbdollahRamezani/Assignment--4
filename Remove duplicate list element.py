n=int(input("please enter number of element list : "))
list1=[]
for i in range (n):
    element=input("enter List elements : ")
    list1.append(element)
    i-=n
mylist = list(dict.fromkeys(list1))
print(mylist)