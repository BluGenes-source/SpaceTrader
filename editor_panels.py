import wx
from src.editor.terrain_editor import TerrainEditor
from src.editor.size_editor import SizeEditor
from src.editor.atmosphere_editor import AtmosphereEditor
from src.editor.features_editor import SurfaceEditor
from src.ui.size_editor_panel import SizeEditorPanel

class SurfaceEditorPanel(wx.Panel):
    def __init__(self, parent):
        super(SurfaceEditorPanel, self).__init__(parent)
        self.editor = SurfaceEditor()
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Terrain Height Controls
        terrain_box = wx.StaticBoxSizer(wx.StaticBox(self, label="Terrain Height"), wx.VERTICAL)
        self.x_input = wx.TextCtrl(self, value="0")
        self.y_input = wx.TextCtrl(self, value="0")
        self.height_input = wx.TextCtrl(self, value="0")
        set_height_btn = wx.Button(self, label="Set Height")
        set_height_btn.Bind(wx.EVT_BUTTON, self.on_set_height)
        terrain_box.Add(wx.StaticText(self, label="X:"))
        terrain_box.Add(self.x_input)
        terrain_box.Add(wx.StaticText(self, label="Y:"))
        terrain_box.Add(self.y_input)
        terrain_box.Add(wx.StaticText(self, label="Height:"))
        terrain_box.Add(self.height_input)
        terrain_box.Add(set_height_btn)
        sizer.Add(terrain_box, 0, wx.EXPAND|wx.ALL, 5)

        # Feature Controls
        feature_box = wx.StaticBoxSizer(wx.StaticBox(self, label="Add Feature"), wx.VERTICAL)
        self.feature_type_input = wx.TextCtrl(self, value="tree")
        self.feature_pos_input = wx.TextCtrl(self, value="(0,0)")
        add_feature_btn = wx.Button(self, label="Add Feature")
        add_feature_btn.Bind(wx.EVT_BUTTON, self.on_add_feature)
        feature_box.Add(wx.StaticText(self, label="Type:"))
        feature_box.Add(self.feature_type_input)
        feature_box.Add(wx.StaticText(self, label="Position (x,y):"))
        feature_box.Add(self.feature_pos_input)
        feature_box.Add(add_feature_btn)
        sizer.Add(feature_box, 0, wx.EXPAND|wx.ALL, 5)

        # Waterscape Controls
        water_box = wx.StaticBoxSizer(wx.StaticBox(self, label="Add Waterscape"), wx.VERTICAL)
        self.water_type_input = wx.TextCtrl(self, value="lake")
        self.water_area_input = wx.TextCtrl(self, value="[(0,0),(1,1)]")
        add_water_btn = wx.Button(self, label="Add Waterscape")
        add_water_btn.Bind(wx.EVT_BUTTON, self.on_add_waterscape)
        water_box.Add(wx.StaticText(self, label="Type:"))
        water_box.Add(self.water_type_input)
        water_box.Add(wx.StaticText(self, label="Area (list of tuples):"))
        water_box.Add(self.water_area_input)
        water_box.Add(add_water_btn)
        sizer.Add(water_box, 0, wx.EXPAND|wx.ALL, 5)

        self.SetSizer(sizer)

    def on_set_height(self, event):
        try:
            x = int(self.x_input.GetValue())
            y = int(self.y_input.GetValue())
            height = float(self.height_input.GetValue())
            self.editor.set_terrain_height(x, y, height)
            wx.MessageBox(f"Set height at ({x},{y}) to {height}")
        except Exception as e:
            wx.MessageBox(str(e), style=wx.ICON_ERROR)

    def on_add_feature(self, event):
        try:
            feature_type = self.feature_type_input.GetValue()
            pos = eval(self.feature_pos_input.GetValue())
            self.editor.add_feature(feature_type, pos)
            wx.MessageBox(f"Added {feature_type} at {pos}")
        except Exception as e:
            wx.MessageBox(str(e), style=wx.ICON_ERROR)

    def on_add_waterscape(self, event):
        try:
            water_type = self.water_type_input.GetValue()
            area = eval(self.water_area_input.GetValue())
            self.editor.add_waterscape(water_type, area)
            wx.MessageBox(f"Added {water_type} at {area}")
        except Exception as e:
            wx.MessageBox(str(e), style=wx.ICON_ERROR)

    def get_features_data(self):
        return {
            "terrain_map": self.editor.get_terrain_map(),
            "features": self.editor.get_features(),
            "waterscapes": self.editor.get_waterscapes()
        }

class EditorPanels(wx.Panel):
    def __init__(self, parent):
        super(EditorPanels, self).__init__(parent)
        self.terrain_editor = TerrainEditor(self)
        self.size_editor = SizeEditorPanel(self)
        self.atmosphere_editor = AtmosphereEditor(self)
        self.surface_editor = SurfaceEditor(self)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.terrain_editor, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.size_editor, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.atmosphere_editor, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.surface_editor, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(self.sizer)

    def get_planet_data(self):
        return {
            "terrain": self.terrain_editor.get_terrain_map(),
            "size": self.size_editor.size_editor.get_diameter(),
            "atmosphere": self.atmosphere_editor.get_atmosphere_info(),
            "surface": {
                "features": self.surface_editor.get_features(),
                "waterscapes": self.surface_editor.get_waterscapes(),
                "terrain_map": self.surface_editor.get_terrain_map(),
                "ring": self.surface_editor.get_ring()
            }
        }