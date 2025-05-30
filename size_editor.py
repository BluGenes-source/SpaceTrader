class SizeEditor:
    def __init__(self):
        self.diameter = 0
        self.scale = 1.0

    def set_diameter(self, diameter):
        if diameter > 0:
            self.diameter = diameter
        else:
            raise ValueError("Diameter must be a positive value.")

    def get_diameter(self):
        return self.diameter

    def set_scale(self, scale):
        if scale > 0:
            self.scale = scale
        else:
            raise ValueError("Scale must be a positive value.")

    def get_scale(self):
        return self.scale

    def apply_size_changes(self):
        # Logic to apply size changes to the planet
        pass