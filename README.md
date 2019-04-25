## Overview

Simple script that counts the occurence of lower case ascii letters stored in the input file. It also creates an output JSON file that contains the username, printer name and the data from the input file.

## Getting Started

### Dependencies

Python 3.6 with standard libraries.

### Installing

Clone the git repository into your system.

### Executing program

Go to the folder where the source code files are located:
```
python3 main.py --userName 'userName' --printerName 'printerName' --inputPath 'inputPath' --outputPath 'outputPath'
```

Example for the input.txt file containing "example":
```
python3 main.py --userName exampleName --printerName printer1 --inputPath input.txt --outputPath output.json


stdout:
a:1
e:2
l:1
m:1
p:1
x:1

output.json file:
{
  "userName": "exapmleName",
  "printerName": "printer1",
  "data": "example"
}
```
### Executing unit tests

Go to the folder where the source code files are located:
```
python3 -m unittest
```

## Help

```
python3 main.py -h
```

