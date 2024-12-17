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