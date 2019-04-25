import unittest
import sys
import ArgParse
from pathlib import Path


def setUp(argsList):
    return ['--userName', argsList[0],
            '--printerName', argsList[1],
            '--inputPath', argsList[2],
            '--outputPath', argsList[3]]


class argParseTestCase(unittest.TestCase):
    """Test class for the argument parsing module"""

    def assertName(self, correctName: str, realName: str) -> None:
        self.assertEqual(correctName, realName)

    def assertPath(self, correctPath: str, realPath: str) -> None:
        correctPath = Path(correctPath)
        self.assertEqual(correctPath, realPath)

    def test_correctArgs(self) -> None:
        argsList = ['UserName123', 'printer1@asdf', 'input.txt', 'out.json']
        sys.argv[1:] = setUp(argsList)
        args = ArgParse.ArgParse()
        self.assertName(argsList[0], args.userName)
        self.assertName(argsList[1], args.printerName)
        self.assertPath(argsList[2], args.inputFile)
        self.assertPath(argsList[3], args.outputFile)

    def test_correctArgsShort(self) -> None:
        argsList = ['L', 'p', 'i.txt', 'o.json']
        sys.argv[1:] = setUp(argsList)
        args = ArgParse.ArgParse()
        self.assertName(argsList[0], args.userName)
        self.assertName(argsList[1], args.printerName)
        self.assertPath(argsList[2], args.inputFile)
        self.assertPath(argsList[3], args.outputFile)

    def test_wrongOutFormat(self) -> None:
        argsList = ['UserName123', 'printer1@asdf', 'input.txt', 'out.jsn']
        sys.argv[1:] = setUp(argsList)
        try:
            ArgParse.ArgParse()
        except TypeError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_emptyName(self) -> None:
        argsList = ['', 'printer1', 'input.txt', 'out.json']
        sys.argv[1:] = setUp(argsList)
        try:
            ArgParse.ArgParse()
        except ValueError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_emptyPrinter(self) -> None:
        argsList = ['Lukas', '', 'input.txt', 'out.json']
        sys.argv[1:] = setUp(argsList)
        try:
            ArgParse.ArgParse()
        except ValueError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_emptyInFile(self) -> None:
        argsList = ['Lukas', 'printer1', '', 'out.json']
        sys.argv[1:] = setUp(argsList)
        try:
            ArgParse.ArgParse()
        except ValueError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_emptyOutFile(self) -> None:
        argsList = ['Lukas', 'printer1', 'input.txt', '']
        sys.argv[1:] = setUp(argsList)
        try:
            ArgParse.ArgParse()
        except ValueError:
            self.assertTrue(True)
        else:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
