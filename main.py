import os
import random
import matplotlib.pyplot as plt

# Create output directory for planet images
output_dir = os.path.join(os.path.dirname(__file__), '../../planets')
os.makedirs(output_dir, exist_ok=True)

def random_color():
    return (random.random(), random.random(), random.random())

def generate_planet_image(planet_num, size):
    fig, ax = plt.subplots(figsize=(2, 2), dpi=100)
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.axis('off')
    circle = plt.Circle((size/2, size/2), size/2 - 2, color=random_color())
    ax.add_patch(circle)
    plt.savefig(f"{output_dir}/planet_{planet_num}.png", bbox_inches='tight', pad_inches=0)
    plt.close(fig)

# Resource definitions with rarity, value, and use
RESOURCE_INFO = {
    "iron":         {"rarity": 0.8, "value": 10, "use": "build_primary"},
    "aluminum":     {"rarity": 0.7, "value": 12, "use": "build_primary"},
    "nickel":       {"rarity": 0.6, "value": 15, "use": "build_primary"},
    "copper":       {"rarity": 0.5, "value": 20, "use": "build_secondary"},
    "titanium":     {"rarity": 0.4, "value": 30, "use": "build_secondary"},
    "silver":       {"rarity": 0.3, "value": 50, "use": "merchant"},
    "gold":         {"rarity": 0.2, "value": 80, "use": "merchant"},
    "platinum":     {"rarity": 0.15, "value": 120, "use": "merchant"},
    "lithium":      {"rarity": 0.1, "value": 150, "use": "build_secondary"},
    "uranium":      {"rarity": 0.05, "value": 500, "use": "engine_weapon"},
}
RESOURCES = list(RESOURCE_INFO.keys())

SPACE_RESOURCE_INFO = {
    "water_ice":         {"rarity": 0.5, "value": 15, "use": "food"},
    "methane":           {"rarity": 0.4, "value": 20, "use": "merchant"},
    "ammonia":           {"rarity": 0.3, "value": 30, "use": "merchant"},
    "carbon_dust":       {"rarity": 0.2, "value": 40, "use": "spacesuit_upgrade"},
    "silicates":         {"rarity": 0.2, "value": 40, "use": "spacesuit_upgrade"},
    "organic_compounds": {"rarity": 0.1, "value": 60, "use": "food"},
}
SPACE_RESOURCES = list(SPACE_RESOURCE_INFO.keys())

# Building components: each needs one main resource and two secondary resources
BUILDING_COMPONENTS = {
    "outpost": {
        "main": "iron",
        "secondary": ["aluminum", "nickel"]
    },
    "ship_hull": {
        "main": "aluminum",
        "secondary": ["titanium", "nickel"]
    },
    "engine": {
        "main": "uranium",
        "secondary": ["copper", "lithium"]
    },
    "weapon": {
        "main": "uranium",
        "secondary": ["platinum", "titanium"]
    },
    "storage_unit": {
        "main": "nickel",
        "secondary": ["iron", "copper"]
    }
}

class Moon:
    def __init__(self, name, size, orbit_radius):
        self.name = name
        self.size = size
        self.orbit_radius = orbit_radius

class Nugget:
    def __init__(self, metal, total_weight, metal_ratio):
        self.metal = metal  # gold, silver, platinum
        self.total_weight = total_weight  # in grams
        self.metal_ratio = metal_ratio  # fraction of metal (0.1 to 1.0)
        self.stone_weight = total_weight * (1 - metal_ratio)
        self.metal_weight = total_weight * metal_ratio
        self.value = int(self.metal_weight * RESOURCE_INFO[metal]["value"])  # value based on pure metal weight

    def __str__(self):
        return f"{self.metal.title()} Nugget: {self.total_weight:.1f}g (Metal: {self.metal_weight:.1f}g, Stone: {self.stone_weight:.1f}g, Value: {self.value})"

class Mine:
    def __init__(self, resource, required_tool, amount):
        self.resource = resource
        self.required_tool = required_tool
        self.amount = amount

    def mine(self, tool, amount):
        if tool != self.required_tool:
            print(f"Tool '{tool}' is not suitable for mining {self.resource}.")
            return 0
        if self.amount <= 0:
            print(f"No {self.resource} left in this mine.")
            return 0
        mined = min(amount, self.amount)
        self.amount -= mined
        return mined

RESOURCE_TOOLS = {
    "iron": "pickaxe",
    "aluminum": "pickaxe",
    "nickel": "pickaxe",
    "copper": "pickaxe",
    "titanium": "drill",
    "silver": "drill",
    "gold": "drill",
    "platinum": "drill",
    "lithium": "laser",
    "uranium": "laser"
}

