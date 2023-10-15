#alvin ocasio jr
#10/15/2023
#Module 3: Lab Activity – Programming
your_name = "alvin"
instructor_name = "james"
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
if first_name == your_name or first_name == instructor_name:
    print(f"Hello, {first_name} {last_name}, nice to meet you!")
else:
    print(f"Hello, {first_name} {last_name}, welcome!")

miles_driven = float(input("Please enter the number of miles driven: "))
gallons_used = float(input("Please enter the number of gallons used: "))
mpg = miles_driven / gallons_used
print(f"Your car's fuel efficiency is {mpg:.2f} MPG.")
gallons_used =(input("please enter the number of gallons used: "))
mpg = miles_driven / gallons_used
print("your cars mpg is")

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")

start_day = int(input("Enter the starting day number (0 for Sunday, 1 for Monday, etc.): "))
stay_length = int(input("Enter the length of your stay (in nights): "))
return_day = (start_day + stay_length) % 7
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"You will return home on a {days_of_week[return_day]}.")
