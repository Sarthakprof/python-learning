a=5
b="sarthak"
c=10.5

print(type(a))
print(type(b))
print(type(c))

#Python Data types
#1.Numeric - a. Integers - b.Complex Numbers - c.float
#2.Sequence Type - a.String - b.lists - c.tuple
#3.Dictionary
#4.Boolean
#5.Set

# A complex number contains an ordered pair,
# i.e., x + iy where x and y denote the real and imaginary parts, respectively.
# The complex numbers like 2.14j, 2.0 + 2.3j, etc.

#Numeric Example
m = 5  
print("The type of a", type(m))  
  
n = 40.5  
print("The type of b", type(n))  
  
c = 1+3j  
print("The type of c", type(c))  
print(" c is a complex number", isinstance(1+3j,complex))  

# String Example
str = "string using double quotes"  
print(str)  
s = '''''A multiline 
string'''  
print(s)  

# String Example 2

str1 = 'hello javatpoint' #string str1    
str2 = ' how are you' #string str2    
print (str1[0:2]) #printing first two character using slice operator    
print (str1[4]) #printing 4th character of the string    
print (str1*2) #printing the string twice    
print (str1 + str2) #printing the concatenation of str1 and str2    

# List Example

list1  = [1, "hi", "Python", 2]    
#Checking type of given list  
print(type(list1))  
  
#Printing the list1  
print (list1)  
  
# List slicing  
print (list1[3:])  
  
# List slicing  
print (list1[0:2])   
  
# List Concatenation using + operator  
print (list1 + list1)  
  
# List repetation using * operator  
print (list1 * 3)  

# TUPLE
# A tuple is similar to the list in many ways.
# Like lists, tuples also contain the collection of the items of different data types. 
# The items of the tuple are separated with a comma (,) and enclosed in parentheses ().
# A tuple is a read-only data structure as we can't modify the size and value of the items of a tuple.
tup  = ("hi", "Python", 2)    
# Checking type of tup  
print (type(tup))    
  
#Printing the tuple  
print (tup)  
  
# Tuple slicing  
print (tup[1:])    
print (tup[0:1])    
  
# Tuple concatenation using + operator  
print (tup + tup)    
  
# Tuple repatation using * operator  
print (tup * 3)     
  
# Adding value to tup. It will throw an error.  
#tup[2] = "hi"  

# Dictionary
# Dictionary is an unordered set of a key-value pair of items.
# It is like an associative array or a hash table where each key stores a specific value.
# Key can hold any primitive data type, whereas value is an arbitrary Python object.
d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}     
  
# Printing dictionary  
print (d)  
  
# Accesing value using keys  
print("1st name is "+d[1])   
print("2nd name is "+ d[4])    
  
print (d.keys())    
print (d.values())    

#Boolean
# Python program to check the boolean type  
print(type(True))  
print(type(False))  
#print(false) - throws error 

# Set
# Python Set is the unordered collection of the data type.
# It is iterable, mutable(can modify after creation), and has unique elements.
# In set, the order of the elements is undefined; 
# it may return the changed sequence of the element.
# The set is created by using a built-in function set(), 
# or a sequence of elements is passed in the curly braces and separated by the comma.
# It can contain various types of values

# Creating Empty set  
set1 = set()  
  
set2 = {'James', 2, 3,'Python'}  
  
#Printing Set value  
print(set2)  
  
# Adding element to the set  
  
set2.add(10)  
print(set2)  
  
#Removing element from the set  
set2.remove(2)  
print(set2)  

