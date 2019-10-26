def program_1():
    element_1 = input("Enter items for further processing: ").split()
    while True:
        steps = input("To shift left-enter positive values, to shift right- enter negative\nNumber of offset items: ")
        try:
            steps = int(steps)
        except ValueError:
            print("Only enter numbers.")
            steps = str(steps)
        else:
            if steps < 0:
                print("Shift left:")
                element_1 = element_1[len(element_1) + steps:] + element_1[:len(element_1) + steps]
            if steps == 0:
                print("The offset was not completed. Because the number of positions is zero.")
            else:
                print("Shift right:")
                element_1 = element_1[steps:] + element_1[:steps]
            print(element_1)
            break

while True:
    choice = input("Enter 1 to start the program. Enter 2 to exit.\n \nYour answer: ")

    try:
        choice = int(choice)
    except ValueError:
        print("You have entered an incorrect value, please try again.")

    if choice == 1:
        program_1()
    elif choice == 2:
        exit()
    else:
        print("Enter 1 or 2!")

    resume = input("Continue running the program? Enter y - yes, n - no: ")
    while resume.lower() != "y" and resume.lower() != "n":
        print( "Invalid character entered!" )
        resume = input("Continue running the program? Enter y - yes, n - no: ")
    if resume.lower() == "n":
        break