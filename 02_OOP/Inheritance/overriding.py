class Employee:
    def work(self):
        print("Employee is working.....")
class Developer(Employee):
    def work(self):
        print("Developer is coding......")

d=Developer()
d.work()