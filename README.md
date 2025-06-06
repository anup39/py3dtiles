# py3dtiles

A Python library for converting 3D models (OBJ, etc.) into 3D Tiles format, compatible with Cesium viewers.

## Overview

py3dtiles is an open-source tool that helps you convert 3D models into [3D Tiles](https://github.com/CesiumGS/3d-tiles) format, making them ready for visualization in CesiumJS-based applications. The library handles model optimization, tiling, and generates the required tileset.json for proper rendering.

## Features

- Convert OBJ models to 3D Tiles format
- Automatic LOD (Level of Detail) generation
- Spatial subdivision of large models
- Configurable tiling parameters
- Georeferencing support
- Tileset.json generation
- Memory-efficient processing

## Installation

```bash
pip install py3dtiles
```

## Usage

Basic usage with command line interface:

```bash
python main.py input.obj output_folder --divisions 2 --lods 3
```

### Arguments

- `input`: Path to input 3D model file (required)
- `output`: Output directory for generated tiles (required)
- `--divisions`: Number of spatial divisions for splitting (default: 2)
- `--lods`: Number of Level of Details to generate (default: 3)
- `--latitude`: Latitude for georeferencing (optional)
- `--longitude`: Longitude for georeferencing (optional)
- `--altitude`: Altitude in meters (default: 0)
- `--scale`: Scale factor for the model (default: 1.0)

### Example

```bash
python main.py models/city.obj output/city_tiles --divisions 4 --lods 5 --latitude 37.7749 --longitude -122.4194
```

## Pipeline Steps

1. **Reduction**: Generates multiple LODs through mesh decimation
2. **Splitting**: Subdivides the model into spatial tiles
3. **Tiling**: Converts the tiles into 3D Tiles format

## Requirements

- Python 3.7+
- Required packages listed in requirements.txt

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [CesiumJS](https://cesium.com/platform/cesiumjs/) for the 3D Tiles specification
- The open-source community for various tools and libraries used in this project

## Contact

Project Link: [https://github.com/yourusername/py3dtiles](https://github.com/yourusername/py3dtiles)