print(len("This thing is strange"))

# Apparently, String in python are just an Array of Chars
print("Hello"[-1])

# String
print("123" + "345")

# Integer = Whole Number
print(123 + 345)

# Large Integers
print(123_123_123)

# Float Datatype
print(3.14159)

# Boolean
print(True)
print(False)

# Check the Datatype
print(type("Hello"))
print(type(123))
print(type(123.00))
print(type(True))

# Type Casting
print(int("555") + int("123"))

# Exercise to identify where is the error on the line of code
username = input("Enter your name\n")
username_len = len(username)
print("Number of letters in your name: " + str(username_len))
# Answer: The error is on getting the len of name, when you get this int an try to
# Concatenate to str type, gives an error, to solve this, you need to cast len to str

