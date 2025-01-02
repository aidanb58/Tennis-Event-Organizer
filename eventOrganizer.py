import random
import operator

class Players(object):
    pros = []  #enter the names of the pros/coaches here. Capitalized, in quotation marks, and seperated by commas
    def __init__(self, name, skill, singles):
        self.name = name
        self.skill = skill
        self.partner = None
        self.singles = singles
        self.prev_partners = []
        self.prev_opponents = []
        
    def shuffle8(player1, player2, player3, player4, player5, player6, player7, player8):
        duos_count = 0
        players = [player1, player2, player3, player4, player5, player6, player7, player8]
        for player in players:
            if player.partner != None:
                duos_count += 0.5
        if duos_count == 0:
            num_attempts = 30
        if duos_count == 1:
            num_attempts = 15
        if duos_count == 2:
            num_attempts = 3
        for i in range(1, 4):
            round = i
            possible_matches = []
            while len(possible_matches) <= num_attempts:
                players = [player1, player2, player3, player4, player5, player6, player7, player8]
                if duos_count == 0:
                    playersNew = Players.shuffle(players)
                elif duos_count == 1:
                    first_found = False
                    for i in range(0, len(players)):
                        if players[i].partner != None:
                            if first_found == False:
                                players[i], players[0] = players[0], players[i]
                                first_found = True
                            else:
                                players[i], players[1] = players[1], players[i]
                    playersNew = [players[0], players[1]] + Players.shuffle(players[2:8])
                elif duos_count == 2:
                    ind = 0
                    i = 0
                    while i < len(players):
                        if players[i].partner != None:
                            players[i], players[ind] = players[ind], players[i]
                            ind += 1
                            for n in range(i+1, len(players)):
                                if players[n] == players[i].partner:
                                    players[ind], players[n] = players[n], players[ind]
                                    ind += 1
                                    i += 2
                        else:          
                            i += 1
                    playersNew = [players[0], players[1], players[2], players[3]] + Players.shuffle(players[4:8])
                    if round == 2:
                        playersNew[2], playersNew[4] = playersNew[4], playersNew[2]
                        playersNew[3], playersNew[5] = playersNew[5], playersNew[3]
                    elif round == 3:
                        playersNew[0], playersNew[6] = playersNew[6], playersNew[0]
                        playersNew[1], playersNew[7] = playersNew[7], playersNew[1]
                if playersNew not in possible_matches:
                    valid = True
                    for i in range(0, len(playersNew)):
                        if i % 2 == 0:
                            if (playersNew[i+1] in playersNew[i].prev_partners):
                                valid = False
                            if (i == 2):
                                if (playersNew[i-1] in playersNew[i].prev_opponents):
                                    valid = False
                        elif i % 2 == 1:
                            if i == 3:
                                if (playersNew[i-2] in playersNew[i].prev_opponents):
                                    valid = False
                    if valid == True:
                        possible_matches.append(playersNew)
            best_combo = None
            lowest_diff = 100
            for i in range(0, len(possible_matches)):
                combo = possible_matches[i]
                current_diff = abs((combo[0].skill + combo[1].skill) - (combo[2].skill + combo[3].skill)) + abs((combo[4].skill + combo[5].skill) - (combo[6].skill + combo[7].skill))
                if current_diff < lowest_diff:
                    lowest_diff = current_diff
                    best_combo = combo
            print(f"Round {round}:\n{best_combo[0].name} and {best_combo[1].name} vs {best_combo[2].name} and {best_combo[3].name}\n{best_combo[4].name} and {best_combo[5].name} vs {best_combo[6].name} and {best_combo[7].name}\n")
            for i in range(0, len(best_combo)):
                if i % 2 == 0:
                    if best_combo[i].partner != best_combo[i+1]:
                        best_combo[i].prev_partners.append(best_combo[i+1])
                    if duos_count < 2:
                        if i == 2:
                            if best_combo[i-1].partner != None:
                                best_combo[i].prev_opponents.append(best_combo[i-1])
                else:
                    if best_combo[i].partner != best_combo[i-1]:
                        best_combo[i].prev_partners.append(best_combo[i-1])
                    if duos_count < 2:
                        if i == 3:
                            if best_combo[i-2].partner != None:
                                best_combo[i].prev_opponents.append(best_combo[i-2])
   
    def shuffle10(player1, player2, player3, player4, player5, player6, player7, player8, player9, player10):
        players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
        singles_players = []
        duos_count = 0
        round1Singles = []
        round2Singles = []
        round3Singles = []
        for player in players:
            if player.partner != None:
                duos_count += 0.5
            elif player.singles:
                singles_players.append(player)
        if duos_count == 0:
            num_attempts = 30
        if duos_count == 1:
            num_attempts = 15
        if duos_count == 2:
            num_attempts = 5
        singles_players.sort(key = operator.attrgetter('skill'))
        proActive = False
        for playr in singles_players:
            if playr.name in Players.pros:
                proActive = True
                round1Singles.append(playr)
                round2Singles.append(playr)
                round3Singles.append(playr)
                singles_players.remove(playr)
                if len(singles_players) > 3:
                    ind = random.randint(0, len(singles_players)-1)
                    round1Singles.append(singles_players[ind])
                    singles_players.remove(singles_players[ind])
                    ind = random.randint(0, len(singles_players)-1)
                    round2Singles.append(singles_players[ind])
                    singles_players.remove(singles_players[ind])
                    ind = random.randint(0, len(singles_players)-1)
                    round3Singles.append(singles_players[ind])
                    singles_players.remove(singles_players[ind])
                elif len(singles_players) == 3:
                    round1Singles.append(singles_players[0])
                    round2Singles.append(singles_players[1])
                    round3Singles.append(singles_players[2])
                elif len(singles_players) == 2:
                    round1Singles = [singles_players[0], singles_players[1]]
                    round2Singles.append(singles_players[0])
                    round3Singles.append(singles_players[1])
                elif len(singles_players) == 1:
                    round1Singles.append(singles_players[0])
                    round2Singles.append(singles_players[0])
                    round3Singles.append(singles_players[0])
                break
        if proActive == False:
            if len(singles_players) == 3:
                round1Singles = [singles_players[1], singles_players[2]]
                round2Singles = [singles_players[0], singles_players[1]]
                round3Singles = [singles_players[0], singles_players[2]]
            elif len(singles_players) == 4:
                round1Singles = [singles_players[2], singles_players[3]]
                round2Singles = [singles_players[0], singles_players[1]]
                round3Singles = [singles_players[1], singles_players[2]]
            elif len(singles_players) == 5:
                round1Singles = [singles_players[3], singles_players[4]]
                round2Singles = [singles_players[0], singles_players[1]]
                round3Singles = [singles_players[2], singles_players[3]]
            elif len(singles_players) > 5:
                round1Singles = [singles_players[len(singles_players-1)], singles_players[len(singles_players-2)]]
                round2Singles = [singles_players[2], singles_players[3]]
                round3Singles = [singles_players[0], singles_players[1]]
        for i in range(1, 4):
            round = i
            if round == 1:
                singles = round1Singles
            elif round == 2:
                singles = round2Singles
            elif round == 3:
                singles = round3Singles
            print(f'Round {round}:\n{singles[0].name} vs {singles[1].name}')
            possible_matches = []
            while len(possible_matches) <= num_attempts:
                players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
                if duos_count == 0:
                    for player in players:
                        if player in singles:
                            players.remove(player)
                    playersNew = Players.shuffle(players)
                elif duos_count == 1:
                    first_found = False
                    for player in players:
                        if player in singles:
                            players.remove(player)
                    for i in range(0, len(players)):
                        if players[i].partner != None:
                            if first_found == False:
                                players[i], players[0] = players[0], players[i]
                                first_found = True
                            else:
                                players[i], players[1] = players[1], players[i]
                    playersNew = [players[0], players[1]] + Players.shuffle(players[2:8])
                elif duos_count == 2:
                    for player in players:
                        if player in singles:
                            players.remove(player)
                    ind = 0
                    i = 0
                    while i < len(players):
                        if players[i].partner != None:
                            players[i], players[ind] = players[ind], players[i]
                            ind += 1
                            for n in range(i+1, len(players)):
                                if players[n] == players[i].partner:
                                    players[ind], players[n] = players[n], players[ind]
                                    ind += 1
                                    i += 2
                        else:          
                            i += 1
                    playersNew = [players[0], players[1], players[2], players[3]] + Players.shuffle(players[4:8])
                    if round == 2:
                        playersNew[2], playersNew[4] = playersNew[4], playersNew[2]
                        playersNew[3], playersNew[5] = playersNew[5], playersNew[3]
                    elif round == 3:
                        playersNew[0], playersNew[6] = playersNew[6], playersNew[0]
                        playersNew[1], playersNew[7] = playersNew[7], playersNew[1]
                if playersNew not in possible_matches:
                    valid = True
                    for i in range(0, len(playersNew)):
                        if i % 2 == 0 and i < 8:
                            if (playersNew[i+1] in playersNew[i].prev_partners):
                                valid = False
                            if (i == 2):
                                if (playersNew[i-1] in playersNew[i].prev_opponents):
                                    valid = False
                        elif i % 2 == 1:
                            if i == 3:
                                if (playersNew[i-2] in playersNew[i].prev_opponents):
                                    valid = False
                    if valid == True:
                        possible_matches.append(playersNew)
            best_combo = None
            lowest_diff = 100
            for i in range(0, len(possible_matches)):
                combo = possible_matches[i]
                current_diff = abs((combo[0].skill + combo[1].skill) - (combo[2].skill + combo[3].skill)) + abs((combo[4].skill + combo[5].skill) - (combo[6].skill + combo[7].skill))
                if current_diff < lowest_diff:
                    lowest_diff = current_diff
                    best_combo = combo
            print(f"{best_combo[0].name} and {best_combo[1].name} vs {best_combo[2].name} and {best_combo[3].name}\n{best_combo[4].name} and {best_combo[5].name} vs {best_combo[6].name} and {best_combo[7].name}\n")
            for i in range(0, len(best_combo)):
                if i % 2 == 0 and i < 8:
                    if best_combo[i].partner != best_combo[i+1]:
                        best_combo[i].prev_partners.append(best_combo[i+1])
                    if duos_count < 2:
                        if i == 2:
                            if best_combo[i-1].partner != None:
                                best_combo[i].prev_opponents.append(best_combo[i-1])
                else:
                    if best_combo[i].partner != best_combo[i-1]:
                        best_combo[i].prev_partners.append(best_combo[i-1])
                    if duos_count < 2:
                        if i == 3:
                            if best_combo[i-2].partner != None:
                                best_combo[i].prev_opponents.append(best_combo[i-2])
   
    def shuffle11(player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11):
        duos_count = 0
        players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11]
        for player in players:
            if player.partner != None:
                duos_count += 0.5
        if duos_count == 0:
            num_attempts = 25
        if duos_count == 1:
            num_attempts = 10
        if duos_count == 2:
            num_attempts = 4
        if duos_count == 3:
            num_attempts = 2
        for i in range(1, 4):
            round = i
            possible_matches = []
            while len(possible_matches) <= num_attempts:
                players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11]
                singlesFound = False
                for player in players:
                    if player.name in Players.pros:
                        singlePlayer = player
                        singlesFound = True
                if not singlesFound:
                    bestPlayer = player1
                    for i in range (1, len(players)):
                        if (players[i].skill > bestPlayer.skill) and (players[i].singles):
                            bestPlayer = players[i]
                    singlePlayer = bestPlayer
                players.remove(singlePlayer)
                if duos_count == 0:
                    playersNew = Players.shuffle(players)
                elif duos_count == 1:
                    first_found = False
                    for i in range(0, len(players)):
                        if players[i].partner != None:
                            if first_found == False:
                                players[i], players[0] = players[0], players[i]
                                first_found = True
                            else:
                                players[i], players[1] = players[1], players[i]
                    playersNew = [players[0], players[1]] + Players.shuffle(players[2:10])
                elif duos_count == 2:
                    ind = 0
                    i = 0
                    while i < len(players):
                        if players[i].partner != None:
                            players[i], players[ind] = players[ind], players[i]
                            ind += 1
                            for n in range(i+1, len(players)):
                                if players[n] == players[i].partner:
                                    players[ind], players[n] = players[n], players[ind]
                                    ind += 1
                                    i += 2
                        else:          
                            i += 1
                    playersNew = [players[0], players[1], players[2], players[3]] + Players.shuffle(players[4:10])
                    if round == 2:
                        playersNew[2], playersNew[4] = playersNew[4], playersNew[2]
                        playersNew[3], playersNew[5] = playersNew[5], playersNew[3]
                    elif round == 3:
                        playersNew[0], playersNew[6] = playersNew[6], playersNew[0]
                        playersNew[1], playersNew[7] = playersNew[7], playersNew[1]
                elif duos_count == 3:
                    ind = 0
                    i = 0
                    while i < len(players):
                        if players[i].partner != None:
                            players[i], players[ind] = players[ind], players[i]
                            ind += 1
                            for n in range(i+1, len(players)):
                                if players[n] == players[i].partner:
                                    players[ind], players[n] = players[n], players[ind]
                                    ind += 1
                                    i += 2
                        else:          
                            i += 1
                    playersNew = [players[0], players[1], players[2], players[3], players[4], players[5]] + Players.shuffle(players[6:10])
                    if round == 2:
                        playersNew[2], playersNew[8] = playersNew[8], playersNew[2]
                        playersNew[3], playersNew[9] = playersNew[9], playersNew[3]
                    if round == 3:
                        playersNew[0], playersNew[8] = playersNew[8], playersNew[0]
                        playersNew[1], playersNew[9] = playersNew[9], playersNew[1]              
                playersNew.append(singlePlayer)
                if playersNew not in possible_matches:
                    valid = True
                    for i in range(len(playersNew)):
                        if i % 2 == 0 and i < 10:
                            if (playersNew[i+1] in playersNew[i].prev_partners):
                                valid = False
                            if (i == 2):
                                if (playersNew[i-1] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 4:
                                if (playersNew[i+2] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 6:
                                if (playersNew[i-1] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 8:
                                if (playersNew[i+2] in playersNew[i].prev_opponents):
                                    valid = False
                        elif i % 2 == 1:
                            if i == 1:
                                if (playersNew[i+1] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 3:
                                if (playersNew[i-2] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 5:
                                if (playersNew[i+1] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 7:
                                if (playersNew[i-2] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 9:
                                if (playersNew[i+1] in playersNew[i].prev_opponents):
                                    valid = False
                    if valid == True:
                        possible_matches.append(playersNew)
            best_combo = None
            lowest_diff = 100
            for i in range(0, len(possible_matches)):
                combo = possible_matches[i]
                current_diff = abs((combo[0].skill + combo[1].skill) - (combo[2].skill + combo[3].skill)) + abs((combo[4].skill + combo[5].skill) - (combo[6].skill + combo[7].skill))
                if current_diff < lowest_diff:
                    lowest_diff = current_diff
                    best_combo = combo
            print(f"Round {round}:\n{best_combo[0].name} and {best_combo[1].name} vs {best_combo[2].name} and {best_combo[3].name}\n{best_combo[4].name} and {best_combo[5].name} vs {best_combo[6].name} and {best_combo[7].name}\n{best_combo[8].name} and {best_combo[9].name} vs {best_combo[10].name}\n")
            for i in range(0, len(best_combo)):
                if i % 2 == 0 and i < 10:
                    if best_combo[i].partner != best_combo[i+1]:
                        best_combo[i].prev_partners.append(best_combo[i+1])
                    if duos_count < 3:
                        if i == 2:
                            if best_combo[i-1].partner != None:
                                best_combo[i].prev_opponents.append(best_combo[i-1])
                        if i == 4:
                            if best_combo[i+2].partner != None:
                                best_combo[i].prev_opponents.append(best_combo[i+2])
                        if i == 6:
                            if best_combo[i-1].partner != None:
                                best_combo[i].prev_opponents.append(best_combo[i-1])
                        if i == 8:
                            best_combo[i].prev_opponents.append(best_combo[i+2])
                else:
                    if best_combo[i].partner != best_combo[i-1]:
                        best_combo[i].prev_partners.append(best_combo[i-1])
                    if duos_count < 3:
                        if i == 1:
                            if best_combo[i+1].partner != None:
                                best_combo[i].prev_opponents.append(best_combo[i+1])
                        if i == 3:
                            if best_combo[i-2].partner != None:
                                best_combo[i].prev_opponents.append(best_combo[i-2])
                        if i == 5:
                            if best_combo[i+1].partner != None:
                                best_combo[i].prev_opponents.append(best_combo[i+1])
                        if i == 7:
                            if best_combo[i-2].partner != None:
                                best_combo[i].prev_opponents.append(best_combo[i-2])
                        if i == 9:
                            best_combo[i].prev_opponents.append(best_combo[i+1])

    def shuffle12(player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12):
        duos_count = 0
        players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12]
        for player in players:
            if player.partner != None:
                duos_count += 0.5
        if duos_count == 0:
            num_attempts = 75
        if duos_count == 1:
            num_attempts = 45
        if duos_count == 2:
            num_attempts = 25
        if duos_count == 3:
            num_attempts = 10
        for i in range(1, 4):
            round = i
            possible_matches = []
            while len(possible_matches) <= num_attempts:
                players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12]
                if duos_count == 0:
                    playersNew = Players.shuffle(players)
                elif duos_count == 1:
                    first_found = False
                    for i in range(0, len(players)):
                        if players[i].partner != None:
                            if first_found == False:
                                players[i], players[0] = players[0], players[i]
                                first_found = True
                            else:
                                players[i], players[1] = players[1], players[i]
                    playersNew = [players[0], players[1]] + Players.shuffle(players[2:12])
                elif duos_count == 2:
                    ind = 0
                    i = 0
                    while i < len(players):
                        if players[i].partner != None:
                            players[i], players[ind] = players[ind], players[i]
                            ind += 1
                            for n in range(i+1, len(players)):
                                if players[n] == players[i].partner:
                                    players[ind], players[n] = players[n], players[ind]
                                    ind += 1
                                    i += 2
                        else:          
                            i += 1
                    playersNew = [players[0], players[1], players[2], players[3]] + Players.shuffle(players[4:12])
                    if round == 2:
                        playersNew[2], playersNew[4] = playersNew[4], playersNew[2]
                        playersNew[3], playersNew[5] = playersNew[5], playersNew[3]
                    elif round == 3:
                        playersNew[0], playersNew[6] = playersNew[6], playersNew[0]
                        playersNew[1], playersNew[7] = playersNew[7], playersNew[1]
                elif duos_count == 3:
                    ind = 0
                    i = 0
                    while i < len(players):
                        if players[i].partner != None:
                            players[i], players[ind] = players[ind], players[i]
                            ind += 1
                            for n in range(i+1, len(players)):
                                if players[n] == players[i].partner:
                                    players[ind], players[n] = players[n], players[ind]
                                    ind += 1
                                    i += 2
                        else:          
                            i += 1
                    playersNew = [players[0], players[1], players[2], players[3], players[4], players[5]] + Players.shuffle(players[6:12])
                    if round == 2:
                        playersNew[2], playersNew[8] = playersNew[8], playersNew[2]
                        playersNew[3], playersNew[9] = playersNew[9], playersNew[3]
                    if round == 3:
                        playersNew[0], playersNew[8] = playersNew[8], playersNew[0]
                        playersNew[1], playersNew[9] = playersNew[9], playersNew[1]              
                if playersNew not in possible_matches:
                    valid = True
                    for i in range(len(playersNew)):
                        if i % 2 == 0:
                            if (playersNew[i+1] in playersNew[i].prev_partners):
                                valid = False
                            if (i == 2):
                                if (playersNew[i-1] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 4:
                                if (playersNew[i+2] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 6:
                                if (playersNew[i-1] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 8:
                                if (playersNew[i+2] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 10:
                                if (playersNew[i-1] in playersNew[i].prev_opponents):
                                    valid = False
                        elif i % 2 == 1:
                            if i == 1:
                                if (playersNew[i+1] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 3:
                                if (playersNew[i-2] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 5:
                                if (playersNew[i+1] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 7:
                                if (playersNew[i-2] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 9:
                                if (playersNew[i+1] in playersNew[i].prev_opponents):
                                    valid = False
                            if i == 1:
                                if (playersNew[i-2] in playersNew[i].prev_opponents):
                                    valid = False
                    if valid == True:
                        possible_matches.append(playersNew)
            best_combo = None
            lowest_diff = 100
            for i in range(0, len(possible_matches)):
                combo = possible_matches[i]
                current_diff = abs((combo[0].skill + combo[1].skill) - (combo[2].skill + combo[3].skill)) + abs((combo[4].skill + combo[5].skill) - (combo[6].skill + combo[7].skill)) + abs((combo[8].skill + combo[9].skill) - (combo[10].skill + combo[11].skill))
                if current_diff < lowest_diff:
                    lowest_diff = current_diff
                    best_combo = combo
            print(f"Round {round}:\n{best_combo[0].name} and {best_combo[1].name} vs {best_combo[2].name} and {best_combo[3].name}\n{best_combo[4].name} and {best_combo[5].name} vs {best_combo[6].name} and {best_combo[7].name}\n{best_combo[8].name} and {best_combo[9].name} vs {best_combo[10].name} and {best_combo[11].name}\n")
            for i in range(0, len(best_combo)):
                if i % 2 == 0:
                    if best_combo[i].partner != best_combo[i+1]:
                        best_combo[i].prev_partners.append(best_combo[i+1])
                    #if duos_count < 3:
                    if i == 2:
                        if best_combo[i-1].partner != None:
                            best_combo[i].prev_opponents.append(best_combo[i-1])
                    if i == 4:
                        if best_combo[i+2].partner != None:
                            best_combo[i].prev_opponents.append(best_combo[i+2])
                    if i == 6:
                        if best_combo[i-1].partner != None:
                            best_combo[i].prev_opponents.append(best_combo[i-1])
                    if i == 8:
                        best_combo[i].prev_opponents.append(best_combo[i+2])
                    if i == 10:
                        best_combo[i].prev_opponents.append(best_combo[i-1])
                else:
                    if best_combo[i].partner != best_combo[i-1]:
                        best_combo[i].prev_partners.append(best_combo[i-1])
                    #if duos_count < 3:
                    if i == 1:
                        if best_combo[i+1].partner != None:
                            best_combo[i].prev_opponents.append(best_combo[i+1])
                    if i == 3:
                        if best_combo[i-2].partner != None:
                            best_combo[i].prev_opponents.append(best_combo[i-2])
                    if i == 5:
                        if best_combo[i+1].partner != None:
                            best_combo[i].prev_opponents.append(best_combo[i+1])
                    if i == 7:
                        if best_combo[i-2].partner != None:
                            best_combo[i].prev_opponents.append(best_combo[i-2])
                    if i == 9:
                        best_combo[i].prev_opponents.append(best_combo[i+1])
                    if i == 11:
                        best_combo[i].prev_opponents.append(best_combo[i-2])

    def shuffle(lst):
        new_lst = []
        while len(lst) > 0:
            added_var = random.randint(0, len(lst)-1)
            new_lst.append(lst[added_var])
            lst.remove(lst[added_var])
        return new_lst




# Add players to be stored in the program here. Store them in the format: 
# name = Players("Name", skill level, singles)   
# Enter an integer for skill level. Higher number = higher skill. Enter True for willing to play singles and False for not willing.
# Examples:
# amelia = Players("Amelia", 6, False) 
# rob = Players("Rob", 8, True)


objects = []
inputs = []
active_players = []


print("Enter players one by one.\nIf you wish to add a new player, enter \"new\".\nIf you wish to stop entering players, enter \"stop\".\nHere are the players in the system:")
print("\nWomen: ") #put the names of all the women here if you wish for them to be displayed
print("\nMen: ")   #put the names of all the men here if you wish for them to be displayed

players_lst = [] #put every single player object name in the list, seperated by commas. Ex: [amelia, rob]
active_players = []
repeat = True
while repeat == True:
    response = input(f"\nEnter Player {len(active_players) + 1}: ")
    if "stop" in response.lower():
        repeat = False
    elif "new" in response.lower():
        name = input("Enter Player Name: ")
        skill = int(input("Enter skill level (1-15): "))
        singles = input("Will play singles? (\"Y\" or \"N\")")
        if "y" in singles.lower():
            singles = True
        elif "n" in singles.lower():
            singles = False
        player = Players(name, skill, singles)
        active_players.append(player)
    else:
        valid = False
        for player in players_lst:
            if player.name.lower() == response.lower().strip():
                active_players.append(player)
                valid = True
        if valid == False:
            print("Player not known")

rpt = True
while rpt == True:
    partners = input("Do any more players wish to play together? (\"Y\" or \"N\")" )
    if "y" in partners.lower():
        player1 = input("Which player has a partner?")
        player2 = input("Who is this player's partner?")
        valid = 0
        for player in active_players:
            if player.name.lower().strip() == player1:
                player1 = player
                valid += 1
            elif player.name.lower().strip() == player2:
                player2 = player  
                valid += 1  
        if valid == 2:
            player1.partner = player2
            player2.partner = player1
            print(f"{player1.name} and {player2.name} are partners.")
        elif valid == 1:
            print("You entered an invalid player")
        else:
            print("You entered invalid players")
    else:
        rpt = False


if len(active_players) < 8:
    print("Sorry not enough players. Please enter at least 8 players")
elif len(active_players) == 8:
    Players.shuffle8(active_players[0], active_players[1], active_players[2], active_players[3], active_players[4], active_players[5], active_players[6], active_players[7])
elif len(active_players) == 9:
    ("9 active players. Please remove or add a player and try again.")
elif len(active_players) == 10:
    Players.shuffle10(active_players[0], active_players[1], active_players[2], active_players[3], active_players[4], active_players[5], active_players[6], active_players[7], active_players[8], active_players[9])
elif len(active_players) == 11:
    Players.shuffle11(active_players[0], active_players[1], active_players[2], active_players[3], active_players[4], active_players[5], active_players[6], active_players[7], active_players[8], active_players[9], active_players[10])
elif len(active_players) == 12:
    Players.shuffle12(active_players[0], active_players[1], active_players[2], active_players[3], active_players[4], active_players[5], active_players[6], active_players[7], active_players[8], active_players[9], active_players[10], active_players[11])
else:
    print("Too many players. Enter at most 12 players")
