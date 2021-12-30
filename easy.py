# Number 2
def isValidSubsequence(array, sequence):
    i= 0
    j= 0
    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            j+= 1
        i+= 1
    if j == len(sequence):
        return True
    return False

# print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8], [22, 25, 6])

def tournamentWinner(competitions, results):
    highScore= 0
    winner= ""
    scoreboard= {}
    for i in range(len(competitions)):
        hometeam= competitions[i][0]
        awayteam= competitions[i][1]
        winningteam= hometeam if results[i] == 1 else awayteam
        if winningteam not in scoreboard:
            scoreboard[winningteam]= 0
        scoreboard[winningteam]+= 3
    for key, val in scoreboard.items():
        if val > highScore:
            highScore=val
            winner= key
    return winner

competitions= [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results= [0, 0, 1]

# print(tournamentWinner(competitions, results))

def productSum(array, sums=0, mult=1):
    for i in range(len(array)):
        if array[i] == type(list):
            productSum(array[i], sums, mult+1)
        sums+= array[i]*mult
    return sums

print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))