# PaleoMagKit

Jupyter notebooks for paleomagnetic and rock-magnetic data processing.

## Notebooks

| Notebook | Analysis |
| --- | --- |
| [01 — ANU VSM screening and DCD export](notebooks/01_ANU_VSM_Screening_DCD_Export_v01.ipynb) | Hysteresis and backfield screening, Day plots, Bcr and DCD conversion. |
| [02 — DCD unmixing (Egli SGG)](notebooks/02_DCD_Egli_Unmixing_Interactive_v01.ipynb) | Direct DCD fitting, component comparison, bootstrap and export. |
| [FORC multipanel](notebooks/Plot_FORCs-Multipanel.ipynb) | Multi-panel FORC figures from FORCsensei and FORCtool exports. |

## Installation

Run the notebooks in JupyterLab or VS Code. Install the dependencies with:

```bash
python -m pip install numpy pandas scipy matplotlib ipywidgets openpyxl
```

Optional: `ipyfilechooser` (file browser), `xlrd` (legacy Excel files).

Sample files are in `examples/`, including VSM, DCD and FORC data.

## Tests

```bash
python -m unittest discover -s tests -v
```

## License

Code and documentation: [MIT](LICENSE). The project authors confirm that datasets in `examples/` are their own and authorize their inclusion in this repository. The TA04-05 hysteresis and backfield measurements (`examples/hys/TA04-05-500ms_500mT_hys` and `examples/DCD/raw_dcd/TA04-05-5s_500mT_back`) are shared under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (cite PaleoMagKit and specimen TA04-05). No additional reuse license is specified for other example datasets.
