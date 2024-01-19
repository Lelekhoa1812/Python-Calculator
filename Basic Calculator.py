import math

def add(*numbers):
    return sum(numbers)

def subtract(*numbers):
    if len(numbers) == 1:
        return -numbers[0]
    else:
        total = numbers[0]
        for num in numbers[1:]:
            total -= num
        return total

def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

def divide(*numbers):
    if len(numbers) == 1:
        return 'Error! Division by zero is not allowed'
    else:
        total = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                return 'Error! Division by zero is not allowed'
            total /= num
        return total

def power(*numbers):
    base = numbers[0]
    exponent = numbers[1]
    return base ** exponent

def logarithm(*numbers):
    if len(numbers) == 1:
        return math.log(numbers[0])
    else:
        base = numbers[0]
        num = numbers[1]
        return math.log(num, base)

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Logarithm")

while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num_of_numbers = int(input("Enter the number of numbers to be calculated: "))
        numbers = []
        for i in range(num_of_numbers):
            num = float(input("Enter number " + str(i+1) + ": "))
            numbers.append(num)

        if choice == '1':
            print("The sum of the numbers is: ", add(*numbers))

        elif choice == '2':
            print("The result of the subtraction is: ", subtract(*numbers))

        elif choice == '3':
            print("The product of the numbers is: ", multiply(*numbers))

        elif choice == '4':
            print("The result of the division is: ", divide(*numbers))

        elif choice == '5':
            base = numbers[0]
            exponent = numbers[1]
            print("The result of the power operation is: ", power(base, exponent))

        elif choice == '6':
            if len(numbers) == 1:
                print("The natural logarithm of the number is: ", logarithm(numbers[0]))
            else:
                base = numbers[0]
                num = numbers[1]
                print("The logarithm of the number with base ", base, " is: ", logarithm(base, num))

        next_calculation = input("Do you want to continue calculation (yes/no): ")
        if next_calculation == "no":
          print("Exiting the calculator")
          break

    else:
        print("Invalid Input")