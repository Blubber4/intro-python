class meal():
    cost = 0
    tax = 0
    tip = 0
    total = 0

    def __init__(self, cost = 0):
        self.cost = float(cost)
        self.tax = self.cost * .07
        self.tip = self.cost * .18

    def calcTotal(self):
        self.total = self.tax + self.tip + self.cost

    def printReceipt(self):
        self.calcTotal()
        print("\n\t  Meal : $", '{:>9.2f}'.format(self.cost))
        print("\n\t   tip : $", '{:>9.2f}'.format(self.tip))
        print("\n\t   tax : $", '{:>9.2f}'.format(self.tax))
        print("\n\t Total : $", '{:>9.2f}'.format(self.total))