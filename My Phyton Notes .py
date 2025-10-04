array=[]
array.append(1)
array.append(2)
array.append(3)
array.append(4)
array.append(5)
print(array)

flower=[]
for i in range(1,51):
    flower.append(i)
for i in range(0,50):
    print(flower[i])

flower=[]
for i in  range(1,1001):
    flower.append(i)
    print(flower[i-1])

for i in range(1,51):
     print(i)
while(i<6):
    print(i)
    i+=1
    i=i+1
    i=i+2
    
j=1
while(j<51):
    print(j)
    j=j+2
    
k=0
while(k<51):
    print(k)
    k=k+2
    
    
n=int(input("Enter a number"))
if n%2==0:
    print("it is an even number")
else:
    print("it is an odd number")


#list=[1,2,2,3,3,4,4,5,5,6,8,9,9,7]
#print(list)
#rev=tuple(list)
#print(rev)


#Mutable ->list
#Immutable ->tuple

list=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
k=set(list)
print(k)
k.add(12)
k.add(12)
print(k)

#sets are mutable
#sets has unique elements

dict={
    "model":"1st Model",
    "year":2021,
    "age":18
}
#print(type(dict))
print(dict['model'])
dict['city']='Hyderabad'
print(dict)

#the functions concept
def mom(a,b):
    print(a+b)
a=10
b=20
mom(a,b)
mom(5,6)
mom(a,b)
mom(5,6)
#to print directly

def mom(a,b):
    return a+b
a=10
b=20
c=mom(a,b)
print(c)
d=mom(5,6)
print(d)
e=mom(a,b)
print(e)
f=mom(5,6)
print(f)
to print internally one by one

list=[1,2,3,4,5,6,7,8,9]
print(list[4:])
print(list[1::2])

def mom(a,b):
    print(a+b)
    
a=10
b=20
c=mom(a,b)
print(c)

#int #(integer)
#float #(decimal) upto 6 decimals
#complex #(x+iy) complex numbers
#str #string
#bool # true or false (boolian)
#list
#tuple
#dict


#if True:
 #   print("Valid")
#else:
   # print("Invalid")
    #out put Valid(about bool data type)

#try and except condition
    
#try:
 #   a=int(input("Enter First Number: "))
 #   b=int(input("Enter Second Number: "))
 #   result=a+b
 #   print("Sum:",result)
#except ValueError:
#    print("Invalid input! Please enter Numbers only.")
#finally:
#    print("Code Exicuted Successfully")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
