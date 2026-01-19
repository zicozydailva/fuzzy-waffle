def main():
    print("Hello from my Python app!")

if __name__ == "__main__":
    main()

# variables

age = 21 # integer
print("You're " + str(age) + " years old") # concatenation method
print(f"You're {age} years old")  # f-string method

# float
height = 5.9 # float
print(f"Your height is {height} feet")  # f-string method

# string
name = "John" # string
print("Hello, " + name + "!") # concatenation method
print(f"Hello, {name}!")  # f-string method

# boolean
is_student = True # boolean
print("Are you a student? " + str(is_student)) # concatenation method
print(f"Are you a student? {is_student}")  # f-string method    


# muliple assignment
x,y,z = 1,2,3
print(x)
print(y)
print(z)

# function decl

def happy_birthday(name, age):
    print(f"Happy birthday to you, {name}!")
    print(f"You're {age} years old!")
    print(f"Happy birthday to you, {name}!")

happy_birthday("John", 21)

# func with return statement
def add(num1, num2):
    z = num1 + num2
    return z

print(add(10, 12))