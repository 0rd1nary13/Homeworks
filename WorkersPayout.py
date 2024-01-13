#This program calculates the total pay of a worker
#Author: Huiguang Ma at Jan 12th 2024
class Worker:
#Define attributes
    work_hours = 0.0
    work_rate = 0.0
#Calculate total pay
    def _total_pay(self):
    #Determine if the worker has worked over 40 hours
        if self.work_hours > 40:
            return (self.work_hours - 40) * self.work_rate * 1.5 + 40 * self.work_rate
        else:
            return self.work_hours * self.work_rate
#Construct a worker
worker1 = Worker()
worker1.work_hours = float(input("Enter work hours: "))
worker1.work_rate = float(input("Enter work rate: "))
print("Pay:",worker1._total_pay())

'''
Out put 1:
Enter work hours: 45
Enter work rate: 10
Pay: 475.0

Process finished with exit code 0
Out put 2:
Enter work hours: 56.32
Enter work rate: 23
Pay: 1483.04

Process finished with exit code 0
Out put 3:
Enter work hours: 32.32
Enter work rate: 17
Pay: 549.44

Process finished with exit code 0
'''
