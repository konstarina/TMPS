def get():
    return "HavingAccountant"


class HavingAccountant:
    def __init__(self, accountant, factory):
        self.accountant = accountant
        self.factory = factory
        accountant.having_accountant = False

    def get_money(self, profit):
        return "good" if profit == "stable" else self.accountant.get_money(profit)


class BusinessPlan:
    def __init__(self, business):
        self.business = business
        business.business_plan = True

    def get(self):
        return self.business.get().replace("Without business plan", "With business plan")

    def get_money(self, profit):
        return "great" if profit == "huge" else self.business.get_money(profit)
