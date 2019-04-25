
contents = []


def my_array(func, value=0):

    global contents
    if func == "add":
        value = int(input('Enter item to add: '))
        contents.append(value)
    elif func == "show":
        print("array", contents)
    elif func == "total":
        print(sum(contents))
    elif func == "clear":
        contents = []
        print(contents)
    else:
        return True


temp = False
while (temp != True):
    opt = input('What would you like to do with the array: ')
    temp = my_array(opt)
