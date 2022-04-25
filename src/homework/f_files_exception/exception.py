def show_inventory(file_name):
    try:      
        file_name = open('inventory.txt', 'r')

        file_name.write()

        contents = file_name.read()

        file_name.close()

    except IOError:
        "Invalid information has been entered"
