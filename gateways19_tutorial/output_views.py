import io
import os

import numpy as np
from matplotlib.figure import Figure

from cclib.parser import ccopen

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class GaussianEigenvaluesViewProvider:
    display_type = 'image'
    name = "Gaussian Eigenvalues"
    test_output_file = os.path.join(BASE_DIR, "data", "gaussian.log")

    def generate_data(self, request, experiment_output, experiment, output_file=None):

        # Parse output_file
        gaussian = ccopen(output_file)
        data = gaussian.parse()
        data.listify()
        homo_eigenvalues = None
        lumo_eigenvalues = None
        if hasattr(data, 'homos') and hasattr(data, 'moenergies'):
            homos = data.homos[0] + 1
            moenergies = data.moenergies[0]
            if homos > 9 and len(moenergies) >= homos:
                homo_eigenvalues = [data.moenergies[0][homos - 1 - i] for i in range(1, 10)]
            if homos + 9 <= len(moenergies):
                lumo_eigenvalues = [data.moenergies[0][homos + i] for i in range(1, 10)]

        # Create plot
        fig = Figure()
        if homo_eigenvalues and lumo_eigenvalues:
            fig.suptitle("Eigenvalues")
            ax = fig.subplots(2, 1)
            ax[0].plot(range(1, 10), homo_eigenvalues, label='Homo')
            ax[0].set_ylabel('eV')
            ax[0].legend()
            ax[1].plot(range(1, 10), lumo_eigenvalues, label='Lumo')
            ax[1].set_ylabel('eV')
            ax[1].legend()
        else:
            ax = fig.subplots()
            ax.text(0.5, 0.5, "No applicable data", horizontalalignment='center',
                verticalalignment='center', transform=ax.transAxes)

        # Export plot as image buffer
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png')
        image_bytes = buffer.getvalue()
        buffer.close()

        # return dictionary with image data
        return {
            'image': image_bytes,
            'mime-type': 'image/png'
        }
