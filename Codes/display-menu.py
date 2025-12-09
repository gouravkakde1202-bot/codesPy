# Temperature converter menu
import random
def celsius_to_fahrenheit(celsius):
   
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main_menu():
    
    print("Temperature converter!")

    while True:
        print("\n-- Menu --")
        print("1: Convert Celsius to Fahrenheit")
        print("2: Convert Fahrenheit to Celsius")
        print("3: Exit Menu")
        print("")

        num = input("Enter your no. (1, 2, or 3):")

        if num == '1':
            try:
                temp_c = float(input("Enter temperature in celsius:"))
                temp_f = celsius_to_fahrenheit(temp_c)
                print(f"Result: {temp_c}°C is {temp_f:.2f}°F") 
            except ValueError:
                print("enter a valid number.")

        elif num == '2':
            try:
                temp_f = float(input("Enter temperature in fahrenheit: "))
                temp_c = fahrenheit_to_celsius(temp_f)
                print(f"Result: {temp_f}°F is {temp_c:.2f}°C")
            except ValueError:
                print("enter a valid number.")

        elif num == '3':
            print("Exiting")
            break  

        else:
            print("Invalid no. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()     