class Planet:
    def __init__(self, planet_id, name, size, orbit_radius, can_build_outpost, day_length, night_length, spin_speed, moon):
        self.planet_id = planet_id
        self.name = name
        self.size = size
        self.orbit_radius = orbit_radius
        self.can_build_outpost = can_build_outpost
        # Resource generation weighted by rarity (rarer = less)
        self.resources = {}
        self.nuggets = []
        self.mines = {}
        for res, info in RESOURCE_INFO.items():
            if res in ["gold", "silver", "platinum"]:
                # Generate nuggets for precious metals
                num_nuggets = random.randint(2, 6)
                total_metal = 0
                for _ in range(num_nuggets):
                    total_weight = random.uniform(10, 100)  # grams
                    metal_ratio = random.uniform(0.1, 1.0)  # at least 10% metal
                    nugget = Nugget(res, total_weight, metal_ratio)
                    self.nuggets.append(nugget)
                    total_metal += nugget.metal_weight
                self.resources[res] = int(total_metal)
                self.mines[res] = Mine(res, RESOURCE_TOOLS[res], int(total_metal))
            else:
                max_amt = int(5000 * info["rarity"])
                min_amt = max(1, int(1000 * info["rarity"]))
                # Uranium is always rare
                if res == "uranium":
                    max_amt = 100
                    min_amt = 5
                amt = random.randint(min_amt, max_amt)
                self.resources[res] = amt
                self.mines[res] = Mine(res, RESOURCE_TOOLS[res], amt)
        self.max_resources = self.resources.copy()
        self.day_length = day_length
        self.night_length = night_length
        self.spin_speed = spin_speed
        self.moon = moon

    def mine(self, resource, amount):
        if resource in self.resources and self.resources[resource] >= amount:
            self.resources[resource] -= amount
            return amount
        elif resource in self.resources:
            mined = self.resources[resource]
            self.resources[resource] = 0
            return mined
        return 0

    def regenerate(self, regen_rate=0.01):
        for res in RESOURCES:
            regen_amount = int(self.max_resources[res] * regen_rate)
            self.resources[res] = min(self.resources[res] + regen_amount, self.max_resources[res])

class CometResource:
    def __init__(self, resource, weight):
        self.resource = resource
        self.weight = weight  # in kg
        self.value = int(weight * SPACE_RESOURCE_INFO[resource]["value"])
        self.use = SPACE_RESOURCE_INFO[resource]["use"]

    def __str__(self):
        return f"{self.resource.replace('_', ' ').title()}: {self.weight:.1f}kg (Value: {self.value}, Use: {self.use})"

class Comet:
    def __init__(self, comet_id, name, orbit_radius, resources):
        self.comet_id = comet_id
        self.name = name
        self.orbit_radius = orbit_radius
        self.resources = resources  # dict of resource: CometResource

def create_solar_system():
    planets = []
    sun_position = (0, 0)
    min_orbit = 100
    orbit_gap = 80
    max_planet_size = 0
    planet_sizes = []
    # Determine all planet sizes to find the largest
    for i in range(1, 11):
        size = random.randint(50, 200)
        planet_sizes.append(size)
        if size > max_planet_size:
            max_planet_size = size
    for i in range(1, 11):
        size = planet_sizes[i-1]
        orbit_radius = min_orbit + (i - 1) * orbit_gap
        name = f"Planet_{i}"
        can_build_outpost = 4 <= i <= 7
        # Moon size is up to 20% of planet size
        moon_size = random.randint(int(size * 0.1), max(1, int(size * 0.2)))
        moon_orbit = random.randint(int(size * 1.5), int(size * 2.5))
        moon = Moon(f"{name}_Moon", moon_size, moon_orbit)
        # Day/night length based on distance and size (longest for largest planet)
        base_day = 10
        base_night = 10
        day_length = base_day + int((orbit_radius / (min_orbit + 9 * orbit_gap)) * 20) + int((size / max_planet_size) * 10)
        night_length = base_night + int((orbit_radius / (min_orbit + 9 * orbit_gap)) * 20) + int((size / max_planet_size) * 10)
        spin_speed = round(360 / (day_length + night_length), 2)  # degrees per time unit
        planet = Planet(i, name, size, orbit_radius, can_build_outpost, day_length, night_length, spin_speed, moon)
        planets.append(planet)
        generate_planet_image(i, size)
    print("Generated 10 planet images in the 'planets' folder.")
    return planets, sun_position

def create_comets(num_comets=3):
    comets = []
    for i in range(1, num_comets + 1):
        orbit_radius = random.randint(900, 2000)
        name = f"Comet_{i}"
        num_resources = random.randint(2, len(SPACE_RESOURCES))
        chosen_resources = random.sample(SPACE_RESOURCES, num_resources)
        resources = {}
        for res in chosen_resources:
            weight = random.uniform(100, 1000)  # kg
            resources[res] = CometResource(res, weight)
        comets.append(Comet(i, name, orbit_radius, resources))
    return comets

