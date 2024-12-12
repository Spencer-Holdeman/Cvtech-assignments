import random
import string
import time

number_of_passwords = int(input('how many passwords do you want?'))
password_length = int(input('How long do you want your passwords?'))

start = time.time()
for i in range(number_of_passwords):
    password = ''
    password_characters = string.ascii_letters + string.digits + string.punctuation
    random_sequence = random.choices(password_characters, k = password_length)
    count = 0

    for x in random_sequence:
        password += x
    print('your password is : ' + password)
end = time.time()
print(end - start)
