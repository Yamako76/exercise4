import random

print('Tossing a coin...')
cnt1 = 0
cnt2 = 0
for i in range(3):
    n = random.randint(0,100)
    if (n % 2) == 0:
        print('Round ' + str(i+1) + ': Heads')
        cnt1 += 1
    elif (n % 2) == 1:
        print('Round ' + str(i+1) + ': Tails')
        cnt2 += 1
print('Heads: '+ str(cnt1) + ', Tails: ' + str(cnt2))