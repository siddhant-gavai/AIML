def divide_numbers(a, b):
    try:
        print(f"Attempting to divide {a} by {b}...")
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input types. Please provide numbers.")
    else:
        # This block runs only if no exception occurred in the try block
        print(f"Success! The result is {result}")
    finally:
        # This block always runs, regardless of whether an exception occurred
        print("Execution of the division operation is complete.\n")


# Test cases to demonstrate the flow
print("--- Test Case 1: Successful Division ---")
divide_numbers(10, 2)

print("--- Test Case 2: Division by Zero Exception ---")
divide_numbers(10, 0)

print("--- Test Case 3: Type Error Exception ---")
divide_numbers(10, "a")
