name = input('Please enter you name: ')
age = int(input('How old are you, {0}? '.format(name)))
print(age)

if age == 17:
    print('Please come back in {0} year.'.format(18 - age))
elif age >= 18:
    print('You are an adult')
else:
    print('Please come back in {0} years'.format(18 - age))

