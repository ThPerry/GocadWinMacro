import winHandler
import winMacro
import auxFiles
import time

if __name__ == "__main__":
    windowName = 'NoMachine - ConexaoUFF'    

    # Initialize window handler
    winHndl = winHandler.Handler(windowName)

    # Initialize window macro
    macroHandler = winMacro.ApplicationMacro(winHndl.win, windowName)
    Mouse = winMacro.myMouse()

    # Read code fle
    addCode = auxFiles.CodeFile('gocad_Code.c')
    removeCode = auxFiles.CodeFile('gocad_Code.c')
    addCodeTxt = addCode.getCodeText()
    removeCodeTxt = removeCode.getCodeText()
    
    # macroHandler.printMousePosition()
    mainScript_position  = Mouse.getMouseClickPosition('Please enter the main script position...')
    applyButton_position = Mouse.getMouseClickPosition('Please enter the applyButton position...')

    #cellsFile = auxFiles.CellsFile('AddRemoveCells.txt')
    #addPositions = cellsFile.getAddCells()
    #removePositions = cellsFile.getRemoveCells()


    cellsFile = auxFiles.CellsFile('AddRemoveCells.txt')
    edgePositions = cellsFile.getAddCells()
    addPositions = []

    for pos in edgePositions:
        for j in range(pos[1] + 1, 123 + 1):
            addPositions.append([pos[0], j, pos[2]])


    progressCounter = 1
    for pos in addPositions:
        progressText = f'Adding {progressCounter} of {len(addPositions)} ...'
        print(progressText)
        
        # Print Header (Cell positino)
        macroHandler.clickAtPosition(mainScript_position)
        macroHandler.writeString(f'i = {pos[0]}; j = {pos[1]}; k = {pos[2]};\n')
      
        # Print code
        for line in addCodeTxt:
            macroHandler.writeString(line)

        # Execute code

        macroHandler.clickAtPosition(applyButton_position)

        # Erase main script buffer
        time.sleep(2)
        macroHandler.eraseMainScript(mainScript_position)

        progressCounter += 1



    