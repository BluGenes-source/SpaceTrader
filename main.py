import wx
from ui.main_window import MainWindow

def main():
    app = wx.App(False)
    main_window = MainWindow(None, "Planet Map Editor")
    app.MainLoop()

if __name__ == "__main__":
    main()