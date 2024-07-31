import logging
import re
from typing import List

#debug: Detailed information, typically of interest only when diagnosing problems.

#info: Confirmation that things are working as expected.

#warning: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

#error: Due to a more serious problem, the software has not been able to perform some function.

#critical: A serious error, indicating that the program itself may be unable to continue running.

logger = logging.getLogger(__name__)

logging.basicConfig(filename='test.log',level=logging.DEBUG, format='%(levelname)s:%(asctime)s:%(message)s')

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

add_res = add(a=89, b=456789)
logger.debug(f"Add: 89 + 456789 = {add_res}")


class employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        if self.first == '' or self.last == '':
            logging.warning('Employee name is not provided')
            return
        logger.debug(f"Created Employee: {self.first} {self.last}")
        

emp1 = employee('John', 'Doe')
emp2 = employee('', 'Smith')


def filter_datum(fields, redaction, message, separator):
    #this function returns the log message obfuscating the fields provided in the fields list
    #with the redaction string using re.sub method to perform the substitution with a single regex
    
    for field in fields:
        message = re.sub(field+'=.*?'+separator, 
                         field+'.*?'+redaction+separator, message)
        
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        redact the message of LogRecord instance
        Args:
        record (logging.LogRecord): LogRecord instance containing message
        Return:
            formatted string
        """
        message = super(RedactingFormatter, self).format(record)
        redacted = filter_datum(self.fields, self.REDACTION,
                                message, self.SEPARATOR)
        return redacted
