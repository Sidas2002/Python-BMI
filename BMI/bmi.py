import sys

def get_user_input():
    try:
        weight_unit = input("Enter weight unit (kg/lb): ").lower()
        weight = float(input("Enter your weight: "))
        height_unit = input("Enter height unit (cm/inch): ").lower()
        if height_unit == 'cm':
            height = float(input("Enter your height in centimeters: "))
        elif height_unit == 'inch':
            feet = float(input("Enter feet: "))
            inches = float(input("Enter inches: "))
            height = (feet * 12) + inches
        else:
            print("Invalid height unit. Please enter 'cm' or 'inch'.")
            sys.exit(1)

        if weight <= 0 or (height_unit == 'cm' and height <= 0) or (height_unit == 'inch' and feet <= 0 and inches <= 0):
            print("Weight and height must be positive values.")
            sys.exit(1)

        return weight, height, weight_unit, height_unit
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        sys.exit(1)

def convert_to_metric(weight, height, weight_unit, height_unit):
    if weight_unit == 'lb':
        weight *= 0.453592  # Convert pounds to kilograms

    if height_unit == 'inch':
        height *= 2.54  # Convert inches to centimeters

    return weight, height

def calculate_bmi(weight, height):
    # Calculate BMI using the formula
    bmi = weight / ((height / 100) ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal Weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def display_bmi_info(bmi, bmi_category):
    print("Your BMI is:", round(bmi, 2))
    print("BMI Category:", bmi_category)

def main():
    print("Welcome to the BMI Calculator!")

    weight, height, weight_unit, height_unit = get_user_input()
    weight, height = convert_to_metric(weight, height, weight_unit, height_unit)

    bmi = calculate_bmi(weight, height)
    bmi_category = interpret_bmi(bmi)

    display_bmi_info(bmi, bmi_category)

if __name__ == "__main__":
    main()
