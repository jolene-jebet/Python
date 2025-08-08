def calculator():
    """
    A simple calculator that performs basic arithmetic operations.
    """
    
    print("=== Basic Calculator ===")
    print("Available operations: +, -, *, /")
    print()
    
    try:
        # Get the first number
        num1 = float(input("Enter the first number: "))
        
        # Get the operation
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Get the second number
        num2 = float(input("Enter the second number: "))
        
        # Perform the calculation based on the operation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
            
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
            
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
                
        else:
            print(f"Error: '{operation}' is not a valid operation.")
            print("Please use +, -, *, or /")
    
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
if __name__ == "__main__":
    # You can choose which version to run:
    
    # Option 1: Simple calculator (one calculation)
    calculator()
    
    print("\n" + "="*50 + "\n")