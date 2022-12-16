from PuzzleEntry import Puzzle
import string

class Puzzle3(Puzzle):

    priorityArr = []

    def __init__(self, day):
        self.priorityArr = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        super().__init__(day)


    def implementation(self, input: str):
        backpacks = input.split('\n')
        allTogether = 0
        for backpack in backpacks:
            if backpack == '':
                continue
            length = len(backpack)
            sep = int(len(backpack)/2)
            left = backpack[0:sep]
            right = backpack[sep:len(backpack)]
            duplicate = ''
            for char in left:
                for c in right:
                    if char == c:
                        duplicate = char
            print(self.priorityArr.index(duplicate)+1)
            allTogether += (self.priorityArr.index(duplicate)+1)
        print(allTogether)

    def implementation2(self, input: str):
        backpacks = input.split('\n')
        all = 0
        for i in range(len(backpacks)):
            if backpacks[i] == '':
                continue
            if i % 3 == 0:
                first = backpacks[i]
                second = backpacks[i+1]
                third = backpacks[i+2]
                potencials = []
                duplicate = ''
                for char in first:
                    for c in second:
                        if(char == c):
                            potencials.insert(0, c)
                for c in third:
                    for char in potencials:
                        if c == char:
                            duplicate = c
                print((self.priorityArr.index(duplicate)+1))
                all += (self.priorityArr.index(duplicate)+1)
        print(all)

p = Puzzle3("3")
p.runPuzzle2()