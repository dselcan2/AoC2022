from PuzzleEntry import Puzzle

# A - X = Rock
# B - Y = Paper
# C - Z = Scissors

class Puzzle2(Puzzle):

    points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    mappings = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }

    def implementation(self, input:str):
        beats = {
            "X": "C",
            "Y": "A",
            "Z": "B"
        }
        
        
        cumulativePoints = 0
        rounds = input.split('\n')
        count = 0
        for round in rounds:
            played = round.split(' ')
            if len(played) != 2:
                continue
            roundPoints = 0
            if self.mappings[played[0]] == played[1]:
                roundPoints += 3
            elif beats[ played[1] ] == played[0]:
                roundPoints += 6
            else:
                roundPoints += 0
            roundPoints += self.points[played[1]]
            cumulativePoints += roundPoints
        print(cumulativePoints)

    def implementation2(self, input:str):
        rounds = input.split('\n')
        toLose= {
            "A": "Z",
            "B": "X",
            "C": "Y"
        }
        toWin = {
            "A": "Y",
            "B": "Z",
            "C": "X"
        }
        allTogether = 0
        for round in rounds:
            roundPoints = 0
            played = round.split(' ')
            if len(played) != 2:
                continue
            wonSym = ''
            if played[1] == 'Y': #Draw
                roundPoints += 3
                wonSym = self.mappings[played[0]]
            elif played[1] == 'X': #Loose
                wonSym = toLose[played[0]]
            else:
                roundPoints += 6
                wonSym = toWin[played[0]]
            roundPoints += self.points[wonSym]
            print(roundPoints)
            allTogether += roundPoints
        print(allTogether)

p = Puzzle2("2")

p.runPuzzle2()
#p.runPuzzle2()