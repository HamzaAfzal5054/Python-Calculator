import math

def calculator():
    print('Welcome to the calculator')
    while True:
        print('\nChoose the operation:')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Square root')
        print('6. Cube')
        print('7. Modulus')
        print('8. Exponential')
        print('9. Exit')
        
        operation = input('Enter the operation number and it will perform soon: ')
        
        if operation == '1':
            a = float(input('Enter the first number: '))
            b = float(input('Enter the second number: '))
            print('The sum of the two numbers is:', a + b)
        elif operation == '2':
            a = float(input('Enter the first number: '))
            b = float(input('Enter the second number: '))
            print('The difference of the two numbers is:', a - b)
        elif operation == '3':
            a = float(input('Enter the first number: '))
            b = float(input('Enter the second number: '))
            print('The product of the two numbers is:', a * b)
        elif operation == '4':
            a = float(input('Enter the first number: '))
            b = float(input('Enter the second number: '))
            if b != 0:
                print('The division of the two numbers is:', a / b)
            else:
                print('Error: Division by zero is not allowed.')
        elif operation == '5':
            a = float(input('Enter the number: '))
            if a >= 0:
                print('The square root of the number is:', math.sqrt(a))
            else:
                print('Error: Cannot compute the square root of a negative number.')
        elif operation == '6':
            a = float(input('Enter the number: '))
            print('The cube of the number is:', a ** 3)
        elif operation == '7':
            a = float(input('Enter the first number: '))
            b = float(input('Enter the second number: '))
            print('The modulus of the two numbers is:', a % b)
        elif operation == '8':
            a = float(input('Enter the base number: '))
            b = float(input('Enter the exponent: '))
            print('The result of exponentiation is:', a ** b)
        elif operation == '9':
            print('Exiting the calculator. Goodbye!')
            break
        else:
            print('Invalid operation. Please try again.')

        print("\nReturning to the main menu...\n")  

calculator()