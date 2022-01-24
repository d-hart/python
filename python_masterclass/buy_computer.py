available_parts = ['computer',
                    'monitor',
                    'keyboard',
                    'mouse',
                    'mouse mat',
                    'hdmi cable',
                    'dvd drive'
                    ]

# Generate a dynamic list based on the amount of entries in the corresponding list above
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = '-'
computer_parts = []

while current_choice != '0':
    # Compare numerically generated list to the list of computer parts
    if current_choice in valid_choices:
        # Turn current choice into an index for the list of computer parts
        index = int(current_choice) - 1
        chosen_part =  available_parts[index]
        if chosen_part in computer_parts:
            # Remove computer part from the list of selected computer parts
            print(f'Removing {current_choice}')
            computer_parts.remove(chosen_part)
        else:
            print(f'Adding {current_choice}')
            # Add computer part to the list of selected computer parts
            computer_parts.append(chosen_part)
        print(f"Your list now contains: {computer_parts}")
    else:
        print('Please add options from the list below:')
        # Print the index number and item from the list of computer parts
        for number, part in enumerate(available_parts):
            print(f'{number + 1}: {part}')
    current_choice = input()
print(computer_parts)