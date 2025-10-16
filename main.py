from beam import Beam

# Example usage

# Constants for steel (in SI units)
E = 200e9  # Young's modulus in Pascals
I = 8.333e-6  # Moment of inertia in m^4

# Create beam
beam = Beam(length=10, E=E, I=I)

# Add loads
beam.add_point_load(location=5, magnitude=10000)  # 10 kN at 5 m
beam.add_udl(start=0, end=10, magnitude=2000)  # 2 kN/m over entire length

# Plot diagrams
beam.plot_diagrams()
