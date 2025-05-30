# Planet Map Editor

## Overview
The Planet Map Editor is a customizable tool that allows users to create and modify planets by adjusting various parameters such as terrain, size, atmosphere, and additional features. This project is designed to provide an intuitive interface for users to fully customize their planetary creations.

## Features
- **Terrain Editor**: Customize the terrain type and texture of the planet.
- **Size Editor**: Adjust the size of the planet, including diameter and scale.
- **Atmosphere Editor**: Modify the atmosphere's composition, pressure, and color.
- **Features Editor**: Add or remove features such as mountains, rivers, and vegetation.

## Project Structure
```
planet-map-editor
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── editor
│   │   ├── __init__.py
│   │   ├── terrain_editor.py
│   │   ├── size_editor.py
│   │   ├── atmosphere_editor.py
│   │   └── features_editor.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── planet.py
│   │   └── terrain.py
│   └── ui
│       ├── __init__.py
│       ├── main_window.py
│       └── editor_panels.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd planet-map-editor
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To start the application, run the following command:
```
python src/main.py
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.