# Tool crafting/trading info
TOOL_INFO = {
    "pickaxe": {
        "buildable": False,  # All users start with this
        "tradeable": False,
        "cost": 0,
        "requirements": {}
    },
    "drill": {
        "buildable": True,
        "tradeable": True,
        "cost": 500,  # Merchant price
        "requirements": {
            "iron": 50,
            "nickel": 30,
            "copper": 20
        }
    },
    "laser": {
        "buildable": True,
        "tradeable": True,
        "cost": 2000,  # Most expensive
        "requirements": {
            "titanium": 40,
            "lithium": 25,
            "uranium": 10,
            "gold": 5
        }
    }
}

def print_tool_info():
    print("Mining Tools:")
    for tool, info in TOOL_INFO.items():
        if info["buildable"]:
            reqs = ", ".join(f"{k}: {v}" for k, v in info["requirements"].items())
            print(f"  {tool.title()}: Buildable (requires {reqs}), Merchant price: {info['cost']}")
        else:
            print(f"  {tool.title()}: All users start with this tool.")

class Tool:
    def __init__(self, name):
        self.name = name
        self.durability = 0  # 0% = new, 100% = broken
        self.broken = False
        self.repair_resource = self.get_repair_resource()

    def use(self):
        if self.broken:
            print(f"{self.name.title()} is broken and cannot be used.")
            return False
        self.durability += 5  # Each use increases damage by 5%
        if self.durability >= 100:
            self.durability = 100
            self.broken = True
            print(f"{self.name.title()} is now broken!")
        return not self.broken

    def get_repair_resource(self):
        # More valuable resource for more advanced tools
        if self.name == "pickaxe":
            return "iron"
        elif self.name == "drill":
            return "titanium"
        elif self.name == "laser":
            return "uranium"
        return "iron"

    def repair(self, player_inventory):
        if self.broken or self.durability > 0:
            needed = 1  # 1 unit of resource to repair
            res = self.repair_resource
            if player_inventory.get(res, 0) >= needed:
                player_inventory[res] -= needed
                self.durability = 0
                self.broken = False
                print(f"{self.name.title()} repaired using {needed} {res}.")
                return True
            else:
                print(f"Not enough {res} to repair {self.name.title()}.")
                return False
        print(f"{self.name.title()} does not need repair.")
        return False

# Example player inventory for demonstration
player_inventory = {"iron": 10, "titanium": 5, "uranium": 2}

# Example usage in main()
def main():
    print("Welcome to the Galaxy project!")
    print_tool_info()
    # Player starts with a pickaxe
    player_tools = {"pickaxe": Tool("pickaxe")}
    print("\nPlayer starts with a pickaxe.")
    # Simulate tool usage and repair
    print("\nSimulating tool usage:")
    for i in range(22):  # Use more than 20 times to break
        print(f"Use {i+1}: ", end="")
        player_tools["pickaxe"].use()
        if player_tools["pickaxe"].broken:
            print("Attempting repair...")
            player_tools["pickaxe"].repair(player_inventory)
    planets, sun_position = create_solar_system()
    comets = create_comets()
    print("Solar System Layout:")
    print(f"Sun at {sun_position}")
    for planet in planets:
        outpost_status = "Can build outpost" if planet.can_build_outpost else "No outpost"
        print(f"{planet.name}: Orbit radius {planet.orbit_radius}, {outpost_status}")
        print(f"  Size: {planet.size}, Moon: {planet.moon.name} (size {planet.moon.size})")
        print(f"  Day: {planet.day_length} units, Night: {planet.night_length} units, Spin: {planet.spin_speed} deg/unit")
        for resource, mine in planet.mines.items():
            info = RESOURCE_INFO[resource]
            if resource in ["gold", "silver", "platinum"]:
                print(f"    {resource} mine: {mine.amount}g (nuggets, tool: {mine.required_tool})")
                for nugget in planet.nuggets:
                    if nugget.metal == resource:
                        print(f"      {nugget}")
            else:
                print(f"    {resource} mine: {mine.amount} (tool: {mine.required_tool}, value: {info['value']}, use: {info['use']})")
        print()
    print("Comets in the system:")
    for comet in comets:
        print(f"{comet.name}: Orbit radius {comet.orbit_radius}")
        for cres in comet.resources.values():
            print(f"    {cres}")
        print()
    print("Building Components (requirements):")
    for comp, req in BUILDING_COMPONENTS.items():
        print(f"  {comp.title()}: Main - {req['main']}, Secondary - {', '.join(req['secondary'])}")

if __name__ == "__main__":
    main()