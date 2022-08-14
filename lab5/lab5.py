from date import Date

def main():
    more = 'y'
    while more == 'y' or more == 'Y':
        print("\nThis program will find days passed or date in the year")
        print("\t1)  Input date (mm/dd/yyyy) to find days passed")
        print("\t2)  Input passed days to find date in the year")

        choice = int(input("\t\tYour choice (1/2): "))
        if choice == 1:
            user_input = input("\n\tPlease input date (mm/dd/yyyy): ")
            d = user_input.split('/')
            # d, y, m order so m can be only default
            date = Date(d[1], d[2], d[0])
            if date.isValid():
                print("\n\tThere are", date.toDays(), "days passed in the year", date.y)
            else:
                print("\n\tPlease give a valid date (mm/dd/yyyy)")
        elif choice == 2:
            days = input("\n\tInput days: ")
            year = input("\n\t      Year: ")
            date = Date(days, year)
            if date.isValid():
                print("\n\tThe date is ", date.m, '/', date.d, '/', date.y, sep='')
            else:
                print("\n\tSomething is wrong with days or year.")
        else:
            print("\tPlease give a valid choice (1 or 2).")

        more = input("\n\tDo more (Y/N)? ")

main()
