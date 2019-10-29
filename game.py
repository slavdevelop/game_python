player = {'name': 'Slav', 'attack': 13, 'heal': 16, 'health': 100}
monster = {'name': 'Max', 'attack': 12, 'health': 100}
game_running = True


while game_running == True:

    print('Please select action')
    print('1) Attack')
    print('2) Heal')

    user_input = input()

    if user_input == '1':
        monster['health'] -= player['attack']
        player['health'] -= monster['attack']

        print(monster['health'])
        print(player['health'])
    elif user_input == '2':
        print('Heal player')
    else:
        print('Invalid Input!')

    if player['health'] <= 0 or monster['health'] <= 0:
        game_running = False
