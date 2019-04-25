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


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter which operand (add,min,mul,div):  ')

print(calc(num1, num2, op))
