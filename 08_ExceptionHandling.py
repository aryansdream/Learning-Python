# =========================================
# ⚠️ EXCEPTION HANDLING IN PYTHON
# =========================================


# =========================================
# 1. BASIC TRY-EXCEPT
# =========================================
try:
    x = int("abc")  # will cause error
except:
    print("Error occurred")


# =========================================
# 2. SPECIFIC EXCEPTIONS
# =========================================
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ValueError:
    print("Invalid input (not a number)")
except ZeroDivisionError:
    print("Cannot divide by zero")


# =========================================
# 3. MULTIPLE EXCEPTIONS
# =========================================
try:
    a = int("10")
    b = int("0")
    print(a / b)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)


# =========================================
# 4. ELSE BLOCK
# =========================================
try:
    num = int("5")
except:
    print("Error")
else:
    print("Success, result:", num)


# =========================================
# 5. FINALLY BLOCK
# =========================================
try:
    file = open("sample.txt", "r")
except:
    print("File not found")
finally:
    print("This always runs")


# =========================================
# 6. RAISING EXCEPTIONS
# =========================================
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18+")

try:
    check_age(16)
except ValueError as e:
    print(e)


# =========================================
# 7. CUSTOM EXCEPTION
# =========================================
class CustomError(Exception):
    pass

def test():
    raise CustomError("Something went wrong")

try:
    test()
except CustomError as e:
    print(e)


# =========================================
# 8. FILE HANDLING WITH EXCEPTION
# =========================================
def safe_read(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error: {e}"

print(safe_read("sample.txt"))


# =========================================
# 9. REAL-WORLD EXAMPLE (USER INPUT)
# =========================================
def divide():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a / b)
    except ValueError:
        print("Enter valid numbers")
    except ZeroDivisionError:
        print("Cannot divide by zero")


# =========================================
# 10. BEST PRACTICES
# =========================================
# ❌ avoid:
# except:
#     pass

# ✅ better:
# except Exception as e:
#     print(e)


# =========================================
# 🎯 END OF EXCEPTION HANDLING
# =========================================