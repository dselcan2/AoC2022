from PuzzleEntry import Puzzle


class Puzzle6(Puzzle):
    def implementation(self, input: str):
        curr = []
        i = 0
        for c in input:
            i += 1
            curr.append(c)
            if len(curr) > 4:
                print(curr)
                curr.remove(curr[0])
                if len(curr) == len(set(curr)):
                    print(i)
                    break


    def implementation2(self, input: str):
        curr = []
        i = 0
        for c in input:
            i += 1
            curr.append(c)
            if len(curr) > 14:
                print(curr)
                curr.remove(curr[0])
                if len(curr) == len(set(curr)):
                    print(i)
                    break
    

puzzle = Puzzle6("6")
puzzle.runPuzzle2()