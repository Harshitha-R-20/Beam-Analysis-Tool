from beam import Beam

print('--- Beam Analysis Tool Interactive Mode ---')

# Material selection
def get_material():
    materials = {
        'concrete': {'E': 25e9, 'desc': 'Concrete (E = 25 GPa typical)'},
        'steel': {'E': 200e9, 'desc': 'Steel (E = 200 GPa typical)'}
    }
    print('Select material:')
    for i, k in enumerate(materials):
        print(f"  {i+1}. {materials[k]['desc']}")
    while True:
        sel = input('Material [1=Concrete, 2=Steel]: ').strip()
        if sel == '1':
            return materials['concrete']['E']
        elif sel == '2':
            return materials['steel']['E']
        else:
            print('Invalid selection!')

# Get beam parameters
length = float(input('Enter beam length [m]: '))
E = get_material()
I = float(input('Enter moment of inertia I [in m^4]: '))

beam = Beam(length=length, E=E, I=I)

# Add point loads
def add_point_loads():
    print('Add point loads (enter nothing to stop):')
    while True:
        loc = input('  Load location [m, leave empty to stop]: ')
        if loc.strip() == '':
            break
        mag = float(input('  Magnitude [N]: '))
        beam.add_point_load(location=float(loc), magnitude=mag)
add_point_loads()

# Add UDLs
def add_udls():
    print('Add UDLs (enter nothing to stop):')
    while True:
        start = input('  UDL start position [m, leave empty to stop]: ')
        if start.strip() == '':
            break
        end = float(input('  UDL end position [m]: '))
        mag = float(input('  Magnitude [N/m]: '))
        beam.add_udl(start=float(start), end=end, magnitude=mag)
add_udls()

beam.plot_diagrams(export=True)
print('\n[INFO] Diagrams plotted and saved.')
