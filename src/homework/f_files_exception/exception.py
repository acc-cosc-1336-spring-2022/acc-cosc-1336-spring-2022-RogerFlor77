import files
def show_inventory(file_name):
    try:      
        file_name = open('inventory.txt', 'r')

        file_name.write(files.add_inventory)

        contents = file_name.read()

        file_name.close()

        print('The inventory is')

    except IOError:
        print("Invalid information has been entered")
