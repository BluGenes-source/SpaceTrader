class TerrainEditor:
    def __init__(self):
        self.terrain_type = None
        self.texture = None

    def set_terrain_type(self, terrain_type):
        self.terrain_type = terrain_type

    def set_texture(self, texture):
        self.texture = texture

    def get_terrain_info(self):
        return {
            "terrain_type": self.terrain_type,
            "texture": self.texture
        }