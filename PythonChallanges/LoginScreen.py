while True:
    print('Welcome to DEFCON')
    username = str(input('Please enter username'))
    password = str(input('Please enter password'))
    idan = str('megagay16')
    idanpass = str('password')
    sagi = str('123456sagi')

    if idan in username and idanpass in password:
        
        print('Welcome back sir!')

    elif idan in username and idanpass not in password:
        print('Password incorrect')

    else:
        print('User does not exist')

