'''def gmean(a,b):
    mean= (a*b)/(a+b)
    print(mean)

def greater(a,b):
    if (a>b):
        print("1st is greater")
    else:
        print("2nd is greater")        
a=10
b=20
gmean(a,b)
greater(a,b)

g=7
h=8
gmean(g,h)
greater(g,h)
    

def avg(*num):
    sum = 0
    for i in num:
        sum = sum + i
        return sum / len(num)
c=avg (5,5)
print(ConnectionAbortedError)'''


#KBC EXERCISE 
'''KBC=["apple", "orange","mango","banana"]
sent=input("Select a national fruit of India: ")
if sent in KBC:
    print("selected item is: ",sent)
    if sent =="mango":
        print("YAHHHHH, Answer is correct , YOu Won 1 crore")
    else:
        print("Wrong answer")    
else: 
    print("Invalid input")'''

#Functions
'''
def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(10))        
'''
#Dictonary
'''info={'name':'Rakesh','age':'19','Place':'KLBG'}
print(info)
print(info.keys())
print(info.values())
print(info.items())
print(info.get('name'))

for key in info.keys():
    print(info[key], end=" ")
'''
'''
for i in range (6):
    print(i)
    if (i==4):
        break
else:
    print("Sorry no i")    

'''
#
'''def func1():
    try:
        l=[1,2,3,4,5]
        num=int(input("Enter a number: "))
        print(l[num])
        return 1
    except :
        print("Invalid input")
        return 0
R=func1()
print(R)    
'''

'''a = input("Enter the value butween 5 and 9: ")

if (a == "quit"):
  print("ohk")
elif (int(a) < 5 or int(a) > 9):
  raise ValueError("The number should be between 5 and 9")



class Solution:
    def printNumber(self):
        n=int(input("Enter Number: "))
        print(n)
'''

'''marks=[12,3,44,33,98,76,54]
print(marks)

for index,mark in enumerate(marks):
    print(mark)
    if(index==4):
        print("Rakesh, awesome!")
    index+=1
'''

'''from math import sqrt,pi
n=sqrt(9) * pi
print(n)
'''
# from timeframe import timestamp,hour
# print(f"HI, RAKESH now the time is :{timestamp}")


'''
x=4
print(x)
def hello():
    x=5
    print("The local value of x is: ",x)
print("The value of global: ",x)    
hello()
print("The value of global: ",x)
'''

# f=open("timeframe.py","r")
# print(f.read())

'''def cube(x):
    return x*x*x
print(cube(2))
l=[1,2,3,4,5,6]
new=list(map(cube,l))
print(new)          '''


'''a=4
A="4"
print(a==A)
print(a is A)'''


'''
class Person:  
    # name="Rakesh"
    # occupation="Student"
    # Age="20"
    def __init__(self,name,occupation,age):
        
        self.name=name
        self.occupation=occupation
        self.age=age
    def info(self):
        print(f"{self.name} is a {self.occupation} and his age is {self.age}")
a=Person("Rakesh","Student","20")
a.info()'''


''''
def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("thanks")
    return mfx    
@greet
def hello():
     print("Hello World")
hello() '''

'''class Employee:
    def __init__(self):
        self.name="Rakesh"
        self.age="20"

a=Employee()
print(a.name)
print(a.age)'''


'''
#Snake,Water,Gun Game
import random

def check(comp,user):
    if comp==user:
        return 0
    if (comp==0 and user==1):
        return -1
    if (comp==1 and user==2):
        return -1
    if (comp==2 and user==0):
        return -1
    return 1

comp=random.randint(0,2)
user=int(input("0 for snake,1 for Water, 2 for Gun\nEnter your choice:"))


print("YOU:",user)
print("Computer:",comp)

score=check(comp,user)
if (score==0):
    print("It's a tie")
elif (score==1):
    print("You Won")
else:
    print("You Lose")  
 '''

##Library managment
# class Library:
#     def __init__(self):
#         self.nobooks = 0
#         self.books=[]
#     def addbook(self,book):
#         self.books.append(book)
#         self.nobooks=len(self.books)
#     def showinfo(self):
#         print(f"The books in the library is {self.nobooks}")

# l1=Library()
# l1.addbook("Rakesh")
# l1.addbook("Rakesh2")
# l1.addbook("Rakesh3")
# l1.showinfo( )      


# class person:
#     def __init__(self,name,age,version ):
#         self.name = name
#         self.age = age
#         self.version = version
# p = person("Raki",20,1)
# print(p.__dict__)        
# print(help(person))


# class shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def area(self):
#         return (self.x *self.y) 
# rec=shape(4,3)
# print(rec.area())      

'''import time
t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_time)'''


'''
foods=list()
while True:
    food=input("What food u like: ")
    if food=="quit":
        break
    foods.append(food)

foods=list()
while(food := input("Whta food u like: "))!="quit":
    foods.append(food)
'''
'''
#News_reader
import requests
from bs4 import BeautifulSoup
url="https://timesofindia.indiatimes.com/"
r=requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("figcaption"):
  print(heading.text) '''


'''
import threading
import time

def func(seconds):
    print(f"The seconds for waiting is {seconds} seconds")
    time.sleep(seconds)
time1=time.perf_counter()
# func(4)    
# func(2)    
# func(1)


t1=threading.Thread(target=func, args=(4,))    
t2=threading.Thread(target=func, args=(2,))    
t3=threading.Thread(target=func, args=(1,))


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2=time.perf_counter()  
print(time2-time1) '''

#Multi_processing
'''
import multiprocessing
import requests

def downloadfile(url,name):
    print("Started downloading")
    response=requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content) 
    print("FInished downloading")
pros=[]
url=
for i in range(5):
    p=multiprocessing.process(target=downloadfile, args=[url,i])
    p.start()
    pros.append(p)
for p in pros:
    p.join() '''