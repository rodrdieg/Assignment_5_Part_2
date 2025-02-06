def calculate_bmi(weight_kg, height_m):
    """Calculate the Body Mass Index (BMI) given weight in kilograms (kg)
    and height in meters (m). BMI is a general indicator of health, but does 
    not account for factors like gender, muscle mass, or age. This function 
    returns the BMI as a float. Please consult a healthcare professional for 
    a more personalized assessment."""

    # Check for valid inputs
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive values. Please enter valid numbers.")
    
    # BMI calculation
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Example usage
try:
    # Prompt user for their weight (kg) and height (m)
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))
    
    bmi = calculate_bmi(weight, height)
    
    # Output result with helpful context for accessibility
    print(f"Your Body Mass Index (BMI) is: {bmi:.2f}.")
    print("Note: BMI is a general health indicator and may not fully reflect your overall health. Consult a healthcare professional for personalized advice.")
except ValueError as e:
    print(e)


