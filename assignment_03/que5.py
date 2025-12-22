def greet(name, message="good morning"):
    print(message, name)

# Function calls
greet("riya")                
greet("riya", "Good Evening") 

def student_info(name, rollno, course):
    print("Name:", name)
    print("Roll No:", rollno)
    print("Course:", course)

# Keyword arguments
student_info(name="Amit", rollno=101, course="Python")

# Order does not matter
student_info(course="Java", name="Neha", rollno=102)


# Arithmetic functions
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Function that accepts another function
def calculate(a, b, operation):
    return operation(a, b)

# Function calls
print("Addition:", calculate(10, 5, add))
print("Multiplication:", calculate(10, 5, multiply))



