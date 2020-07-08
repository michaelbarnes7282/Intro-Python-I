total = 1760
fifties = 0
tens = 0
while total > 0:

    if total >= 50:
        fifties += 1
        total -= 50
    if total >= 10:
        tens += 1
        total -= 10
print('fifties ' + str(fifties))
print('tens ' + str(tens))
print((tens * 10) + (fifties * 50))