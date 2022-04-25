
def add_inventory(inventory, widget_name, widget_quantity):
    if widget_name not in inventory:
        inventory[widget_name] = widget_quantity
    else:
        inventory[widget_name] += widget_quantity

def remove_inventory_widget(inventory, widget_name):
    if widget_name in inventory:
        del inventory[widget_name]
        print('Record deleted')
    else:
        print('Item not found')

