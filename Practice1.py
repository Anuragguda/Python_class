#!/usr/bin/env python
# coding: utf-8

# In[12]:


#print hello world
print("hello world")


# In[22]:


#indentation
if 8>4:
    print("a is greater than b")


# In[29]:


#declaring a variable(comment line)
""" multi comment"""#(multi comment line)
x=5
x=55.55
myName="Anurag"
place='Hyderabad'#string can be declared either in single or double quote
print(x)
print(myName)
print(place)
print(x,myName,place)


# In[38]:


#types of declaring variable names
age=22
Age=22
myName='anurag'
_myname='bryant'
RollNumber=72
#29x=8 #syntax error variable name should start with a _(character or alphabet)
#for=32 #variable name should not be a keyword and keyword always start with a small letter
For=28
print(age)
print(Age)
print(myName)
print(_myname)
print(RollNumber)
print(For)


# In[50]:


#getting the type of datatype
x=5
print(type(x))#integer type
y=8.566
print(type(y))#float type
s={1,2,3,4,5}
print(type(l))#set
t=(1,2,3)
print(type(t))#tuple
m={'a':'anurag','b':33,'c':22}
print(type(m))#dictionary
l=[1,2,33,44]
print(type(s))#list
y=True
print(type(y))#boolean


# In[63]:


#setting the type of datatype
x=str("hello world")
print(x)
print(type(x))
a=int(3)
print(a)
print(type(a))#similary for float
s=set((1,2,3,4,(1,2),))#syntax for set is set((values))
print(s)
print(type(s))
t=tuple((1,2,3))#syntax for tuple is tuple((values))
print(t)
print(type(t))
l=list(((1,2),{3,2,1},1,3.5,{'a':'anurag','b':33})) #syntax for list is list((values))
print(l)
print(type(l))
d=dict(a='python',b='programming language') #syntax for dict is dict(a=value,......)
print(d)
print(type(d))


# In[65]:


#numbers in python
x=5   #integer
y=5.5 #float can be either +ve or -ve containing one or more decimals
m=-55.55
z=95j #complex number
print(type(x))
print(type(y))
print(type(m))
print(type(z))


# In[81]:


#type casting
#integer
x=25.22
int(x) #float is converted to a integer using int() constructor
print(x)

#y="anurag" #we cannot convert a string containing name to a integer 
#print(int(y))

z="33" #here string containig whole number can be converted to a integer
print(int(z))

#float
f=35
print(float(f)) #integer is coverted to float using float() constructor 

#similarly like integer string containing cannot be converted to a float value

s="38.6666" #string containing a number is converted to float
print(float(s)) 

#string
r=88
print(str(r))
# Anything written in int and float can be converted to string using str() constructor


# In[83]:


#strings
a="anurag" #assigning a string to a variable
print(a)
#multiline strings
h="""anurag studied in vardhaman college of
engineering in electronics and communications department"""
print(h)


# In[91]:


#boolean
print(len("anurag")>len("python")) #comparing the lengths of two strings
print(9<10)
print(int(9)>float(10.5))
x=5
z=10
print(x>z)


# In[138]:


#Lists in Python
list1=["anurag",23,99.8,(1,2)] #creating a list
print(list1)
print(list1[0]) #accesing the elements from a list
#print(list1[4]) #list index out of range error
#negative indexing-means beginning from the end
print(list1[-2]) #prints the value (it prints the last 2nd value)
#range of indexes - gives the values of specified range 
print(list1[-2:-1]) #here the range of 1 is included but 3 is not included
print(list1[1:]) #in this it prints the range from 1 to end 

#methods in list
#append()
list1.append("anudeep")#appends the value at the end of the list
#list1.append(23,23,"arjun") #Type error - append()takes eaxctly one argument
list1.append(23)
#count #counts the value repeated how many times
#list1.count(23)
print(list1.count(23))
print(list1)
#extend() #add the elements of a list to the current list
l2=[1,2,3]
l2.extend(list1) 
print(l2)
print(list1)
l3=[1,3,4]
l3.extend(l2)
print(l3)
#pop() #removes the element from the specified position
#l3.pop()
#print(l3)
#l3.pop(2,3) #pop() takes atmost 1 argument
print(l3)




# In[140]:


#pop()
l1=[1,2,3,4]
print(l1.pop(0))
print(l1)


# In[146]:


#extend()
l1=[1,2,3,4]
l2=[5,6,7,8]
l1.extend(l2)
print(l1)
print(l2)
print(l1[1:])


# In[147]:


#append()
l1=[1,5,8,10]
l1.append(8)
l1.append(9)
print(l1)


# In[164]:


#insert 
l1=["anurag",2,3,4]
l1.insert(-1,"kobe")
l1.insert(-1,"bryant")
print(l1[1]+l1[2]) #performs the addition between both the values in indexes
print(l1[-1]+l1[2])
print(l1[-2]+l1[-3])
#print(l1[3]+l1[4]+l[-1])# we can concatenate only strings not strings with int
print(l1)


# In[ ]:




