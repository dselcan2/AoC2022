from PuzzleEntry import Puzzle


class Puzzle4(Puzzle):

    def implementation(self, input: str):
        rows = input.split('\n')
        count = 0
        for row in rows:
            if row == '':
                continue
            assignments = row.split(',')
            a1 = assignments[0].split('-')
            a2 = assignments[1].split('-')

            l1 = int(a1[0])
            l2 = int(a2[0])

            h1 = int(a1[1])
            h2 = int(a2[1])

            firstLonger = False

            if h1-l1 > h2-l2:
                firstLonger = True

            if firstLonger:
                if l1 <= l2 and h1 >= h2:
                    count += 1
            else: 
                if l2 <= l1 and h2 >= h1:
                    count += 1
        print(count)


    def implementation2(self, input: str):
        rows = input.split('\n')
        count = 0
        for row in rows:
            if row == '':
                continue
            assignments = row.split(',')
            a1 = assignments[0].split('-')
            a2 = assignments[1].split('-')

            l1 = int(a1[0])
            l2 = int(a2[0])

            h1 = int(a1[1])
            h2 = int(a2[1])

            s1 = [x for x in range(l1, h1+1)]
            s2 = [x for x in range(l2, h2+1)]

            for i in s1:
                if i in s2:
                    count += 1
                    break
        print(count)


p = Puzzle4('4')
p.runPuzzle2()