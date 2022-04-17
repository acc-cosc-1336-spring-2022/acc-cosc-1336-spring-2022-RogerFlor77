import unittest 

from src.homework.i_dictionaries_sets import add_inventory
from src.homework.i_dictionaries_sets import remove_inventory_widget

class Test_Config(unittest.TestCase):
    
    def test_add_inventory(self):
        inventory = {}
        widget_name = "Widget1"
        widget_quantity = 10
        add_inventory(inventory, widget_name, widget_quantity)
        self.assertEqual(inventory[widget_name], 10)

        widget_quantity = 25
        add_inventory(inventory, widget_name, widget_quantity)
        self.assertEqual(inventory[widget_name], 35)

        widget_quantity = -10
        add_inventory(inventory, widget_name, widget_quantity)
        self.assertEqual(inventory[widget_name], 25)

    def test_remove_inventory_widet(self):
        inventory = {}
        inventory['widget1'] = 5
        inventory['widget2'] = 10
        remove_inventory_widget(inventory, 'widget1')
        self.assertEqual(1, len(inventory))
        self.assertEqual(inventory['widget2'], 10)
