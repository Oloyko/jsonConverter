import argparse
from pathlib import Path


class ArgParse(object):
    """Loads and checks the script parameters"""

    def __init__(self):
        self.args = self.parseArgs()

        self.userName: str = self.args.userName
        self.printerName: str = self.args.printerName
        self.checkEmptyName()

        self.inputFile: str
        self.outputFile: str
        self.resolveFilePath()

    def parseArgs(self) -> argparse:
        args = argparse.ArgumentParser()
        args.add_argument('-u', '--userName', type=str, required=True,
                                help='A name of the user.')
        args.add_argument('-p', '--printerName', type=str, required=True,
                                help='A name of the printer.')
        args.add_argument('-i', '--inputPath', type=str, required=True,
                                help='A path to the file with the input data.')
        args.add_argument('-o', '--outputPath', type=str, required=True,
                                help='A path to the JSON file with the output data.')
        self.help = args.print_help
        return args.parse_args()

    def resolveFilePath(self) -> None:
        self.checkEmptyFile()
        self.inputFile = Path(self.args.inputPath)
        self.outputFile = Path(self.args.outputPath)

    def checkEmptyName(self) -> None:
        if not self.userName:
            self.help()
            raise ValueError('userName must not be empty')
        if not self.printerName:
            self.help()
            raise ValueError('printerName must not be empty')

    def checkEmptyFile(self) -> None:
        if not self.args.inputPath:
            self.help()
            raise ValueError('inputFile must not be empty')
        if not self.args.outputPath:
            self.help()
            raise ValueError('outputFile must not be empty')
        if not self.args.outputPath.endswith('.json'):
            self.help()
            raise TypeError('The output file must be the JSON format (.json)')
