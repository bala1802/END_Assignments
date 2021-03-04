PYTHON_BLOCK_SEPERATOR = '#END_OF_CODE'
CSV_COLUMNS = ['Source', 'Target']

import csv

'''
Read Dataset from the text file
'''

def readDataSet(filePath):
    content = ""
    with open(filePath, 'r', encoding='utf-8') as content_file:
        content = content_file.read()
    return content

'''
Attach a custom Python Block Seperator
'''
def attachBlockSeperator(content):
    lines = content.splitlines()
    newLines = []
    for line in lines:
        tempLine = line.strip().lower()
        if tempLine.startswith('#') and (
                'write' in tempLine or 'program' in tempLine or 'function' in tempLine or 'python' in tempLine or 'driven code' in tempLine or 'convert' in tempLine or 'generate' in tempLine):
            newLines.append(PYTHON_BLOCK_SEPERATOR) 
        tempLine = line.strip()
        if tempLine != '':
            newLines.append(line)
    newLines.append(PYTHON_BLOCK_SEPERATOR)
    return newLines

'''
Maintain List of Blocks of list of lines.
[Block-1[Line-1, Line-2, ..., Line-N], Block-2[Line-1, Line-2, ..., Line-N],....., Block-N[Line-1, Line-2,...., Line-N]]
'''
def segregateBlocksOfLines(lines):
    blockOfLines = []
    newLines = []
    for line in lines:
        tempLine = line.strip()
        if tempLine != PYTHON_BLOCK_SEPERATOR:
            newLines.append(line)
        else:
            if len(newLines) > 0:
                blockOfLines.append(newLines)
                newLines = []
    return blockOfLines  

'''
Divide the lines of code into blocks
'''
def divideBlocks(blocksOfLines):
    blocks = []
    for blocksOfLine in blocksOfLines:
        block = ''
        for line in blocksOfLine:
            block = block + '\n' + line
        blocks.append(block)
    
    return blocks

'''
Segregate Source and Target from each block
'''
def segregateSourceTarget(pythonBlock):
    tempPythonBlock = pythonBlock.strip()
    sourceLines = tempPythonBlock.splitlines()
    newSourceLines = []
    for sourceLine in sourceLines:
        tempSourceLine = sourceLine.strip()
        if tempSourceLine.startswith('#'):
            newSourceLines.append(sourceLine)
        else:
            break
    print
    source = ' '.join(newSourceLines).replace('#', ' ').strip()
    target = pythonBlock
    for newSourceLine in newSourceLines:
        target = target.replace(newSourceLine, '')
    target = convertTargetToSingleLine(target)
    target = target.replace(':', ' : ')
    return source, target

'''
Convert the Target python block to single line of code, replacing the real newline by '\n', the real tab by '\t',

the spaces into equivalent amount of \t

example 4 spaces = 1 Tab
'''
def convertTargetToSingleLine(block) :
    lines = block.splitlines()
    newLines = ''
    for line in lines:
            tempLine = line.strip()
            if tempLine != '':
                num_spaces = 0
                
                for letter in line:
                    if letter != ' ':
                        break
                    num_spaces += 1
                
                if num_spaces % 20 == 0:
                    line = line.replace(' '*20, '\t\t\t\t\t') #If number of Spaces is 20, replace with five tab
                elif num_spaces % 19 == 0:
                    line = line.replace(' '*19, '\t\t\t\t\t') #If number of Spaces is 19, replace with five tab
                elif num_spaces % 18 == 0:
                    line = line.replace(' '*18, '\t\t\t\t\t') #If number of Spaces is 18, replace with five tab
                elif num_spaces % 17 == 0:
                    line = line.replace(' '*17, '\t\t\t\t\t') #If number of Spaces is 17, replace with five tab
                elif num_spaces % 16 == 0:
                    line = line.replace(' '*16, '\t\t\t\t') #If number of Spaces is 16, replace with four tab
                elif num_spaces % 15 == 0:
                    line = line.replace(' '*15, '\t\t\t\t') #If number of Spaces is 15, replace with four tab
                elif num_spaces % 14 == 0:
                    line = line.replace(' '*14, '\t\t\t\t') #If number of Spaces is 14, replace with four tab
                elif num_spaces % 13 == 0:
                    line = line.replace(' '*13, '\t\t\t\t') #If number of Spaces is 13, replace with four tab
                elif num_spaces % 12 == 0:
                    line = line.replace(' '*12, '\t\t\t') #If number of Spaces is 12, replace with triple tab
                elif num_spaces % 11 == 0:
                    line = line.replace(' '*11, '\t\t\t') #If number of Spaces is 11, replace with triple tab
                elif num_spaces % 10 == 0:
                    line = line.replace(' '*10, '\t\t\t') #If number of Spaces is 10, replace with triple tab
                elif num_spaces % 9 == 0:
                    line = line.replace(' '*9, '\t\t\t') #If number of Spaces is 9, replace with triple tab
                elif num_spaces % 8 == 0:
                    line = line.replace(' '*8, '\t\t') #If number of Spaces is 8, replace with double tab
                elif num_spaces % 7 == 0:
                    line = line.replace(' '*7, '\t\t') #If number of Spaces is 7, replace with a double tab
                elif num_spaces % 6 == 0:
                    line = line.replace(' '*5, '\t\t') #If number of Spaces is 7, replace with a double tab
                elif num_spaces % 5 == 0:
                    line = line.replace(' '*5, '\t\t') #If number of Spaces is 5, replace with a double tab
                elif num_spaces % 4 == 0:
                    line = line.replace(' ' *4, '\t') #If number of Spaces is 4, replace with single tab
                elif num_spaces % 3 == 0:
                    line = line.replace(' ' * 3, '\t') #If number of Spaces is 3, replace with a single tab
                elif num_spaces % 2 == 0:
                    line = line.replace(' ' * 2, '\t') #If number of Spaces is 2, replace with a single tab
                elif num_spaces % 1 == 0:
                    line = line.replace(' ' * 1, '\t') #If number of Spaces is 1, replace with a single tab
                
                newLines = newLines + '\n' + line
            
    converted = repr(newLines)
    return converted

'''
Populate the Dataset into CSV format
'''
def populateDataSetCSV(tuplesList):
    with open('English_Python_DataSet.csv', 'w', encoding='utf-8', newline = '') as out:
         csv_out=csv.writer(out)
         csv_out.writerow(CSV_COLUMNS)
         for row in tuplesList:
             csv_out.writerow(row)
    return

'''
Process the input file
'''
def process(filePath):
    content = readDataSet(filePath)
    lines = attachBlockSeperator(content)
    
    blocksOfLines = segregateBlocksOfLines(lines)
    blocks = divideBlocks(blocksOfLines)
    
    tuplesList = []
    for block in blocks:
        tempBlock = block.strip()
        if tempBlock != '':
            source, target = segregateSourceTarget(block)
            data = (source, target)
            tuplesList.append(data)
    populateDataSetCSV(tuplesList)


process("english_python_dataset.txt")
