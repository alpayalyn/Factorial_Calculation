while True:

    multiply = 1
    list1 = []
    number = int(input(print("Please enter a number for the factorial.")))

    while (number != 0):

        list1.append(number)

        multiply = multiply * number
        number = number - 1

        print(list1)
    print(multiply)
