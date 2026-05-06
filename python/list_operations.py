def demonstrate_lists():
    """A simple demonstration of python list operations."""
    fruits = ["apple", "banana", "cherry"]
    print("Original list:", fruits)
    
    # Append
    fruits.append("orange")
    print("After append:", fruits)
    
    # Insert
    fruits.insert(1, "mango")
    print("After insert at index 1:", fruits)
    
    # Remove
    fruits.remove("banana")
    print("After removing 'banana':", fruits)
    
    # Pop
    last_item = fruits.pop()
    print(f"Popped item: {last_item}, List after pop: {fruits}")
    
    # List comprehension
    uppercase_fruits = [fruit.upper() for fruit in fruits]
    print("Uppercase versions using comprehension:", uppercase_fruits)

if __name__ == "__main__":
    demonstrate_lists()
