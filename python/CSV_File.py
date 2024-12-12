import csv
import json
import os

os.system('cls')

y: int = 0

first_name = input('what is your first name?')
last_name = input('what is your last name?')
phone_number = input('What is your phone number?')
y = 1
data: dict = {

}

with open('profiles1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ['First Name', 'Last Name', 'Phone Number']
    writer.writerow(field)
    writer.writerow([first_name, last_name, phone_number])

with open('profiles1.csv', 'r') as csvfile:
    cvs_reader = csv.DictReader(csvfile)
    for row in cvs_reader:
        data[f'User Data {y}'] = row
        y += 1

with open('data.json', 'w') as file:
     json.dump(data, file, indent=2)

