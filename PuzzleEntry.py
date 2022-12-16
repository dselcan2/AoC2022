import requests
import os


#day = "1"


class Puzzle:
    puzzleInput = ""

    def __init__(self, day):
        filesPath = "cachedInputs/"
        input = "input"
        file = day + "_" + input + ".txt"
        if os.path.exists(filesPath + file):
            with open(filesPath + file, 'r') as f:
                self.puzzleInput = f.read()
        else:
            URL = "https://adventofcode.com/2022/day/" + day + "/" + input
            session = requests.Session()
            cookie = "" #paste cookie in here
            response = requests.get(URL, cookies={"session": cookie})
            if response.status_code == 200:
                with open(filesPath + file, 'w') as f:
                    f.write(response.text)
                    self.puzzleInput = response.text

    def implementation(self, input:str):
        return

    def implementation2(self, input:str):
        return

    def runPuzzle(self):
        self.implementation(self.puzzleInput)

    def runPuzzle2(self):
        self.implementation2(self.puzzleInput)


#print(puzzleInput)

#open("instagram.ico", "wb").write(response.content)
#print(response.text)