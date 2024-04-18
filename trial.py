number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number:"))
operation = input("Choose the operation (+, -, *): ")

if operation == "+":
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)       

elif operation == "-":
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == "*":
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
    