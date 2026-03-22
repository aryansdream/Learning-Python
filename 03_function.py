# =========================================
# 🧠 FUNCTIONS IN PYTHON
# =========================================


# =========================================
# 1. BASIC FUNCTION
# =========================================
def greet():
    print("Hello, welcome!")

greet()


# =========================================
# 2. FUNCTION WITH PARAMETERS
# =========================================
def greet_user(name):
    print("Hello", name)

greet_user("Aryan")


# =========================================
# 3. RETURN VALUES
# =========================================
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)


# =========================================
# 4. DEFAULT PARAMETERS
# =========================================
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Aryan")


# =========================================
# 5. KEYWORD ARGUMENTS
# =========================================
def student(name, age):
    print(name, age)

student(age=20, name="Aryan")


# =========================================
# 6. *ARGS (MULTIPLE POSITIONAL ARGUMENTS)
# =========================================
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add_all(1, 2, 3, 4))


# =========================================
# 7. **KWARGS (KEYWORD ARGUMENTS)
# =========================================
def print_info(**data):
    for key, value in data.items():
        print(key, ":", value)

print_info(name="Aryan", age=20, city="Patna")


# =========================================
# 8. LAMBDA FUNCTIONS
# =========================================
square = lambda x: x * x
print(square(5))


# =========================================
# 9. RECURSION
# =========================================
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# =========================================
# 10. LOCAL vs GLOBAL VARIABLES
# =========================================
x = 10  # global

def test():
    x = 5  # local
    print("Inside function:", x)

test()
print("Outside function:", x)


# =========================================
# 11. FUNCTION AS ARGUMENT
# =========================================
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def process(func, text):
    return func(text)

print(process(shout, "hello"))
print(process(whisper, "HELLO"))


# =========================================
# 12. MAP, FILTER (IMPORTANT)
# =========================================
nums = [1, 2, 3, 4]

squared = list(map(lambda x: x*x, nums))
print(squared)

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)


# =========================================
# 13. MINI PROBLEMS
# =========================================

# 1. Check prime using function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))


# 2. Reverse a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))


# 3. Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(5)


# =========================================
# 🎯 END OF FUNCTIONS
# =========================================