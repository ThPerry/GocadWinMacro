import win32gui
import win32ui

class Handler():
    def __init__(self, applicationName):
        # Initialize attributes
        self._aplicationName = applicationName
        
        # Initialize window handlers
        self.win                = None
        self._mainWndHandl      = None
        self._childWndHandlDict = None
        self._childWndName      = ''
        self._childWndHandl     = None

        # Initialize window and respective childWindows handlers
        self._setMainWindow()
        self._childWndHandlDict = self._list_inner_windows()
        
        # Select child window
        self._childWndName  = list(self._childWndHandlDict.keys())[0]
        self._setChildWindow()


    # List all windows names and respective hex ids
    def _list_window_names(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
        win32gui.EnumWindows(winEnumHandler, None)

    # Lists all inner windows inside one specific window. Returns a dictionary for all child windows.
    def _list_inner_windows(self):
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                hwnds[win32gui.GetClassName(hwnd)] = hwnd
            return True

        hwnds = {}
        win32gui.EnumChildWindows(self._mainWndHandl, callback, hwnds)
        return hwnds  

    # Set main window based on its name
    def _setMainWindow(self):
        self._mainWndHandl = win32gui.FindWindow(None, self._aplicationName)

    # set childWindow based on its name
    def _setChildWindow(self):
        self._childWndHandl = self._childWndHandlDict[self._childWndName]
        self.win = win32ui.CreateWindowFromHandle(self._childWndHandl)

    
