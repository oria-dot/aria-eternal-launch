
class IncomeAutomationCore:
    def __init__(self):
        self.sources = {}

    def add_income(self, source, amount):
        if source in self.sources:
            self.sources[source] += amount
        else:
            self.sources[source] = amount

    def get_income_summary(self):
        return self.sources
