# PaleoMagKit

Jupyter notebooks for paleomagnetic and rock-magnetic data processing.

## Notebooks

| Notebook | Analysis |
| --- | --- |
| [01 — ANU VSM screening and DCD export](notebooks/01_ANU_VSM_Screening_DCD_Export_v01.ipynb) | Hysteresis and backfield screening, Day plots, Bcr and DCD conversion. |
| [02 — DCD unmixing (Egli SGG)](notebooks/02_DCD_Egli_Unmixing_Interactive_v01.ipynb) | Direct DCD fitting, component comparison, bootstrap and export. |

## Installation

Run the notebooks in JupyterLab or VS Code. Install the dependencies with:

```bash
python -m pip install numpy pandas scipy matplotlib ipywidgets openpyxl
```

Optional: `ipyfilechooser` (file browser), `xlrd` (legacy Excel files).

Sample VSM and DCD measurements are in `examples/vsm/` (specimen TA04-05).

## Tests

```bash
python -m unittest discover -s tests -v
```

## License

Code and documentation: [MIT](LICENSE). Example measurements in `examples/vsm/`: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (cite PaleoMagKit and specimen TA04-05). Third-party material retains its original licensing.
