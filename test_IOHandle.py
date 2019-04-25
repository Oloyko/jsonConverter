import unittest
import IOHandle
from contextlib import redirect_stdout
import io
import json
from pathlib import Path


class SetUp():
    """This class simulates the ArgParse class"""

    def __init__(self, argList):
        self.userName: str = argList[0]
        self.printerName: str = argList[1]
        self.inputFile: str = argList[2]
        self.outputFile: str = argList[3]

    def prepareInput(self, inputstring: str) -> None:
        with open(Path('input.txt'), 'w') as inputFile:
            print(inputstring, file=inputFile)

    def redirectOut(self, setUp: 'SetUp') -> io.StringIO:
        realOut = io.StringIO()
        with redirect_stdout(realOut):
            IOHandle.IOHandle(setUp)
        return realOut

    def prepareTestDict(self, setUp: 'SetUp', testString: str) -> dict:
        return {'userName': setUp.userName,
                'printerName': setUp.printerName,
                'data': testString}


class TestIOHandle(unittest.TestCase):
    """Test class for the module that handles IO and letter counting"""

    def assertOut(self, correctOut: str, setUp: 'SetUp') -> None:
        realOut = setUp.redirectOut(setUp)
        self.assertEqual(realOut.getvalue(), correctOut)

    def assertJson(self, correctJson: dict) -> None:
        with open(Path('out.json'), 'r') as outFile:
            realJson = json.load(outFile)
            self.assertDictEqual(realJson, correctJson)

    def test_correctParams_lowerAsciiIn(self):
        setUp = SetUp(list(['Lukas', 'printer1', Path('input.txt'), Path('out.json')]))
        testString = 'this is a test string'
        correctOut = 'a:1\ne:1\ng:1\nh:1\ni:3\nn:1\nr:1\ns:4\nt:4\n'

        correctJson = setUp.prepareTestDict(setUp, testString)
        setUp.prepareInput(testString)

        self.assertOut(correctOut, setUp)
        self.assertJson(correctJson)

    def test_correctParams_whiteSpcIn(self):
        setUp = SetUp(list(['mQqzdU*u', 'bHw^!^uJ', Path('input.txt'), Path('out.json')]))
        testString = ' \n \t '
        correctOut = ''

        correctJson = setUp.prepareTestDict(setUp, testString)
        setUp.prepareInput(testString)

        self.assertOut(correctOut, setUp)
        self.assertJson(correctJson)

    def test_correctParams_upperAsciiIn(self):
        setUp = SetUp(list(['gL&XDe*i', '3sdmXc!j', Path('input.txt'), Path('out.json')]))
        testString = 'DONT COUNT THIS BUT this'
        correctOut = 'h:1\ni:1\ns:1\nt:1\n'

        correctJson = setUp.prepareTestDict(setUp, testString)
        setUp.prepareInput(testString)

        self.assertOut(correctOut, setUp)
        self.assertJson(correctJson)

    def test_correctParams_NonAsciiIn(self):
        setUp = SetUp(list(['PN!sT5fS', 'Wd&V^v4G', Path('input.txt'), Path('out.json')]))
        testString = 'Èěščřžýáíétest'
        correctOut = 'e:1\ns:1\nt:2\n'

        correctJson = setUp.prepareTestDict(setUp, testString)
        setUp.prepareInput(testString)

        self.assertOut(correctOut, setUp)
        self.assertJson(correctJson)

    def test_correctParams_emptyIn(self):
        setUp = SetUp(list(['pm6KqL2R', 'lQ*&W1oa', Path('input.txt'), Path('out.json')]))
        testString = ''
        correctOut = ''

        correctJson = setUp.prepareTestDict(setUp, testString)
        setUp.prepareInput(testString)

        self.assertOut(correctOut, setUp)
        self.assertJson(correctJson)

    def test_correctParams_numbersIn(self):
        setUp = SetUp(list(['A7sZ8nVy', 'yoABr&vm', Path('input.txt'), Path('out.json')]))
        testString = '0123456789nubmers'
        correctOut = 'b:1\ne:1\nm:1\nn:1\nr:1\ns:1\nu:1\n'

        correctJson = setUp.prepareTestDict(setUp, testString)
        setUp.prepareInput(testString)

        self.assertOut(correctOut, setUp)
        self.assertJson(correctJson)

    def test_correctParams_chineseIn(self):
        setUp = SetUp(list(['@Ye1Pp2L', 'L^eC@AnZ', Path('input.txt'), Path('out.json')]))
        testString = '形声字形聲字'
        correctOut = ''

        correctJson = setUp.prepareTestDict(setUp, testString)
        setUp.prepareInput(testString)

        self.assertOut(correctOut, setUp)
        self.assertJson(correctJson)

    def test_correctParams_combinedIn(self):
        setUp = SetUp(list(['Nrz#tAaC', 'J2yaTPEk', Path('input.txt'), Path('out.json')]))
        testString = '形声字形聲字 123 !@#$%^&*()_+{}:"|>?|}"+ěščřžýáíé=INcorrect'
        correctOut = 'c:2\ne:1\no:1\nr:2\nt:1\n'

        correctJson = setUp.prepareTestDict(setUp, testString)
        setUp.prepareInput(testString)

        self.assertOut(correctOut, setUp)
        self.assertJson(correctJson)

    def test_incorrectInFile(self):
        setUp = SetUp(list(['KPxM$!94', '!Dz@d1s7', Path('iDontExist.err'), Path('out.json')]))
        testString = ''
        correctOut = ''

        correctJson = setUp.prepareTestDict(setUp, testString)
        setUp.prepareInput(testString)

        self.assertRaises(FileNotFoundError)


if __name__ == '__main__':
    unittest.main()
