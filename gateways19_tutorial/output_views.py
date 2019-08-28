import io

import numpy as np
from matplotlib.figure import Figure

class GaussianLogViewProvider:
    display_type = 'image'
    name = "Gaussian Log Viewer"

    def generate_data(self, request, experiment_output, experiment, output_file=None):
        # return dictionary with image data
        N = 500
        x = np.random.rand(N)
        y = np.random.rand(N)
        fig = Figure()
        ax = fig.subplots()
        ax.scatter(x, y)
        ax.set_title('Random scatterplot')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png')
        image_bytes = buffer.getvalue()
        buffer.close()
        return {
            'image': image_bytes,
            'mime-type': 'image/png'
        }
