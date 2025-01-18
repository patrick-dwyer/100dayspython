# machine consumables (money: $, water: mL, coffee: g, milk: mL)
machine_resources = {
    'money': 5.00,
    'water': 500,
    'coffee': 100,
    'milk': 250

}

# dictonary of items (item: [cost ($), water (mL), coffee (g), milk (mL)])
drink_dictionary = {
    'espresso': [1.50, 50, 18, 0], 
    'latte': [2.50, 200, 24, 150], 
    'cappuccino': [3.00, 250, 24, 100]
    }

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
    print(f'Water: {machine_resources["water"]} mL\nMilk: {machine_resources["milk"]} mL\nCoffee: {machine_resources["coffee"]} g\nMoney: ${"{:.2f}".format(round(machine_resources["money"], 2))}')

else:
    # TODO 4. Check resources sufficient
    # give errors for which resources are insufficient
    def resource_check(user_selection, water, coffee, milk):
        water_check = water
        milk_check = milk
        coffee_check = coffee

        def resource_check():
            if water_check < 0 or coffee_check < 0 or milk_check < 0:
                print("Insufficient resources in the manchine, please replenish before making an order.")
                if water_check < 0:
                    print('Please replenish water.')
                if coffee_check < 0:
                    print('Please replenish coffee.')
                if milk_check < 0:
                    print('Please replenish milk.')
                
                return False
            else:
                print('No issue.')
                print(water_check, coffee_check, milk_check)
                return True

        if user_selection == 'espresso':
            water_check -= drink_dictionary['espresso'][1]
            coffee_check -= drink_dictionary['espresso'][2]
            milk_check = drink_dictionary['espresso'][3]
            resource_feedback = resource_check()
        elif user_selection == 'latte':
            water_check -= drink_dictionary['latte'][1]
            coffee_check -= drink_dictionary['latte'][2]
            milk_check -= drink_dictionary['latte'][3]
            resource_feedback = resource_check()
        elif user_selection == 'cappuccino':
            water_check -= drink_dictionary['cappuccino'][1]
            coffee_check -= drink_dictionary['cappuccino'][2]
            milk_check -= drink_dictionary['cappuccino'][3]
            resource_feedback = resource_check()
        else:
            print('Not a drink that can be made. Exiting to start.')
            return False

        
        # TODO 5. Process coins
        # prompt user to insert coins if sufficient consumables
        # ask user for how many they put in for coins
        # calculate the amount of coins put in
        if resource_feedback == True:
            def user_coin_input(user_selection):
                drink_cost = drink_dictionary[user_selection][0]
                print(f"You have selected {user_selection} that costs ${'%.2f' % drink_cost}. Please insert coins.")
                user_pennies = int(input('How many pennies? '))

                user_nickels = int(input('How many nickels? '))

                user_dimes = int(input('How many dimes? '))

                user_quarters = int(input("How many quarters? "))

                user_money_sum = ((user_pennies * 1) + (user_nickels * 5) + (user_dimes * 10) + (user_quarters * 25))/100
                print('Total money input is $', '%.2f' % user_money_sum)
                
                # TODO 6. Check transaction successful
                # check if money inserted enough, if not refund amount and error message
                # if exact money add to machine money, take away from consumables
                # if too much money, give refund amount to user as printout (round to two decimal places)
                if user_money_sum >= drink_cost:
                    refund_money = user_money_sum - drink_cost
                    print(f"Here is ${'%.2f' % refund_money} in change.")
                    print(f'Enjoy your {user_selection}!') 
                    # TODO 7. Make coffee
                    # deduct resources from coffee machine based on selection
                    # provide message to enjoy their drink of choice
                    print(type(refund_money))

                    machine_resources['water'] = water_check
                    machine_resources['coffee'] = coffee_check
                    machine_resources['milk'] = milk_check
                    machine_resources['money'] -= refund_money 
                    

                    print(machine_resources)
                    
                else:
                    refund_money = user_money_sum
                    print(f"Sorry that is not enough money. ${'%.2f' % refund_money} has been given back.")



            user_coin_input(user_selection)

    resource_check(user_selection, machine_resources["water"], machine_resources["coffee"], machine_resources["milk"])



