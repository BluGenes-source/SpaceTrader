# Space Trader Game

A game where the player travels a map trading at ports, populating planets, and developing resources.

## The Center of the Universe

At the center of the universe is one map sector that all players start from. This sector has services from the federation such as:
- Making colonists available
- Purchasing ships
- Purchasing resources
- Some limited social services
- Maintaining a wanted list and bounty system
- A banking system
- Maybe news too...

### Map System

The map of space is just a 2D grid of 1000 x 1000 locations, but traverse using a six-sided hex grid.

From sector one, generate paths that connect:
- Some that dead end
- Some one way in
- Sectors can connect via sectors that allow direction: either in, out, in and out
- A sector can be a dead end

Fill the map to a percentage of paths that connect.

## Game Interface

### Federation View
The player sees a screen for the main sector, or federation view with options for this sector. Maybe a picture of the star base.

### Ship Controls
Once a player boards his ship, his controls are what the ship can do while either moving, or docked:

**If moving:**
- Direction, speed, etc.

**Combat:**
- Weapons Control: special weapons, fighters, defense, attack, survey

**Trading:**
- Buy or sell
- If negative, steal, etc.

### Planet Controls
When a player is on a planet, controls:
- Population
- Production
- Warehousing
- Defense
- Assets
- Banking

## The Planets

The planets include:
- An Earth-like planet
- A desert-like planet
- An ocean-like planet
- A mountainous planet
- A volcanic planet

Each with more or less quantities of resources.

### Planet Resources

Each planet will have as resources in percentage:
- Petroleum
- Livestock for food
- Organics
- Equipment
- Housing
- Precious metals
- Water
- Air
- Population size
- Population max size
- Population happiness
- Population health

Each planet will have factories for production of the elements of the game.

## Technical Implementation

I am thinking the game to be a combination of:
- **wxWidgets** for the UI
- **Python server** for the game mechanics

Ultimately being played as a localhost game using a web browser.