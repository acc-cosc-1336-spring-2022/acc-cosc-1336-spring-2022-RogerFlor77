import sets

main_decision = 'y'
decision = 'y'
widgets = {}

main_decision = input("1 - Add or Update item:\tPress 1\n2-Delete Item\t\tPress 2\n3-Exit:\t\t\tPress 3")

while main_decision == "1":
    widget_name = input("Please enter the name of the widget you want to add or update")
    quantity = int(input("Please enter the name of the widget you want to add or update"))
    print(quantity, "x", widget_name, "will be added and if it already exists", widget_name, "will be incremented by x", quantity)
    widgets = sets.add_inventory(widgets, widget_name, quantity)
    print(widgets)
    decision = input("Do you have another widget to add?")
    
    while decision.lower() == "y":
        widget_name = input("Please enter the name of the widget you want to add or update")
        print(widget_name, "will be added and if it already exists", widget_name, "will be incremented")
        quantity = int(input("Please enter the quantity being added"))
        print(quantity, "x", widget_name, "will be added and if it already exists", widget_name, "will be incremented b x", quantity)
        widgets = sets.add_inventory(widgets, widget_name, quantity)
        print(widgets)
        decision = input("Do you have another widget to add?")
    main_decision = input("1-Add or Update Item:\tPress 1\n2-Delete Item\t\tPress 2\n3-Exit:\t\t\tPress 3")

    while main_decision == "2":
        print(widgets)
        widget_name = input("Please enter the name of the widget you want to remove")
        print(widget_name, "will be remove")
        sets.remove_inventory(widgets, widget_name)
        print(widgets)
        decision = input("Do you have another widget to remove")

        while decision.lower() == "y":
            print(widgets)
            widget_name = input("Please enter the name of the widget you want to remove")
            print(widget_name, "will be removed")
            sets.remove_inventory(widgets, widget_name)
            print(widgets)
            decision = input("Do you have another widget to remove?")
            main_decision = input("1- Add or Update Item:\tPress 1\n2-Delete Item\t\tPress 2\n3-Exit:\t\t\tPress 3")

            while main_decision == "3":
                print("Program has ended")
                quit()
