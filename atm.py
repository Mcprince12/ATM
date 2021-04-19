print("Welcome to bank ATM in python")
re = ('Y')
ha = 3
bal = 400
while ha >= 0:
    pin = int(input('Enter you pin 4 digits'))
    if pin == (1111):
        while re not in ('n', 'No', 'no', 'NO', 'N'):
            print('1 Balance\n')
            print('2 Widthdrawal\n')
            print('3 Deposit \n')
            print('4 End \n')
            op = int(input('Enter Your Option Here!'))
            if op == 1:
                print('Balance is $', bal, '\n')
                re = input('Do you want to restart?')
                if re in ('n', 'No', 'no', 'NO', 'N'):
                    print("Thank You!")
                    break
            elif op == 2:
                op2 = ('y')
                withd = float(input('Widthdraw amount? : '))
                if withd in [10, 20, 30, 100, 50, 200]:
                    bal = bal - widthd
                    print('\nBalance is $', bal)
                    re = input('Do you want to restart? ')
                    if re in ('n', 'No', 'no', 'NO', 'N'):
                        print('Thank you!')
                        break
            elif withd != [10, 20, 30, 40, 50, 100]:
                print('Invalid amount, do you want to try again?')
                re = ('y')
            elif widthd == 1:
                widthd = float(input('Amount to be widthdrawed :'))
        elif op == 3:
            dep = float(input('Deposit Amount? '))
            bal = bal + dep
            print('\nBalance is $ ', bal)
            re = input('Do you want to restart?')
            if re in ('n', 'No', 'no', 'NO', 'N'):
                print('Thank you')
                break
        elif op == 4:
            print('Please wait for card..\n')
            print('Thanks for enjoying our service!')
            break
        else:
            print('Enter a correct figure. \n')
            re = ('y')
    elif pin != (1111):
        print('Wrong pin')
        ha = ha - 1
        if ha == 0:
            print('\n Try Again!')
            break
