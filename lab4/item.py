class Item(object):

    def __init__(self, n, q, uc, up):
        self.name = n
        self.quantity = int(q)
        self.unit_cost = float(uc)
        self.unit_price = float(up)
        self.ext_cost = float(self.unit_cost * self.quantity)
        self.ext_price = float(self.unit_price * self.quantity)
        if self.ext_cost < self.ext_price:
            self.lower = self.ext_cost
        else:
            self.lower = self.ext_price

    def printItem(self, outF):
        outF.write("  {:<9} {:>4d} {:>9.2f} {:>9.2f}     {:>9.2f} {:>9.2f}\n".format(self.name, \
                    self.quantity, self.unit_cost, self.unit_price, self.ext_cost, self.ext_price))

class Department(object):

    def __init__(self, dep_num):
        self.items = []

        dep_num = int(dep_num)
        if dep_num == 1:
            self.name = "Mens Dept"
        elif dep_num == 2:
            self.name = "Ladies Dept"
        elif dep_num == 3:
            self.name = "Girls Dept"
        elif dep_num == 4:
            self.name = "Boys Dept"
        else:
            self.name = "Unnamed Dept"

    def addItem(self, item):
        self.items.append(item)

    def lowerCost(self):
        if self.costSum() < self.priceSum():
            return self.costSum()
        return self.priceSum()

    def costSum(self):
        sum = 0
        for item in self.items:
            sum += item.ext_cost
        return sum

    def priceSum(self):
        sum = 0
        for item in self.items:
            sum += item.ext_price
        return sum

    def printDepartment(self, outF):
        outF.write(self.name + '\n')
        for item in self.items:
            item.printItem(outF)
        outF.write("   Total {:>33}{:>8.2f} ${:>8.2f} {:>4}{:>8.2f}\n".format('$', self.costSum(), self.priceSum(), '$', self.lowerCost()))
