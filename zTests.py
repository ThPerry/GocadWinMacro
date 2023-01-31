import auxFiles

cellsFile = auxFiles.CellsFile('AddRemoveCells.txt')
edgePositions = cellsFile.getAddCells()
addPositions = []

for pos in edgePositions:
    for j in range(pos[1] + 1, 123 + 1):
        addPositions.append([pos[0], j, pos[2]])


print(addPositions)