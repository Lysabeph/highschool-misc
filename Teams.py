import random

players = ["Bob", "Mike", "Jeff", "Luke", "Fred", "Tim", "Tom", "Jess", "Rick"]
teams = []
player_num = len(players)
for base in (3,4):
    if player_num%base == 0:
        teams.append([str(player_num)+"x"+str(base)])
    else:
        if player_num%base != 1:
            teams.append([str(player_num // base)+"x"+str(base),
            "1x"+str(player_num%base)])
        else:
            
print(teams)
