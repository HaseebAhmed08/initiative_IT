# light and cpu project




cpu : str = 'off'
Kelectric : str = 'on'


iskelectric = input('enter kelectric is on or off  ')

iscpu = input('enter cpu is on or off  ')


if iskelectric == 'on' and iscpu == 'on':
    print('Kelectric light & cpu is on')

elif iskelectric == 'on' and iscpu== 'off':
    print('Kelectric light is on & cpu is off') 

elif iskelectric == 'off' and iscpu== 'on':
    print('kelectric light is oof & cpu is on')



elif iskelectric != 'on' or 'off' or iscpu != 'on' or 'off':
    print('valid input please enter yes or no')

else:
    print('both are off')