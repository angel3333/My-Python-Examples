# Error Handling Example
while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        print('Thank you!')
        break
    finally:
        print('Error handling done!')
