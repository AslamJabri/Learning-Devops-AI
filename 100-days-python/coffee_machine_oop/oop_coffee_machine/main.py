from menu import Menu,MenuItem

my_menu = Menu()

print(my_menu.get_items())
choice = my_menu.find_drink("latte")

print(choice)