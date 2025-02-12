# table in try catch

try:
    userinput =int( input('enter only number you want table'))
    for i in range(1,11):
                    print(f'{userinput} x {i} = {userinput*i}')
except Exception as e :
    print(e)
    print('please input number')