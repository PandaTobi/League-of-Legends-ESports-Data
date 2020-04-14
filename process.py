# -*- coding: utf-8 -*-
"""
Recorded Values:
Winrate	[X]
KDA Avg.
CS per min [X]
Gold per min [X]
%DMG [X]
"""
import operator

output = open("league_pro_play_data.csv", "r")

roles = {}
gamesDICT = {}
csmDICT = {}
winrDICT = {}
gpmDICT = {}
dmgDICT = {}
kdaDICT = {}

#Adding each data point to their respective dictionaries.
def add_stat(stat, DICT, role, games):
        stat = float(stat)
        if role in DICT:
            DICT[role] += float(games) * stat
        else:
            DICT[role] = float(games) * stat

#Just a handy little function for converting percent
def percent2float(p):
    return float(p.strip('%'))/100

def average(stats_dict):
    for i in stats_dict:
        stats_dict[i] = stats_dict[i]/roles[i]

def print_stats(stats_dict, stat):
    for i in roles:
        print("Professional {} players: {}: ".format(i, stat))
        print(stats_dict[i])
    print("\n")

def maxStat(stats, stat):
    maxRole = max(stats.items(), key=operator.itemgetter(1))[0]
    print("In terms of {}, {} players have the most impact, at {} on average, per game. "
          .format(stat, maxRole, stats[maxRole]))           

    
for i in output:
    role = i.split(",")[1]
    games = i.split(",")[2]
    winr = i.split(",")[3]
    kda = i.split(",")[4]
    csm = i.split(",")[8]
    gpm = i.split(",")[9]
    dmg = i.split(",")[10]
    
    #Counting up the number of players that play each role
    if role == "" or role == "Role" or gpm == "-":
        continue
    elif role in roles:
        games = float(games)
        roles[role] += games
    else:
        games = float(games)
        roles[role] = games
    
    if kda == "-":
        kda = float(i.split(",")[5]) + float(i.split(",")[7])
    
    add_stat(percent2float(winr), winrDICT, role, games)
    add_stat(csm, csmDICT, role, games)
    add_stat(gpm, gpmDICT, role, games)
    add_stat(dmg, dmgDICT, role, games)
    add_stat(kda, kdaDICT, role, games)
    
#Averaging the stats 
average(csmDICT)
average(winrDICT)
average(gpmDICT)
average(dmgDICT)
average(kdaDICT)

print_stats(winrDICT, "Winrate")
print_stats(gpmDICT, "Gold per min")
print_stats(dmgDICT, "%DMG of team")
print_stats(kdaDICT, "KDA average")

maxStat(winrDICT, "Winrate")
maxStat(gpmDICT, "Gold per min")
maxStat(dmgDICT, "%DMG of team")
maxStat(kdaDICT, "KDA average")