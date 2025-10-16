import numpy as np
import matplotlib.pyplot as plt

class Beam:
    def __init__(self, length, E, I):
        self.length = length
        self.E = E  # Young's modulus
        self.I = I  # Moment of inertia
        self.point_loads = []
        self.udls = []

    def add_point_load(self, location, magnitude):
        self.point_loads.append({'location': location, 'magnitude': magnitude})

    def add_udl(self, start, end, magnitude):
        self.udls.append({'start': start, 'end': end, 'magnitude': magnitude})

    def shear_force(self, x):
        V = 0
        for load in self.point_loads:
            if x >= load['location']:
                V -= load['magnitude']
        for udl in self.udls:
            if x >= udl['start']:
                length_active = min(x, udl['end']) - udl['start']
                if length_active > 0:
                    V -= udl['magnitude'] * length_active
        return V

    def bending_moment(self, x):
        M = 0
        for load in self.point_loads:
            if x >= load['location']:
                M -= load['magnitude'] * (x - load['location'])
        for udl in self.udls:
            if x >= udl['start']:
                length_active = min(x, udl['end']) - udl['start']
                if length_active > 0:
                    M -= udl['magnitude'] * length_active * (x - udl['start'] - length_active / 2)
        return M

    def deflection(self, x, n=1000):
        xs = np.linspace(0, self.length, n)
        M_vals = np.array([self.bending_moment(xi) for xi in xs])
        curvature = M_vals / (self.E * self.I)
        dx = xs[1] - xs[0]
        slope = np.cumsum(curvature) * dx
        defl = np.cumsum(slope) * dx
        return np.interp(x, xs, defl)

    def plot_diagrams(self, export=False):
        xs = np.linspace(0, self.length, 1000)
        V = np.array([self.shear_force(x) for x in xs])
        M = np.array([self.bending_moment(x) for x in xs])
        D = np.array([self.deflection(x) for x in xs])

        fig, axs = plt.subplots(3, 1, figsize=(12, 14))

        font_title = {'fontsize': 16, 'fontweight': 'bold'}
        font_axis = {'fontsize': 13}
        font_label = {'fontsize': 12}

        axs[0].plot(xs, V, label='Shear Force', color='navy')
        axs[0].set_title('Shear Force Diagram', **font_title)
        axs[0].set_xlabel('Beam Length (m)', **font_axis)
        axs[0].set_ylabel('Shear Force (kN)', **font_label)
        axs[0].legend(loc='best')
        axs[0].grid(True)

        axs[1].plot(xs, M, label='Bending Moment', color='orange')
        axs[1].set_title('Bending Moment Diagram', **font_title)
        axs[1].set_xlabel('Beam Length (m)', **font_axis)
        axs[1].set_ylabel('Bending Moment (kNm)', **font_label)
        axs[1].legend(loc='best')
        axs[1].grid(True)

        axs[2].plot(xs, D, label='Deflection', color='green')
        axs[2].set_title('Deflection Diagram', **font_title)
        axs[2].set_xlabel('Beam Length (m)', **font_axis)
        axs[2].set_ylabel('Deflection (m)', **font_label)
        axs[2].legend(loc='best')
        axs[2].grid(True)

        plt.tight_layout()
        if export:
            fig.savefig('beam_diagrams.png')
            fig.savefig('beam_diagrams.pdf')
        plt.show()
