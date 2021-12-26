
#   0 - Knife
#   1 - Handgun
#   2 - Shotgun
#   3 - Assault Rifle

hp = 100

def start():
    print('Welcome to the Armory')

    while True:
        print('Please Select your weapon of choice:\n0. Knife\n1. Handgun\n2. Shotgun\n3. Assault Rifle')

        select = int(input())
        weapon = ['Knife', 'Handgun', 'Shotgun', 'Assault Rile']

        selection_ver = 0
        for i in range(len(weapon)):

            if(i==select):
                print('You have chosen ' + weapon[i])
                selection_ver = str(input('Are you sure?'))
                if 'yes' or 'Yes' or 'YES' in selection_ver:
                    print('Your current equipped weapon is ' + weapon[i])
                    return
                elif 'no' or 'No' or 'NO' in selection_ver:
                    break
            else:
                print('Error has occurred, Please try again')
                break





