from item import Item
from item import Department

def main():
    inFile = "blinn.dat"
    outFile = "blinn.out"

    try:
        inF = open(inFile, 'r')

    except IOError:
        print("\n\t\tCouldn't open input file", inFile)

    else:
        lines = inF.read().split('\n')
        departments = []
        prev_dept = 0
        for line in lines:
            dept_num = int(line[0])
            if dept_num != prev_dept:
                cur_dept = Department(dept_num)
                departments.append(cur_dept)

            name = line[2:9]
            quantity = line[10:14]
            unit_cost = line[15:18]
            unit_price = line[19:22]
            cur_item = Item(name, quantity, unit_cost, unit_price)
            cur_dept.addItem(cur_item)
            prev_dept = dept_num

        inF.close()

        try:
            outF = open(outFile, 'w')
            
        except IOError:
            print("\n\t\tCouldn't open output file", outFile)

        else:
            outF.write("\t\t       Blinn Discount Apparel Company\n")
            outF.write("\t\t\t   Inventory Evaluation\n")
            outF.write("\t\t\t       03/23/2019\n")
            outF.write("\n\t\t        Unit Cost\t\tExtended\n")
            outF.write("\t  Quantity    Cost    Market        Cost     Market    Lower Cost\n")

            sum = 0
            for dept in departments:
                dept.printDepartment(outF)
                sum += dept.lowerCost()
            outF.write(" Total Inventory {:>47}{:>9.2f}".format('$', sum))
            outF.close()
            print("Success!")

main()
