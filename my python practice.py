#declaring a variable
x = 5 # x is type of int
x + 'hello' # x is type of variable
print(x)

#assign value to multiple variable
x,y,z ="orange","mango","apple"
print(x)
print(y)
print(z)

#assign same value to multiple variable one line
x=y=z= "orange"
print(x)
print(y)
print(z)

#to print text with variable
x = "haroon"
print("my name is"+ x)

#print two variable
x = "haroon"
y = "shaikh"
z = x + y
print(z)

#Global variable
x = "haroon"# the variable create outside the function is(global variable)
def myfunc():#define function
 print("myname is "+ x)#function statemanet
 myfunc()#called myfunc

#create local variable
x = "good" #this is global variable

def myfunc():# create function fisrt
 x = "fantastic" #create local variable inside the function
 print("python is" + x)# statement print the function
 
myfunc() #called function second 
print("python is "+ x)# statement


# use of global keyword
x = "good" #default global variable
def myfunc: #create function myfunc
 global x #use global keyword to define global variable inside the function
 x = "fantastic" # global variable by global keyword
 
myfunc() # second function
 
 print("python is "+ x) #called function statements
 #output :- python is fantastic 



# Data type in python
x = "haroon"
print(x) # display x:

print(type(x)) #display data type of x:


#python Number ( int, float,complex)

x = 1 #int
y = 1.2 #float
z = 1j #complex
print(type(x))
print(type(y))
print(type(z))


#type of conversion
a = int(x) #convert float to int
b = float(y) # convert from 
c = complex(z) #convert from int to complex


#random number
import ramdom #import random module
print(random.randrange(1,10)) #print the random number from range 1 to 10



# String in python
x = 'haroon' # single quote string
x = "haroon" # double qoute string 

# multiple line string
a = ''' this is multi line string
using three single quote or double quote'''
print(a) # to print multiple line string

#string on arrays
a = "haroon"
print(a[1])
#output= a


#check string lenght
a = "haroon"
print(len(a)) #using len() keyword to  check length of variable
# output :- 6

#slicing on python
a = "haroon"
print(b[2:5))
#output:- roo


#string methon (strip() method use to remove white space )
a = " haroon "
print(a.strip()) #output:- haroon

#string lower case and upper case method
a = "HAROON"
print(a.lower()) #output:- haroon
print(a.upper()) #output:- HAROON

#replace method
a = "haroon"
print(a.replace("o","i") #output:- hariin

# split method in python 
a = "haroon, shaikh"
print(a.split(",") #output:- ['haroon','shaikh']


# python condition and if statement
a = 33 # variable
b = 200
if a<b: # condition 
    print("greater") #statement if condition is true

#if , elif, else statement

a = 10
b = 10
if a>b: #first condition
    print("greater")
elif a == b: # second condition
    print("equal")
else:  # print this statement if both condition is not true
    print("smaller")


    
# python loops
# while loop

i = 1 # set  variable with indexing 1
while i<6: # using while condition
    print(i) # statement
    if i ==3: # second condition if 
    break # if second condition is true take break
    i +=1 # same as i = i+1, increment i by adding 1

    
# Python Function
# Creating a function

def my_function(): #using def keyword to start function
    print("hello from function") #function body

#calling a function

def my_function():  #creating function  with def keyword
    print("hello from function") #function body or statement
# closing my_function
my_function() #calling my_function






    

    



