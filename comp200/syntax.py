# Re-doing comp 100 as per comp 200

# hello.py


def hello_function():
    return("hello world")


# calc.py

def calc(num1, num2, operand):
    if operand == "add":
        num_sum = (num1)+(num2)
        return num_sum
    elif operand == "min":
        num_sum = (num1)-(num2)
        return num_sum
    elif operand == "mul":
        num_sum = (num1)*(num2)
        return num_sum
    elif operand == "div":
        num_sum = (num1)/(num2)
        return num_sum


def calc_file():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    op = input('Enter which operand (add,min,mul,div):  ')

    print(calc(num1, num2, op))


# tax_calc.py


def tax_calc(income):
    brackets = {"b1": 0.15, "b2": 0.2, "b3": 0.26, "b4": 0.29, "b5": .33}
    carry = {"b1": 0, "b2": 7145, "b3": 16908, "b4": 30535, "b5": 48719}

    if income < 47630:
        rate = brackets["b1"]
        carryover_tax = carry["b1"]
        return(rate*income + carryover_tax)
    elif income < 95259:
        rate = brackets["b2"]
        carryover_tax = carry["b2"]
        return((income-47630)*rate + carryover_tax)

    elif income < 147667:
        rate = brackets["b3"]
        carryover_tax = carry["b3"]
        return((income-95259)*rate + carryover_tax)

    elif income < 210371:
        rate = brackets["b4"]
        carryover_tax = carry["b4"]
        return((income-147667)*rate + carryover_tax)

    else:
        rate = brackets["b5"]
        carryover_tax = carry["b5"]
        return((income-210371)*rate + carryover_tax)


def tax_file():
    tax = int(input('Enter your income: '))
    tax_calc(tax)


# array.py

contents = []


def my_array(func="add", value=0):

    global contents
    if func == "add":
        # value = int(input('Enter item to add: '))
        contents.append(value)
        return contents
    elif func == "show":
        return contents
    elif func == "total":
        return sum(contents)
    elif func == "clear":
        contents = []
        return(contents)
    else:
        return True


def array_file():
    temp = False
    while (temp != True):
        opt = input('What would you like to do with the array: ')
        temp = my_array(opt)


# dictionary.py
def my_dictionary(key):
    items = {"AB": "Alberta", "BC": "British Columbia",
             "ON": "Ontario", "SK": "Sask"}

    return(items[key])


def dictionary_file():
    value = input("Enter a province(ie AB, BC etc) ").upper()
    my_dictionary(value)
