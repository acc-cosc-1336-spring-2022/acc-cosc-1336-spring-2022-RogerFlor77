import dictionary

menu_selection = "y"
while menu_selection == "y":
    print('\nMenu\n1-Get p disance matrix\n2-Exit')
    selection = int(input('Please select menu item 1 or 2: '))

    if selection == 1: 
        print('Enter your DNA Strings')
        dataset = []
        again = "y"
        while again == 'y':
            DNA_string = input('Enter a DNA String:')
            DNA_list = list(DNA_string)
            dataset.append(DNA_list)
            print('Do you want to add another?')
            again = input('Enter "y" for yes, n for no: ')
        print('Here are the strings')
        for string in dataset:
            print(string)
        print('The p distance matrix is:')
        p_distance_matrix = dictionary.get_p_distance_matrix(dataset)
        for row in p_distance_matrix:
            for item in row:
                print(format(item, '8.3f'), end = ' ')
            print('')

    elif selection == 2: 
        print('Program is done')

    else:
        print("Invalid Entry")
