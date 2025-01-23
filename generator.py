import time

def oddGen(n, m):
    while n < m:
        yield n
        n += 2


def oddLst(n, m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst


t1 = time.time()
sum(oddGen(1, 100000000))
print("Time to sum an iterator: %f" % (time.time() - t1))


class Employee(object):
    numEmployee = 0
    def __init__(self, name, salary, rate):
        self.owed = 0
        self.name = name
        self.rate = rate
        Employee.numEmployee += 1

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self, numHours):
        self.owed += numHours * self.rate
        return ("%.2f hours worked" % numHours)

    def pay(self):
        self.owed = 0
        return ("payed %s " % self.name)




