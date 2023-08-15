shivakumar=[]
#print(type(shivakumar))
 
shivakumar=list()
#print(type(shivakumar))


shivakumar=['hai',347,True,1,1,12,2,2,2,]
#print(len(shivakumar))

shiva=[4,5,4,6,3,54,7,3,3,4,6]
#print(shiva[1])
#print(shiva[-1]) 
#print(shiva[7])
#print(shiva[0:7]) 
#print(shiva[0:8:4])
#print(shiva[8:0:-2])




kumar=[33,56,73,68,94,1,4,5,6,]
#print(kumar[:]) 
#print(kumar[:3])
#print(kumar[5:])
#print(kumar[::])
#print(kumar[:-1])
#print(kumar[-1:])
#print(kumar[::-1])


satya=[77,44,53,78,23,41,5,89,14]
satya.extend([73,47,37,24,15,1])
#print(satya)


kumar=[4,77,233,24,55,26,46,2,454]
# variable_name.method()
#kumar.append("satya")
#kumar.extend([53,23,46,78,77,43,35])
#print(kumar)


raj=[3,6,8,33,7,3,88,1,2,7,9,837]
#print(raj.count(7))
raj.clear()
# print(raj)



satya=[35,66,22,6,77,233,6,7,88,9]
k=satya
#print(k)
satya.append(123)
#print(k)

shiva=[23,67,45,68,93,55,33,76,33]
#print(shiva.index(33))


shiva=[23,67,45,68,93,55,33,76,33]
shiva.insert(0,"673674")
#print(shiva)

shiva=[23,67,45,68,93,55,33,76,33]
#shiva.pop(0)
#shiva.remove(33)
#print(shiva)


shiva=[23,67,45,68,93,55,33,76,33]
shiva.reverse()
#print(shiva)


shiva=[23,67,45,68,93,55,33,76,33]
shiva.sort() #ascending order
#print(shiva)

shiva=[23,67,45,68,93,55,33,76,33]
shiva.sort(reverse=True) #decending order
#print(shiva)  


l=[1,2,3,6,7,55,77,3,6,8,3,]
#print(l.index(3))


#Index
#l=[2,4,2,5,6,7,2,44,56,44,66,78,89]
#for i in range(len(l)):
    #if l[i]==44:
        #print(2)

#print([i**2 for i in [1 ,2, 3,4,5,6,7]])


c=[]
for i in[1,2,3,4,5,6,7]:
        c.append(i*3)
#print(c)



#List Comprehension
#print([i if i%2==0 else "ODD" for i in range(0,20)])
 

#print([num+2 for num in [1,2,3,4,5,6,7,8,9]])



#print([word[0] for word in ['apple','grapes','bananna','mango']])

#Create a list of positive numbers in list
#print([num for num in [-2,-1,0,1,2,3,4] if num > 0])



a=[-2,-1,0,1,2,3,4,5,6,7]
#print(-1 in a)

a=[-2,-1,0,1,2,3,4,5,6,7]
#print(-11 not in a)

a=[-2,-1,0,1,2,3,4]
a2=[-2,-1,0,1,2,3,4]
#print(id(a)==id(a2))

a=1
a2=1
#print(a is a2)


# Removing Multiple Elements in List
### By using list comprehension

num = [1,2,3,4,5,6,7,7,7,7,8,9]
num_to_remove =[7,1]
# Creating new list using list comprehension
num = [i for i in num if i not  in num_to_remove]
#print(num)


#Creating an empty  list 
lst = []
# Number of elements as input
n = int(input("Enter number of elements :"))
# iterating till the range 
for i in range(0,n):
    ele = int(input())
    # adding element
    lst.append(ele)
#print(lst)        


l=[1,2,3,4,5,6,7,7,78,5,3,4,5,33]
print(["adult" for i in l if i==18])
for i in l:
    if i==18:
#print("adult")   
                                      

                                      