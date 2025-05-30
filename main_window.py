import wx
from src.editor.terrain_editor import TerrainEditor
from src.editor.size_editor import SizeEditor
from src.editor.atmosphere_editor import AtmosphereEditor
from src.ui.editor_panels import SurfaceEditorPanel

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title, size=(800, 600))
        
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.terrain_editor = TerrainEditor(self.panel)
        self.size_editor = SizeEditor(self.panel)
        self.atmosphere_editor = AtmosphereEditor(self.panel)
        self.surface_editor = SurfaceEditorPanel(self.panel)

        self.sizer.Add(self.terrain_editor, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.size_editor, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.atmosphere_editor, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.surface_editor, 1, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizer(self.sizer)
        self.Centre()
        self.Show()