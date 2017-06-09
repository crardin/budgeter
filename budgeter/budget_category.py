# this is the generic class file for budget categories
class budget_category:
    def __init__(self):
        self.balance = 0

    def status(self):
        # should return the current status of the category
        # this would be how much it "needs" money
        pass

    def add_money(self, amount):
        # this is the function to handle adding money to the category
        self.balance += amount

    def remove_money(self, amount):
        # this is the function to handle removing money to the category
        self.balance -= amount

    def get_balance(self):
        # this function returns the current amount of money in the category
        return self.balance

