# Simple Calculator
# Build a basic calculator that performs addition, subtraction, multiplication, and division. Use loops for continuous calculations and if-else statements for operation selection.

while True:
       print("Select operation:")
       print("1. Add")
       print("2. Subtract")
       print("3. Multiply")
       print("4. Divide")
       print("5. Exit")

       choice = input("Enter choice(1/2/3/4/5): ")

       if choice in ('1', '2', '3', '4'):
           try:
               num1 = float(input("Enter first number: "))
               num2 = float(input("Enter second number: "))
           except ValueError:
               print("Invalid input. Please enter numbers only.")
               continue

           if choice == '1':
               print(num1, "+", num2, "=", add(num1, num2))
           elif choice == '2':
               print(num1, "-", num2, "=", subtract(num1, num2))
           elif choice == '3':
               print(num1, "*", num2, "=", multiply(num1, num2))
           elif choice == '4':
               if num2 == 0:
                   print("Division by zero not allowed.")
               else:
                   print(num1, "/", num2, "=", divide(num1, num2))

       elif choice == '5':
           break

       else:
           print("Invalid input. Please enter a valid choice.")
calculator()
