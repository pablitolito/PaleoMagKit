# PaleoMagKit
Python tools and interactive Jupyter notebooks for reproducible paleomagnetic and rock-magnetic data analysis
# PaleoMagKit

Python tools and interactive Jupyter notebooks for paleomagnetic and rock-magnetic data processing and analysis.

## Notebooks

**01 — ANU VSM Screening and DCD Export**

Processes hysteresis and backfield measurements from the ANU vibrating sample magnetometer. Provides preliminary hysteresis parameters, Day plots, backfield coercivity estimates and conversion of backfield measurements for DCD analysis.

The paramagnetic correction is intended for preliminary screening, not detailed magnetic characterization.

**02 — DCD Egli Unmixing**

Fits coercivity components directly to DCD curves using skewed generalized Gaussian (SGG) distributions. Supports multiple components, asymmetric distributions, parameter constraints, bootstrap confidence intervals and graphical exports.

## Installation

The notebooks require Python, Jupyter and the following packages:

`numpy`, `pandas`, `scipy`, `matplotlib`, `ipywidgets`, `openpyxl`

Optional: `ipyfilechooser` for folder selection and `xlrd` for legacy Excel files.

## Example data

The `examples/vsm/` folder contains hysteresis and backfield measurements of specimen TA04-05, together with a converted DCD curve.

These measurements are provided for testing and demonstrating the notebooks.

## Usage

Open a notebook in JupyterLab or VS Code, run its cells and select the input and output directories through the interactive interface.

## Tests

Run the DCD validation tests with:

`python -m unittest discover -s tests -v`

## License

Code and documentation are released under the MIT License (see `LICENSE`).

Original example measurement data in `examples/vsm/` are available under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

Third-party scientific references and material remain subject to their respective rights.