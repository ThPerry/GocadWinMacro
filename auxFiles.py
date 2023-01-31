import os

class _AuxFile():
    def __init__(self, fileName):
        self._fileName = fileName
        self._inFile = None
        self.textContent = ''

    def _openFile(self):
        if os.path.exists(self._fileName):
            self._inFile = open(self._fileName, 'r')
            return True
        else:
            print(f'No such file: \'{self._fileName}\'')
            return False

    def _closeFile(self):
        if self._inFile != None:
            self._inFile.close()
        else:
            pass

    def _readFileContent(self):
        if self._openFile:
            return self._inFile.readlines()

            
class CodeFile(_AuxFile):
    def __init__(self, fileName):
        super().__init__(fileName)

    def getCodeText(self):
        self._openFile()
        text = self._readFileContent()
        self._closeFile()
        return text

class CellsFile(_AuxFile):
    def __init__(self, fileName):
        super().__init__(fileName)
        self._content = ''
        self._getFileContent()
        self._nLines = len(self._content)
    
    def _getFileContent(self):
        self._openFile()
        self._content = self._readFileContent()
        self._closeFile()

    def getAddCells(self):
        addCells = []
        linePos = -1

        for i in range(0,self._nLines):
            if self._content[i][:-1] == '# Add cells':
                linePos = i + 2
                break
            
        while linePos < self._nLines and self._content[linePos][:-1] != "":
            addCells.append([int(n) for n in self._content[linePos].split(' ')])
            linePos += 1
        
        return addCells

    def getRemoveCells(self):
        removeCells = []
        linePos = -1

        for i in range(0,self._nLines):
            if self._content[i][:-1] == '# Remove cells':
                linePos = i + 2
                break
            
        while linePos < self._nLines and self._content[linePos][:-1] != "":
            removeCells.append([int(n) for n in self._content[linePos].split(' ')])
            linePos += 1
        
        return removeCells
