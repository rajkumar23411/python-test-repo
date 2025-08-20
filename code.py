def add_numbers(a,b):
    return a+b   # STYLE: missing spaces around operators

def divide(a, b):
    return a / b   # BUG: ZeroDivisionError not handled

def inefficient_sum(numbers):
    total = 0
    for i in range(len(numbers)):   # PERFORMANCE: using range(len()) instead of iterating directly
        total += numbers[i]
    return total

def insecure_function():
    # SECURITY: dangerous use of eval
    user_code = input("Enter Python code: ")
    eval(user_code)

def insecure_function_2():
    # SECURITY: dangerous use of eval
    user_code = input("Enter Python code: ")
    exec(user_code)

add = (x - 20)
print(add)