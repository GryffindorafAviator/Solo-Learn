while True:
    print "Options:"
    print "Enter 'add' to add two numbers"
    print "Enter 'subtract' to subtract two numbers"
    print "Enter 'multiply' to multiply two numbers"
    print "Enter 'divide' to divide two numbers"
    print "Enter 'quit' to end the program"
    user_input = raw_input(":")
    print user_input
    if user_input == 'quit':
        break
    elif user_input == 'add':
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
    elif user_input == 'subtract':
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
    elif user_input == 'multiply':
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
    elif user_input == 'divide':
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
    else:
        print ("unknown input")

    print "The answer is " + result

