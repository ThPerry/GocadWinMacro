from re import X
from PIL import Image

from pynput.mouse import Listener
import pygetwindow
import pyautogui
import time

import win32api
import win32con


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

    def eraseMainScript(self, mainScriptLocation):
        self.clickAtPosition(mainScriptLocation)
        pyautogui.keyDown('ctrl')
        pyautogui.hotkey('a')
        pyautogui.keyUp('ctrl')
        pyautogui.hotkey('backspace')



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

