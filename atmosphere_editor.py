class AtmosphereEditor:
    def __init__(self):
        self.atmosphere_composition = {}
        self.pressure = 1.0  # Default pressure in atm
        self.color = (135, 206, 235)  # Default color (sky blue)

    def set_composition(self, composition):
        self.atmosphere_composition = composition

    def set_pressure(self, pressure):
        if pressure > 0:
            self.pressure = pressure
        else:
            raise ValueError("Pressure must be a positive value.")

    def set_color(self, color):
        if isinstance(color, tuple) and len(color) == 3:
            self.color = color
        else:
            raise ValueError("Color must be a tuple of three values (R, G, B).")

    def set_oxygen_level(self, percent):
        if 0 <= percent <= 100:
            self.atmosphere_composition["O2"] = percent
        else:
            raise ValueError("Oxygen level must be between 0 and 100 percent.")

    def get_atmosphere_info(self):
        return {
            "composition": self.atmosphere_composition,
            "pressure": self.pressure,
            "color": self.color
        }