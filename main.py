import winHandler
import winMacro
import auxFiles
import time

if __name__ == "__main__":
    windowName = 'NoMachine - ConexaoUFF'    

    # Initialize window handler
    winHndl = winHandler.Handler(windowName)

    # Initialize window macro
    GocadMacroHandler = winMacro.GocadApplicationMacro(winHndl.win, windowName)

    # Read code fle
    addCode = auxFiles.CodeFile('gocad_Code.c')
    removeCode = auxFiles.CodeFile('gocad_Code.c')
    addCodeTxt = addCode.getCodeText()
    removeCodeTxt = removeCode.getCodeText()
    
    #cellsFile = auxFiles.CellsFile('AddRemoveCells.txt')
    #addPositions = cellsFile.getAddCells()
    #removePositions = cellsFile.getRemoveCells()

    cellsFile = auxFiles.CellsFile('AddRemoveCells.txt')
    edgePositions = cellsFile.getAddCells()
    addPositions = []

    for pos in edgePositions:
        for j in range(pos[1] + 1, 123 + 1):
            addPositions.append([pos[0], j, pos[2]])

    ## Execute script
    GocadMacroHandler.executeScriptOnListedCells(addPositions, addCodeTxt)




    