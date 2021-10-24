import logging


logging.basicConfig(level=logging.DEBUG, filename='test.log')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

num1 = 20
num2 = 2

result = add(num1, num2)
logging.debug("Add {} {} = {}".format(num1, num2, result))

esult = subtract(num1, num2)
logging.debug("sub {} {} = {}".format(num1, num2, result))

result = multiply(num1, num2)
logging.debug("multiply {} {} = {}".format(num1, num2, result))

result = divide(num1, num2)
logging.debug("divide {} {} = {}".format(num1, num2, result))
