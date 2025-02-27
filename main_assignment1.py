names = ['sandhya', 'anu', 'ram', 'lipika', 'sam']
ages = {'sandhya': 24, 'anu': 30, 'ram': 35, 'lipika': 28, 'sam': 22}
names.append('gada')
names.remove('anu')
names.insert(2, 'riyo')
sublist = names[1:4]
sentence = "Python is a powerful language"
words = sentence.split()
first_three_words = tuple(words[:3])
extra_ages = {'gadha': 29, 'riyo': 27}
employee_data = [('sandhya', 24, 'Engineer'), ('anu', 30, 'Designer'), ('ram', 35, 'Manager')]
last_name = names[-1]
is_in_list = 'ram' in names
names.sort()
names.reverse()
name_count = names.count('sandhya')
names.extend(['aruna', 'siri', 'pravali'])
person = ('sam', 22, 'Artist')
name, age, profession = person
every_second_name = names[::2]
# Using if, elif, and nested if conditions
if 'ram' in names:
    if ages['ram'] > 30:
        print('ram is older than 30.')
    elif ages['ram'] == 30:
        print('ram is 30 years old.')
    else:
        print('ram is younger than 30.')
else:
    print('ram is not in the list.')
# Multiple if conditions 
if 'sandhya' in names:
    print("sandhya is in the list.")
if 'riyo' not in names:
    print("riyo is not in the list.")
if ages['lipika'] < 30:
    print("lipika is younger than 30.")
# by using conditional stmt based on their we can also whether the person is teensger or not
    if age < 20:
        print(f'{name} is a teenager.')
    elif 20 <= age <= 35:
        print(f'{name} is a young adult.')
    else:
        print(f'{name} is an adult.')
#taking example of eligible to vote applied Nested if condition
    if age >= 18:
        if name == 'anu':
            print(f"{name} is eligible to vote and is also a registered voter.")
        else:
            print(f"{name} is eligible to vote.")
    else:
        print(f"{name} is not eligible to vote.")
print(f"Names: {names}")
print(f"Sublist of names: {sublist}")
print(f"First three words: {first_three_words}")
print(f"Last name: {last_name}")
print(f"Is Charlie in list: {is_in_list}")
print(f"Name count for 'Alice': {name_count}")
print(f"Every second name: {every_second_name}")
