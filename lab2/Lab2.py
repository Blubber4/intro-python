import meals

def main():
    more = 'y'
    print("\tCalculate the real cost of a meal, where\n\t  tax is 7% and be nice to add 18% tip" )
    while more == 'y' or more == 'Y':
        cost = input("\n\n\t Meal Cost: ")
        meal = meals.meal(cost)
        meal.printReceipt()
        more = str(input("\n\t\tDo more (Y/N)?: "))

main()