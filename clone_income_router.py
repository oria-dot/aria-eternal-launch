# clone_income_router.py – Feed clone income into Income Core Engine

from income_core import IncomeAutomationCore

class CloneIncomeDistributor:
    def __init__(self):
        self.engine = IncomeAutomationCore()

    def run(self, clone_context):
        for clone in clone_context:
            role = clone.get("role", "Unknown")
            income = clone.get("income", 0.0)
            if income > 0:
                self.engine.add_income(role.capitalize(), income)
        return self.engine.auto_distribute()
