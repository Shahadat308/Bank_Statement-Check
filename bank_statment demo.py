bank_user = {'alice': 4000, 'smith': 3500, 'merry': 8798}

print('WELCOME TO THE BANK.')
while True:
    print('What do you want or like to do?')
    print(' '+'1.VIEW BALANCE')
    print(' '+'2.VIEW ALL BANK INFO')
    print(' '+'3.UPDATE BALANCE')
    print(' '+'4.EXIT')

    desc = input()
    if desc == '1':
        print('Enter your name please!: ')
        k = input()
        if k in bank_user.keys():
            print(k+' Your bank balance is '+str(bank_user[k]))
        else:
            print('The user cannot be found. Would you like to add the user to account?')
            desc = input()
            if desc == 'Yes':
                k = input('Enter your NAME please: ')
                v = input('Enter your balance please: ')
                bank_user.update({k: v})
            else:
                print('Would you like to exit?')
                desc = input()
                if desc == 'Yes':
                    break

    elif desc == '2':

        for k, v in bank_user.items():
            print('username: '+str(k)+'BANK BALANCE: '+str(v))
    elif desc == '3':
        print('Enter your name please: ')
        k = input()
        if k in bank_user.keys():
            print('Do you want to add or subtract from your savings?')
            desc = input()
            if desc == 'Add':
                temp_balance = bank_user[k]
                extra = input('Enter the amount you want to add: ')
                bank_user[k] = temp_balance+int(extra)
                print('Balance updated. It is: ')
                print(bank_user[k])
            elif desc == 'SUBTRACT':
                temp_balance = bank_user[k]
                extra = input('Enter the amount you want subtract')
                bank_user[k] = temp_balance-int(extra)
                print('Balance updated. It is: ')
                print(bank_user[k])
        else:
            print('There is no such account in the bank Database. ')
    elif desc == '4':
        break
