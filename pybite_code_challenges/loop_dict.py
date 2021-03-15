# loop_dict.py
'''
Loop through a dict and change the word to plural as required.
'''
games_won = dict(james=0, scotty=1, george=5, steve=3, dave=1)

def print_game_stats(games_won):
    for key,value in games_won.items():
        if value == 0:
            print(f'{key} has won {value} games')
        elif value ==1:
            print(f'{key} has won {value} game')
        else:
            print(f'{key} has won {value} games')

print_game_stats(games_won)