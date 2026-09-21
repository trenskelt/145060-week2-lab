number1 = input("Enter a number: ")
print(int(number1))

number2 = input("Enter another number: ")
print(int(number2))

print(int(number1) + int(number2))

# It printed 53 because its reading as a string and not converting to a integer.

# Updated with 'int" conversions instead of leaving it as a string. Now it will add the two numbers together and print the total.

age = int(input("Enter your age: "))
print("You will be " + str(age + 10) + " in ten years.")

# Takes the users input then adds 10 and turns it into a string to print the final number. 

favorite_snack = float(input("Enter your snack price: "))
print("Buying 3 of your favorite snack will cost " + str(favorite_snack * 3) + " dollars.")

# Takes the number input and converts it to a float then multiplies by 3 and converts it back to a string to print the final number.

# Integer cant hold 3.5 because it has a decimal point. Only a float can hold a decimal point.




