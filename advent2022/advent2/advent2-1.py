
ROCK     = 1
PAPER    = 2
SCISSORS = 3

WIN     = 6
DRAW    = 3
LOSS    = 0

def calcScore(round: str) -> int:
    if   round == "A X": 
        return ROCK + DRAW 
    elif round == "A Y": 
        return PAPER + WIN 
    elif round == "A Z": 
        return SCISSORS + LOSS
    elif round == "B X": 
        return ROCK + LOSS
    elif round == "B Y": 
        return PAPER + DRAW
    elif round == "B Z": 
        return SCISSORS + WIN
    elif round == "C X": 
        return ROCK + WIN
    elif round == "C Y": 
        return PAPER + LOSS
    elif round == "C Z": 
        return SCISSORS + DRAW


def calcScore2(round: str) -> int:
    if   round == "A X": 
        return LOSS + SCISSORS 
    elif round == "A Y": 
        return DRAW + ROCK
    elif round == "A Z": 
        return WIN + PAPER
    elif round == "B X": 
        return LOSS + ROCK
    elif round == "B Y": 
        return DRAW + PAPER
    elif round == "B Z": 
        return WIN + SCISSORS
    elif round == "C X": 
        return LOSS + PAPER
    elif round == "C Y": 
        return DRAW + SCISSORS
    elif round == "C Z": 
        return WIN + ROCK



with open("data.txt", "r") as data:
    score = sum([calcScore2(x[:3]) for x in data.readlines()])

print(score)