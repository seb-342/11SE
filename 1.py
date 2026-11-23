while True:
    try:
        number = ""
        number = int(input('What is the number? '))
        print('Hello World ' * number)

    except ValueError:
        print('No.')
