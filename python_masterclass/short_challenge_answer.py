print('Please choose your option from the list below:')
print('1:\t Learn Python')
print('2.\tLearn Terraform')
print('3.\tLearn Jenkins')
print('4.\tLearn boto3')
print('5.\tLearn Investing')
print('6.\tLearn Leadership')
print('7.\tLearn a fighting style')
print('8.\tHave fun')
print('0.\tExit')

while True:
    choice = input()

    if choice == '0':
        break
    elif choice in '12345678':
        print('You chose {}'.format(choice))
    else:
        print('Please choose your option from the list below:')
        print('1:\t Learn Python')
        print('2.\tLearn Terraform')
        print('3.\tLearn Jenkins')
        print('4.\tLearn boto3')
        print('5.\tLearn Investing')
        print('6.\tLearn Leadership')
        print('7.\tLearn a fighting style')
        print('8.\tHave fun')
        print('0.\tExit')

# OR

choice = None
while True:
    if choice == '0':
        break
    elif choice in '12345678':
        print('You chose {}'.format(choice))
    else:
        print('Please choose your option from the list below:')
        print('1:\t Learn Python')
        print('2.\tLearn Terraform')
        print('3.\tLearn Jenkins')
        print('4.\tLearn boto3')
        print('5.\tLearn Investing')
        print('6.\tLearn Leadership')
        print('7.\tLearn a fighting style')
        print('8.\tHave fun')
        print('0.\tExit')
    
    choice = input()