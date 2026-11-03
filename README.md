# PaleoMagKit

Python tools and interactive Jupyter notebooks for paleomagnetic and rock-magnetic data processing and analysis.

## Notebooks

| Notebook | Description |
| --- | --- |
| [01 — ANU VSM Screening and DCD Export](notebooks/01_ANU_VSM_Screening_DCD_Export_v01.ipynb) | Preliminary hysteresis and backfield analysis, Day plots and backfield conversion for DCD unmixing. |
| [02 — DCD Egli Unmixing](notebooks/02_DCD_Egli_Unmixing_Interactive_v01.ipynb) | Direct DCD fitting with Egli SGG components, component comparison, bootstrap uncertainty and exports. |

Each notebook contains its own usage instructions, scientific conventions, limitations and references. More tools will be added as they are reviewed and tested.

## Getting started

Open the notebooks in JupyterLab or VS Code with a Jupyter-compatible Python environment. Install the common dependencies with:

```bash
python -m pip install numpy pandas scipy matplotlib ipywidgets openpyxl
```

Optional packages: `ipyfilechooser` for directory selection and `xlrd` for legacy Excel files. Notebook-specific requirements are listed in their introductions.

The `examples/vsm/` directory contains real hysteresis, backfield and converted DCD measurements of specimen TA04-05 for testing and demonstration. Other notebooks may reuse these measurements.

## Tests

```bash
python -m unittest discover -s tests -v
```

## License

Code and documentation are available under the [MIT License](LICENSE). Original example measurement data in `examples/vsm/` are shared under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); please attribute PaleoMagKit and identify specimen TA04-05 when reusing them. Third-party scientific material remains subject to its own rights.
