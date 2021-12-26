def recFunc(num, cntr):
    if num <= 0: print(f'There are {cntr} digits')
    else: recFunc(num//10,cntr+1)

while True:
    recFunc(int(input("Enter num: ")),0)

'''
if num<0:
    print("Invalid num")
elif num==0:
    print("1 digit")
else:
    cntr=0;
    while num>0:
        cntr+=1
        num//=10
    print(f'There are {cntr} digits');
'''