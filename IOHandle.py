from sys import stderr, stdout
import json


class IOHandle(object):
    """Opens up the input and output file
    Reads the input file
    Counts the occurence of a letter
    Outputs into the json file"""

    def __init__(self, argsObj):
        self.jsonOutput: dict = {}
        self.letterCount: dict = {}
        self.args = argsObj
        self.dataOutput: str = ''
        self.openFiles()

    def output2JsonFile(self) -> None:
        self.jsonOutput['userName'] = self.args.userName
        self.jsonOutput['printerName'] = self.args.printerName
        self.jsonOutput['data'] = self.dataOutput
        json.dump(self.jsonOutput, self.args.outputFile, indent=2)

    def readInput(self) -> str:
        data: str = ''
        for line in self.args.inputFile:
            # I was thinking about iterative writing to the output file
            # But it took 0.14 seconds and 3MB RAM to convert 670 000 characters
            # long file to json and count its letters occurence
            data += line
            self.countLetters(line)
        self.printLetters()
        return data

    def countLetters(self, line: str) -> None:
        line = line.encode("ascii", errors="ignore").decode()
        for char in line:
            if char.isalpha() and char.islower():
                if char in self.letterCount:
                    self.letterCount[char] += 1
                else:
                    self.letterCount[char] = 1

    def printLetters(self) -> None:
        for key in sorted(self.letterCount):
            print("{}:{}".format(key, self.letterCount[key]))

    def openFiles(self) -> None:
        with open(self.args.inputFile, 'r') as inputFile, open(self.args.outputFile, 'w') as outputFile:
            self.args.inputFile = inputFile
            self.args.outputFile = outputFile
            self.dataOutput = self.readInput()
            if self.dataOutput[-1:].isspace():
                self.dataOutput = self.dataOutput[:-1]
            self.output2JsonFile()
