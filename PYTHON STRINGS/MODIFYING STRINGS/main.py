# *************************MODIFYING STRINGS**************************************8

# UPPER CASE

#upper() method Is used to return the string in upper case:

#EXAPMLE

a = "Hello, World!"
print(a.upper())


#LOWERCASE
#lower() method Is used to return the string in lower case:

a = "HELLO WORLD"
print(a.lower())

# Remove Whitespace
#Whitespace is the space before and/or after the actual text,
#we use strip() to remove unwanted white spaces
#EXAMPLE

a = "   Hello, World!    "
print(a.strip())

# REPLACING STRING
# WE USE keyword replace for replacing a string
#EXAMPLE

a = "hello world"

print(a.replace("h" "k")) #returns "kello world

#SPLITING A STRING
#The split() method returns a list where the text between the specified separator becomes the list items.

#EXAMPLE 
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

"""
exercise


write a program in python to convert "hello wordld" to uppercase and split the string
"""



