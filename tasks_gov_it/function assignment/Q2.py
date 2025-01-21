
# Use functions to create a calculator.

#  making calculator using function and if else 




def calculator():


    if operation == '+':
        add = number1 + number2

        print(add  )
    
    elif operation == '-':
        print(number1-number2)
    
    elif operation == '*':
        print(number1*number2)

    elif operation == '/':
        print(number1/number2)

    else :
        print('user respond == null')


number1:int = int(input('write any number for operation '))
number2:int = int(input('write any number for operation '))
operation = input(' which operation you want to   (  + , - , * , / )')


calculator()
