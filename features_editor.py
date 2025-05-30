class SurfaceEditor:
    def __init__(self):
        self.terrain_height_map = {}  # {(x, y): height}
        self.features = []  # List of placed features (e.g., trees, boulders)
        self.waterscapes = []  # List of waterscapes (e.g., lakes, rivers, oceans)
        self.ring = None  # Ring data: dict with position and properties

    def set_terrain_height(self, x, y, height):
        """Set the height at a specific (x, y) coordinate."""
        self.terrain_height_map[(x, y)] = height

    def get_terrain_height(self, x, y):
        """Get the height at a specific (x, y) coordinate."""
        return self.terrain_height_map.get((x, y), 0)

    def add_feature(self, feature_type, position):
        """Place a feature (e.g., tree, boulder) at a position."""
        self.features.append({"type": feature_type, "position": position})

    def remove_feature(self, feature_type, position):
        """Remove a feature from a position."""
        self.features = [
            f for f in self.features if not (f["type"] == feature_type and f["position"] == position)
        ]

    def add_waterscape(self, waterscape_type, area):
        """
        Add a waterscape (lake, river, ocean).
        area: could be a list of coordinates or a bounding box.
        """
        self.waterscapes.append({"type": waterscape_type, "area": area})

    def remove_waterscape(self, waterscape_type, area):
        self.waterscapes = [
            w for w in self.waterscapes if not (w["type"] == waterscape_type and w["area"] == area)
        ]

    def set_ring(self, position, tilt=0, thickness=1.0, color=(200, 200, 200)):
        """
        Add or update a ring around the planet.
        position: (x, y, z) tuple for ring orientation.
        tilt: angle in degrees.
        thickness: width of the ring.
        color: RGB tuple.
        """
        self.ring = {
            "position": position,
            "tilt": tilt,
            "thickness": thickness,
            "color": color
        }

    def remove_ring(self):
        self.ring = None

    def get_ring(self):
        return self.ring

    def get_features(self):
        return self.features

    def get_waterscapes(self):
        return self.waterscapes

    def get_terrain_map(self):
        return self.terrain_height_map