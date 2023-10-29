num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3


if (num1 >= num2 and num1 <= num3) or (num1 >= num3 and num1 <= num2):
    second_largest = num1
elif (num2 >= num1 and num2 <= num3) or (num2 >= num3 and num2 <= num1):
    second_largest = num2
else:
    second_largest = num3


print("Largest number:", largest)
print("Second-largest number:", second_largest)
