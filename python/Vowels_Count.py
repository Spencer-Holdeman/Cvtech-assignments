string_input = input('Enter a sentence and I will tell you the amount of vowels used and how many times each vowels is used!')
string_input2 = string_input.replace(' ', '')
letters = [x for x in string_input2]
q = 0
y = 0
a = 0
e = 0
i = 0
o = 0
u = 0
for x in letters:
    if letters[q].lower() == 'y':
        y += 1
    if letters[q].lower() == 'a':
        a += 1
    if letters[q].lower() == 'e':
        e += 1
    if letters[q].lower() == 'i':
        i += 1
    if letters[q].lower() == 'o':
        o += 1
    if letters[q].lower() == 'u':
        u += 1
    q += 1
print(f'Total Number of vowels: {a + e + i + o + u + y}')
print(f'A="{a}"')
print(f'E="{e}"')
print(f'I="{i}"')
print(f'O="{o}"')
print(f'U="{u}"')
print(f'Y="{y}"')

