coins = 0 

coins = 0
while True:
    print(f'You have {coins} coins.')
    answer = input('Do you want another? Yes or No:>> ')
    if answer.lower() == "yes":
        coins += 1
    elif answer.lower() == "no":
        break
    else:
        print('You must enter Yes or No')
        continue
