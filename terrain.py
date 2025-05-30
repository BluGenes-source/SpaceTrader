class Terrain:
    def __init__(self, terrain_type="plain", texture="default"):
        self.terrain_type = terrain_type
        self.texture = texture

    def set_terrain_type(self, terrain_type):
        self.terrain_type = terrain_type

    def set_texture(self, texture):
        self.texture = texture

    def get_terrain_info(self):
        return {
            "terrain_type": self.terrain_type,
            "texture": self.texture
        }