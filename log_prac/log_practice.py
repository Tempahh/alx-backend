import logging

#debug: Detailed information, typically of interest only when diagnosing problems.

#info: Confirmation that things are working as expected.

#warning: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

#error: Due to a more serious problem, the software has not been able to perform some function.

#critical: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(filename='test.log',level=logging.DEBUG, format='%(levelname)s:%(asctime)s:%(message)s')

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

add_res = add(a=89, b=456789)
logging.debug(f"Add: 89 + 456789 = {add_res}")


class employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        if self.first == '' or self.last == '':
            logging.warning('Employee name is not provided')
            return
        logging.debug(f"Created Employee: {self.first} {self.last}")
        

emp1 = employee('John', 'Doe')
emp2 = employee('', 'Smith')