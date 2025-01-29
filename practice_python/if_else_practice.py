

#  Odd or Even Check:

#  Ek program likho jo ek integer input le aur check kare ke yeh number odd hai
#  ya even. Agar even hai to "Even number" print karo aur
#  agar odd hai to "Odd number".


userinput = int(input('enter any number'))

evenlist : list=[]
oddlist : list=[]

if userinput % 2==0:
    print(userinput,'this is even')
    evenlist.append(userinput)
    print(evenlist)

else:
    print(userinput,'this is odd')
    oddlist.append(userinput)
    print(oddlist)

