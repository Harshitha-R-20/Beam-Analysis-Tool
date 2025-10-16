---
title: 'Beam Analysis Tool: Open Source Python Package for Civil and Structural Engineering'
authors:
  - name: Harshitha R.
    affiliation: Department of Civil Engineering, [Your University], India
    github: Harshitha-R-20
repository: https://github.com/Harshitha-R-20/Beam-Analysis-Tool
archive: https://doi.org/10.5281/zenodo.17372120
license: MIT
---

# Summary
The Beam Analysis Tool is a user-friendly Python package designed to help civil and structural engineers, educators, and students analyze simply supported beams subjected to point and uniformly distributed loads. The software calculates shear force, bending moment, and deflection diagrams, and produces publication-quality plots. By simplifying common tasks in beam analysis, this tool makes structural calculations more accessible and reproducible for academic, research, and engineering applications.

# Statement of Need
Structural analysis is a foundational aspect of civil engineering, and practicing engineers as well as students require reliable tools to study beam behavior. Many commercially available solutions are expensive or too complex for classroom use, and few are open source. The Beam Analysis Tool provides an affordable, extensible, and transparent platform while promoting reproducibility—addressing a clear gap in educational and research communities.

# Functionality
- Analyze simply supported beams with any combination of point load and uniformly distributed load
- Calculates shear force, bending moment, and deflection at all points across beam length
- Visualizes diagrams with professional-quality plots (Matplotlib)
- Example scripts and built-in documentation
- Ready for integration into research workflows or teaching labs

# Installation
Clone this repository, install dependencies, and run the example:
```
git clone https://github.com/Harshitha-R-20/Beam-Analysis-Tool.git
cd Beam-Analysis-Tool
pip install -r requirements.txt
python main.py
```

# Example
```
from beam import Beam
E = 200e9  # Young's modulus (Pa)
I = 8.333e-6  # Moment of inertia (m^4)
beam = Beam(length=10, E=E, I=I)
beam.add_point_load(location=5, magnitude=10000)  # 10kN at 5m
beam.add_udl(start=0, end=10, magnitude=2000)  # 2kN/m full length
beam.plot_diagrams()
```

# References
- Gere, J.M. & Timoshenko, S.P., Mechanics of Materials, PWS Publishing, 1997.
- Beer, F.P. et al., Mechanics of Materials, McGraw-Hill, 6th Edition, 2012.
- https://github.com/Harshitha-R-20/Beam-Analysis-Tool

# Acknowledgements
Thanks to open source software contributors and the JOSS editorial team. This work was completed independently as a student initiative.

# Funding
No external funding was received for this work.

# Statement of Reproducibility
The software is open source, versioned, and archived at Zenodo (DOI: https://doi.org/10.5281/zenodo.17372120). All code and example data needed to reproduce the results are included in the repository.
