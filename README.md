# Assignment_5_Part_2
def cal(w, h):
    """Calculate the Body Mass Index (BMI) given weight and height. Takes two
    arguments weight in kilograms (kg) and height in meters(m). The function returns
    BMI of the weight and height as a float."""

    return w / (h ** 2)

# Example usage
bmi = cal(55, 1.67)
print(f"The BMI is: {bmi:.2f}")
