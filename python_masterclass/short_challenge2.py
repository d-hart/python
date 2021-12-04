option_set = ['1.\tLearn Python', '2.\tLearn Terraform', '3.\tLearn Jenkins', '4.\tLearn boto3',
            '5.\tLearn Investing', '6.\tLearn Leadership','7.\tLearn a fighting style', 
            '8.\tHave fun', '0.\tExit']

# option_number = 1
while True:
    print('Please select an option from the list below:\n'
        '1.\tLearn Python\n2.\tLearn Terraform\n'
        '3.\tLearn Jenkins\n4.\tLearn boto3\n5.\tLearn Investing\n'
        '6.\tLearn Leadership\n7.\tLearn a fighting style\n'
        '8.\tHave fun\n0.\tExit')
    user_input=int(input())
    if user_input == 0:
        print('The program is going to terminate.')
        break
    elif 1 <= user_input <= 9:
        user_input-=1
        print(f'You have choosen the following option {option_set[user_input]}')
    # What's the part that hangs up?
        # Printing out the specific user's choice


    # for option in option_set:
        # print(f'{option_number}.\t{option}')
            # option_number = 0
        # option_number+=1
        # user_option = int(input())
        # if user_option == 0:
        #     print('Exiting the program')
        #     break
        # elif 0 < user_option <= 9:
        #     print('This is a valid selection')


