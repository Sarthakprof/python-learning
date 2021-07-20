#Assigning single value to multiple variables
x=y=z=50    
print(x)    
print(y)    
print(z)   

#Assigning multiple values to multiple variables
a,b,c=5,10,15    
print(a)    
print(b)    
print(c)    

#Local variables are the variables
#that declared inside the function and have scope within the function
# Declaring a function  
def add():  
    # Defining local variables. They has scope only within a function  
    a = 20  
    b = 30  
    c = a + b  
    print("The sum is:", c)  
  
# Calling a function  
add() 


#Global variables can be used throughout the program, and its scope is in the entire program
# Declare a variable and initialize it  
x = 101  
  
# Global variable in function  
def mainFunction():  
    # printing a global variable  
    global x  
    print(x)  
    # modifying a global variable  
    x = 'Welcome To my world'  
    print(x)  
  
mainFunction()  
print(x)  

m = 5  
n = 6  
# printing multiple variables  
print(m,n)  
# separate the variables by the comma  
print(1, 2, 3, 4, 5, 6, 7, 8)   
