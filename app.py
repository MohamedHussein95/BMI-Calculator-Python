import math
import os

name = input('Enter your name: ')
height = float(input('Enter your height in meters: '))
weight = float(input('Enter your weight in kilograms: '))

BMI = round(weight / (height ** 2), 2)

status = ''

if BMI <= 18.5:
    status = 'Underweight'
elif 18.5 < BMI <= 24.9:
    status = 'Normal weight'
elif 24.9 < BMI <= 29.9:
    status = 'Overweight'
elif BMI > 30:
    status = 'Obese'

print('Hi ' + name + ', your BMI is ' + str(BMI) + ' and you are ' + status + '.')

if status == 'Overweight' or status == 'Underweight':
    showTips = input('See Tips and Tricks? Reply "y" for yes or "n" for no: ')
    if showTips.lower() == 'y' and status == 'Overweight':
        print('Consult a healthcare professional:')
        print('Begin by consulting with a healthcare professional, such as a doctor or a registered dietitian,')
        print('who can provide personalized guidance based on your specific needs and health conditions.')
        print('Portion control:')
        print('Be mindful of portion sizes and avoid oversized servings.')
        print('Consider using smaller plates and bowls to help control portion sizes.')
    elif showTips.lower() == 'y' and status == 'Underweight':
        print('Consult a healthcare professional:')
        print('Start by consulting with a healthcare professional to rule out any underlying health conditions')
        print('that may contribute to being underweight and to receive personalized advice.')
        print('Strength training exercises:')
        print('Engage in regular strength training exercises to build muscle mass.')
        print('This can involve weightlifting, resistance training, or bodyweight exercises.')
        print('Consult with a fitness professional to design an appropriate program.')
    else:
        exit()

# Specify the directory path
directory = os.path.join(os.path.expanduser("~"), "Downloads")

file_name = name + ".txt"

# Create the file path
file_path = os.path.join(directory, file_name)

# Open and write to the file
with open(file_path, 'w') as file:
    file.write('Your name: ' + name + '\nYour height: ' + str(height) + ' meters\nYour weight: ' + str(weight) + ' kilograms\nBMI: ' + str(BMI) + '\nStatus: ' + status)

print('File saved successfully in the Downloads folder.')
print('File path:', file_path)

