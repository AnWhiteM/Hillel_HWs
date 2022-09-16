while True:
    op = input("Please enter operation(+,- etc.): ")
    n1 = float(input("Please enter 1st number: "))
    n2 = float(input("Please enter 2nd number: "))

    if op == '+':
            r = n1 + n2
            print("Result: " + str(r))
    elif op == '-':
            r = n1 - n2
            print("Result: " + str(r))
    elif op == '*':
            r = n1 * n2
            print("Result: " + str(r))
    elif op == '/':
        if n2 == 0:
                print("Division by zero is not allowed")
        else:
                r = n1 / n2
                print("Result: " + str(r))
    question = input("Do you want to continue (y for yes/n for no) : ")
    question = question.lower()
    if question == "n":
        break
    else:
        continue

