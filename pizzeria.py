# Pizza topping program


def showPizzaToppings(theList):
    if len(theList) == 0:
        print('your pizza has no toppings')
    else:
        print('The toppings on your pizza are:')
        print()
        for toppings in theList: 
            print('        ' + toppings)
    print()

#main code

print('Welcome to Pizzeria, where you get to choose your toppings.')
print('When prompted, enter the first letter or the full word of what you want\
 to do.')
print()
print('----Operations----')
print('a/add            Add a topping')
print('c/change         Change a topping')
print('o/order          Order the pizza')
print('q/quit           Quit')
print('r/remove         Remove a topping')
print('s/startover      Start over')
print()

toppingsList = []   # begin as an empty list
while True:

    print('What would you like to do?')
    menuChoice = input('    add, change, order, quit, remove, startover: ')

    if (menuChoice == 'a') or (menuChoice == 'add'):   # add a topping
        newTopping = input('Type in a topping to add: ')
        toppingsList.append(newTopping)  # append adds to the end of a list

    elif (menuChoice == 'c') or (menuChoice == 'change'):  #change a topping
        oldTopping = input('What topping would you like to change: ')
        if oldTopping in toppingsList:   # is it in the list
            index = toppingsList.index(oldTopping)      # find out where it is
            newTopping = input('What is the new topping: ')
            toppingsList[index] = newTopping    # set a new value at index
        else:
            print(oldTopping, 'was not found.')
    elif (menuChoice == 'o') or (menuChoice == 'order'):    # order the pizza
        showPizzaToppings(toppingsList)
        print()
        print('Thanks for your order!')
        print()
        another = input('Would you like to order another pizza (y/n)? ')
        if another == 'y':
            toppingsList = []  # reset to the empty list
        else:
            break
    elif(menuChoice == 'q') or (menuChoice == 'quit'):  # quit
        break
    elif(menuChoice == 'r') or (menuChoice == 'remove'):    # remove a topping
        delTopping = input('What topping would you like to remove?: ')
        if delTopping in toppingsList:  # check in list
            index = toppingsList.index(delTopping) # find where it is
            toppingsList.pop(index)   # remove it
            # the code above only removes the first occurence of the topping.
        else:
            print(delTopping, 'was not found')
    elif (menuChoice == 's') or (menuChoice == 'startover'):    # reset list
        print("OK, let's start over.")
        toppingsList = [] # reset to empty list
    else:
        print("Uh ... sorry, I'm not sure what you said, please try again.")
    showPizzaToppings(toppingsList)  # show the list of toppings
print()
print('Goodbye')
            
            
