
def tax_calc(income):
    brackets = {"b1": 0.15, "b2": 0.2, "b3": 0.26, "b4": 0.29, "b5": .33}
    carry = {"b1": 0, "b2": 7145, "b3": 16908, "b4": 30535, "b5": 48719}

    if income < 47630:
        rate = brackets["b1"]
        carryover_tax = carry["b1"]
        print("Tax b1", rate*income + carryover_tax)
    elif income < 95259:
        rate = brackets["b2"]
        carryover_tax = carry["b2"]
        print("Tax b2", (income-47630)*rate + carryover_tax)

    elif income < 147667:
        rate = brackets["b3"]
        carryover_tax = carry["b3"]
        print("Tax b3", (income-95259)*rate + carryover_tax)

    elif income < 210371:
        rate = brackets["b4"]
        carryover_tax = carry["b4"]
        print("Tax b4", (income-147667)*rate + carryover_tax)

    else:
        rate = brackets["b5"]
        carryover_tax = carry["b5"]
        print("Tax b5", (income-210371)*rate + carryover_tax)


tax = int(input('Enter your income: '))
tax_calc(tax)
