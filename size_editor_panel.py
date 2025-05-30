import wx
from editor.size_editor import SizeEditor

class SizeEditorPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.size_editor = SizeEditor()
        self.size_editor.set_diameter(100)  # Initial diameter

        self.dragging = False
        self.last_mouse_pos = None
        self.zoom = 1.0
        self.zoom_min = 0.2
        self.zoom_max = 5.0
        self.surface_view_button = None
        self.surface_view_threshold = 2.5  # Zoom level to show surface view button

        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)
        self.Bind(wx.EVT_MOUSEWHEEL, self.on_mouse_wheel)

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        w, h = self.GetSize()
        diameter = int(self.size_editor.get_diameter() * self.zoom)
        x = w // 2
        y = h // 2
        dc.SetBrush(wx.Brush(wx.Colour(135, 206, 235)))
        dc.DrawCircle(x, y, diameter // 2)
        # Draw ring if present
        if hasattr(self, 'features_editor') and self.features_editor.get_ring():
            ring = self.features_editor.get_ring()
            ring_thickness = int(ring.get('thickness', 1.0) * self.zoom)
            ring_color = ring.get('color', (200, 200, 200))
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            dc.SetPen(wx.Pen(wx.Colour(*ring_color), ring_thickness))
            ring_radius = diameter // 2 + int(ring_thickness * 2)
            dc.DrawEllipse(x - ring_radius, y - ring_radius, ring_radius * 2, ring_radius * 2)
        # Show surface view button if zoomed in enough
        if self.zoom >= self.surface_view_threshold:
            if not self.surface_view_button:
                self.surface_view_button = wx.Button(self, label="Surface View", pos=(w-130, h-50), size=(120, 30))
                self.surface_view_button.Bind(wx.EVT_BUTTON, self.on_surface_view)
            self.surface_view_button.Show()
        else:
            if self.surface_view_button:
                self.surface_view_button.Hide()

    def on_left_down(self, event):
        self.dragging = True
        self.last_mouse_pos = event.GetPosition()

    def on_left_up(self, event):
        self.dragging = False
        self.last_mouse_pos = None

    def set_features_editor(self, features_editor):
        self.features_editor = features_editor

    def on_mouse_move(self, event):
        if self.dragging and event.Dragging() and event.LeftIsDown():
            pos = event.GetPosition()
            w, h = self.GetSize()
            center = wx.Point(w // 2, h // 2)
            radius = ((pos.x - center.x) ** 2 + (pos.y - center.y) ** 2) ** 0.5 / self.zoom
            new_diameter = max(10, int(radius * 2))
            self.size_editor.set_diameter(new_diameter)
            self.Refresh()  # Redraw the panel

    def on_mouse_wheel(self, event):
        rotation = event.GetWheelRotation()
        delta = 0.1 if rotation > 0 else -0.1
        new_zoom = min(max(self.zoom + delta, self.zoom_min), self.zoom_max)
        if new_zoom != self.zoom:
            self.zoom = new_zoom
            self.Refresh()

    def on_surface_view(self, event):
        wx.MessageBox("Switching to surface view at this location!", "Surface View")
