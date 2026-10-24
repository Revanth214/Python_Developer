class Employee:
    def get_base_contract(self):
        return "Standard Employment Contract"
class Engineer(Employee):
    def debug_code(self):
        return "Fixing bugs....."
class Manager(Employee):
    def approve_budgut(self):
        return "Budget approved."
class TeamLeader(Engineer, Manager):
    def run_sprint(self):
        return "Starting a new agile work week."

lead=TeamLeader()
print(lead.get_base_contract())
print(lead.debug_code())
print(lead.approve_budgut())
print(lead.run_sprint())