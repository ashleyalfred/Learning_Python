answer = input("Do you want to add, subtract, multiply or divide?: ")

if answer == "add" or "Add" or "ADD": 
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = float(num1) + float(num2)
    print(result)
elif answer == "subtract" or "Subtract" or "SUBTRACT":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = float(num1) - float(num2)
    print(result)
elif answer == "multiply" or "Multiply" or "MULTIPLY":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = float(num1) * float(num2)
    print(result)
elif answer == "divide" or "Divide" or "DIVIDE":
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = float(num1) / float(num2)
    print(result)
