import random

def isValidValue(value, teams):
    if int(value) % int(teams) == 0:
        return True
    else:
        return False


def makeTeams(teamDict, numTeams):
    x = random.randint(0, len(list(teamDict)) - 1)
    teamSize = len(list(teamDict)) - 1 / int(numTeams)
    taken = []

    for player in teamDict:
        if player in taken:
            continue
        else:



    print(list(teamDict)[x])


def main():
    numTeams = input("Please enter the number of teams: ")

    f = open("roster.txt", "r")
    teamDict = {}
    totalValue = 0

    for i in f:
        player = i.strip().split(",")
        totalValue += int(player[1])
        teamDict[player[0]] = player[1]

    if isValidValue(totalValue, numTeams) == False:
        print("The total value of players has to be divisible by: " + numTeams)
        return

    makeTeams(teamDict, numTeams)
    # print(teamDict)



if __name__ == '__main__':
    main()
