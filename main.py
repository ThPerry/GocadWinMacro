import winHandler
import winMacro
import auxFiles

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


    cellsFile = auxFiles.CellsFile('AddRemoveCells.txt')
    addPositions = cellsFile.getAddCells()
    
    #addPositions = []
    #for pos in edgePositions:
    #    for i in range(pos[0], 125 + 1):
    #        addPositions.append([i, pos[1], pos[2]])

    ## Execute script
    GocadMacroHandler.executeScriptOnListedCells(addPositions, addCodeTxt)
        