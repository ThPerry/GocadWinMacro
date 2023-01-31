from re import X

from pynput.mouse import Listener
import pygetwindow
import pyautogui
import time

class myMouse():
    def __init__(self):
        # Mouse click position
        self._click         = False
        self._clickPos_x    = None
        self._clickPos_y    = None

    def getMouseClickPosition(self, questionText):

        def on_click(x,y,button, pressed):
            if pressed:
                self._click = pressed
                self._clickPos_x = x
                self._clickPos_y = y
            return

        listener = Listener(on_click=on_click)

        while not self._click:
            if not listener.is_alive() and not self._click:
                print(questionText)
                listener.start()
            
            if listener.is_alive() and self._click:
                listener.stop()

        self._click = False

        print(self._clickPos_x, self._clickPos_y)

        return [self._clickPos_x, self._clickPos_y]

class ApplicationMacro():
    def __init__(self, win, applicationName):
        self._aplicationName = applicationName
        self._win = win

    def clickAtPosition(self, xy_array):
        pyautogui.moveTo(xy_array[0], xy_array[1])
        pyautogui.click(xy_array[0], xy_array[1])

    def _bringApplicationWindowToFront(self):
        applicationWinton = pygetwindow.getWindowsWithTitle(self._aplicationName)[0]
        applicationWinton.activate()
        
    def _getFowardWindow(self):
        return pygetwindow.getWindowsAt(10, 10)[0]

    def sendChar(self, c):
        fowardWindow = self._getFowardWindow()

        if fowardWindow.title != self._aplicationName:
            self._bringApplicationWindowToFront()
            time.sleep(0.5)
            pyautogui.hotkey(c)
        else:
            pyautogui.hotkey(c)

    def writeString(self, string):
        fowardWindow = self._getFowardWindow()

        if fowardWindow.title != self._aplicationName:
            self._bringApplicationWindowToFront()
            time.sleep(0.5)
            pyautogui.write(string, interval = 0.01)
        else:
            pyautogui.write(string, interval = 0.01)

    def printMousePosition(self):
        print(pyautogui.displayMousePosition())

    

class GocadApplicationMacro(ApplicationMacro):
    def __init__(self, win, applicationName):
        super().__init__(win, applicationName)
        
        self.mouse = myMouse()
        self.mainScript_Location = None
        self.applyButton_Location = None

    def getMainScript_Location(self):
        self.mainScript_Location = self.mouse.getMouseClickPosition('Please click at the main script position...')

    def getApplyButton_Location(self):
        self.applyButton_Location = self.mouse.getMouseClickPosition('Please click at the applyButton position...')

    def eraseMainScript(self):
        self.clickAtPosition(self.mainScript_Location)
        pyautogui.keyDown('ctrl')
        pyautogui.hotkey('a')
        pyautogui.keyUp('ctrl')
        pyautogui.hotkey('backspace')

    def writeMainScript(self, MainsScriptCode_Txt):
        self.clickAtPosition(self.mainScript_Location)
        
        for line in MainsScriptCode_Txt:
            self.writeString(line)

    def executeScript(self):
        self.clickAtPosition(self.applyButton_Location)

    def executeScriptOnListedCells(self, cells_List, ScriptCode_txt):
        self.getMainScript_Location()
        self.getApplyButton_Location()

        # include cell position on the first line of the script
        ScriptCode_txt.insert(0, f'i = 0; j = 0; k = 0;\n')

        progress_counter = 1
        
        for pos in cells_List:
            print(f'Adding {progress_counter} of {len(cells_List)} ...')

            # Update cell position at first line of the script
            ScriptCode_txt[0] = f'i = {pos[0]}; j = {pos[1]}; k = {pos[2]};\n'

            # Write main script
            self.writeMainScript(ScriptCode_txt)

            # Execute script
            self.executeScript()
            time.sleep(2)

            # Erase main script text box
            self.eraseMainScript()

            progress_counter += 1






