from PuzzleEntry import Puzzle


class Puzzle1(Puzzle):
    def implementation(self, input:str):
        sections = input.split('\n\n')
        max = 0
        for s in sections:
            strings = s.split('\n')
            if '' in strings:
                strings.remove('')
            addition = 0
            for n in strings:
                addition += int(n)
            if addition > max:
                max = addition
        print(max)

    def implementation2(self, input: str):
        sections = input.split('\n\n')
        vals = []
        for s in sections:
            strings = s.split('\n')
            if '' in strings:
                strings.remove('')
            addition = 0
            for n in strings:
                addition += int(n)
            vals.insert(0, addition)
        vals.sort(reverse=True)
        print(vals[0])
        print(vals[1])
        print(vals[2])
        print(vals[0] + vals[1] + vals[2])
        

p = Puzzle1("1")
#p.runPuzzle()
p.runPuzzle2()
