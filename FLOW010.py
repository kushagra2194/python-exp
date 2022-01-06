for t in range(int(input())):
    n = input()
    if n.lower() == 'b':
        print('BattleShip')
    elif n.lower() == 'c':
        print('Cruiser')
    elif n.lower() == 'd':
        print('Destroyer')
    elif n.lower() == 'f':
        print('Frigate')