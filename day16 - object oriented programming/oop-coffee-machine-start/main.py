from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

interact = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#make list of items that have selections
items_list = menu.get_items()
items_list = items_list.split('/')
items_list.pop(-1)
# print(items_list)

while interact == True:
    choice = input(f'Choose item ({menu.get_items()}): ')
    
    #turn off
    if choice == 'off':
        interact = False
    
    #check resources (supplies)
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()

    elif choice in items_list:
        drink = menu.find_drink(choice)
        resource_check = coffee_maker.is_resource_sufficient(drink=drink)

        if resource_check == True:    
            money_check = money_machine.make_payment(drink.cost)

            if money_check == True:
                coffee_maker.make_coffee(drink)
            
        else:
            print('Not enough resources for that drink. Please pick another or replenish resources.')

    else:
        print('Please choose an appropriate drink from the list.')