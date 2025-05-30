class Planet:
    def __init__(self, name, size, atmosphere, terrain):
        self.name = name
        self.size = size  # Size in kilometers
        self.atmosphere = atmosphere  # Dictionary containing atmosphere properties
        self.terrain = terrain  # Terrain object

    def update_size(self, new_size):
        self.size = new_size

    def update_atmosphere(self, new_atmosphere):
        self.atmosphere = new_atmosphere

    def update_terrain(self, new_terrain):
        self.terrain = new_terrain

    def __str__(self):
        return f"Planet: {self.name}, Size: {self.size} km, Atmosphere: {self.atmosphere}, Terrain: {self.terrain}"