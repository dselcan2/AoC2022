from PuzzleEntry import Puzzle
import re


class Puzzle5(Puzzle):
    def implementation(self, input: str):
        inp = input.split('\n')

        #Get Fisrt part of input
        startInput = []
        for i in range(0, 8):
            startInput.append(inp[i])
        print("step 1 done")

        matrix = []

        #parse input into 7x7 matrix
        for row in startInput:
            idx = 0
            elem = ''
            rowMatrix = []
            for char in row:
                if idx % 4 == 0 or idx == len(row)-1:
                    if elem != '':
                        insert = elem[0:3]
                        if idx == len(row)-1:
                            if elem[1] == ' ':
                                insert = elem + ' '
                            else:
                                insert = elem+']'
                        rowMatrix.insert(len(rowMatrix), insert)
                    elem = ''
                elem += char
                idx += 1
            matrix.insert(len(matrix), rowMatrix)
        print("step 2 done")

        #parse 7x7 matrix into 7 stacks
        stacks = []
        for stack in range(0, len(matrix[0])):
            stck = []
            for row in range(0, len(matrix)):
                if matrix[row][stack] != '   ':
                    stck.insert(0, matrix[row][stack])
            stacks.insert(len(stacks), stck)
        print("step 3 done")

        secondInput = []
        for i in range(10, len(inp)):
            secondInput.append(inp[i])
        print("step 4 done")

        for command in secondInput:
            if command == '':
                continue
            nums = re.findall(r'\d+', command) #Regex that returns all the numbers in a string to an array ... "move 3 from 4 to 6" => ["3", "4", "6"]
            for i in range(0, int(nums[0])):
                stacks[int(nums[2])-1].append(stacks[int(nums[1])-1].pop())
        output = ""
        for stack in stacks:
            output += stack[len(stack)-1]
        output = output.replace('[', '')
        output = output.replace(']', '')
        print(output) #QMBMJDFTD


    #TODO
    def implementation2(self, input: str):
        return super().implementation2(input)

p = Puzzle5('5')
p.runPuzzle()