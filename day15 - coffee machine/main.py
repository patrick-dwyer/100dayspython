# machine consumables
water = 500
milk = 300
coffee = 50
money = 5.00

# TODO 1. Prompt user with choice of beverage
# check users input for what to do next
# prompt should show up once action is completed for next customer

user_selection = input("Please select which beverage you want. espresso | latte | cappuccino : ")

# TODO 2. Turn off coffee machine by typing 'Off'
# should end execution of program

if user_selection == 'off':
    exit

# TODO 3. Print report
# show report of current consumables and money in machine

elif user_selection == 'report':
    print(f'Water: {water}\nMilk: {milk}\nCoffee: {coffee} g\nMoney: ${"{:.2f}".format(round(money, 2))}')

# TODO 4. Check resources sufficient
# give errors for which resources are insufficient
def resource_check(user_selection, water, milk, coffee):
    water_check = water
    milk_check = milk
    coffee_check = coffee

    if user_selection == 'espresso':
        water_check -= 50
        coffee_check -= 18
        milk_check = milk
        resource_readback()
    elif user_selection == 'latte':
        water_check -= 200
        coffee_check -= 24
        milk_check -= 150
        resource_readback()
    elif user_selection == 'cappuccino':
        water_check -= 250
        coffee_check -= 24
        milk_check -= 100
        resource_readback()
    else:
        print('Not a drink that can be made. Exiting to start.')
        exit

    def resource_readback():
        if water_check < 0 or coffee_check < 0 or milk_check < 0:
            print('Triggered.')
            print(water_check, coffee_check, milk_check)
        else:
            print('No issue.')
            print(water_check, coffee_check, milk_check)

resource_check(user_selection, water, milk, coffee)

# TODO 5. Process coins
# prompt user to insert coins if sufficient consumables
# ask user for how many they put in for coins
# calculate the amount of coins put in

# TODO 6. Check transaction successful
# check if money inserted enough, if not refund amount and error message
# if exact money add to machine money, take away from consumables
# if too much money, give refund amount to user as printout (round to two decimal places)

# TODO 7. Make coffee
# deduct resources from coffee machine based on selection
# provide message to enjoy their drink of choice