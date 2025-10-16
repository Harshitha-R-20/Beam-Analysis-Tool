# Beam Analysis Tool

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17372120.svg)](https://doi.org/10.5281/zenodo.17372120)

This interactive Python package provides tools for analyzing simply supported beams. Users select material, beam dimensions, and loads with a guided command-line interface. The tool generates shear force, bending moment, and deflection diagrams with export options.

## Features
- Interactive user input for material, beam length, and load specifications
- Support for multiple point loads and uniformly distributed loads
- Computation and visualization of shear force, bending moment, and deflection
- Export diagrams as PNG and PDF for reports and publications

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/Harshitha-R-20/Beam-Analysis-Tool.git
   cd Beam-Analysis-Tool
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the interactive tool:
   ```
   python main.py
   ```

## Usage Example
- When prompted, input realistic beam parameters and loads. For example:
  - Beam length: 8
  - Material (1=Concrete, 2=Steel)
  - Moment of inertia: 8.33e-6
  - Point load: location 3, magnitude 5000 N
  - UDL: start 0, end 8, magnitude 2000 N/m

## License
MIT

## Author
Harshitha R.

## Citation
Harshitha, R. (2025). Beam Analysis Tool (Version 1.0.0) [Software]. Zenodo. https://doi.org/10.5281/zenodo.17372120

## Acknowledgements
Thank you to open-source contributors and the JOSS editorial team.
