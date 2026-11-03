"""Numerical regression checks for the DCD/Egli interactive notebook.

Run from the repository root with:
    python -m unittest discover -s tests -v

The tests load the notebook engine cell directly, until the numerical
functions are extracted into the reusable paleomagkit Python package.
"""
from pathlib import Path
import json
import tempfile
import unittest

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "02_DCD_Egli_Unmixing_Interactive_v01.ipynb"
REAL_DCD = (
    ROOT
    / "examples"
    / "DCD"
    / "processed_dcd"
    / "DCD_clean_magnetization"
    / "TA04-05-5s_500mT_back_unmix.back"
)


def load_engine():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    source = "".join(notebook["cells"][1]["source"])
    namespace = {"__name__": "_dcd_engine_for_testing"}
    exec(compile(source, str(NOTEBOOK), "exec"), namespace)
    return namespace


def config(**overrides):
    settings = dict(
        fit_mode="independent",
        coupled_parameters=["Bh", "DP"],
        similarity_strength=0.05,
        use_asymmetry=True,
        s_min=0.75,
        dp_bounds=(0.03, 0.60),
        n_starts=4,
        max_nfev=1800,
        random_seed=42,
        grid_points=250,
        field_unit="auto",
        smooth=False,
        smoothing_s=0.01,
        spectrum_method="absolute",
        n_components=1,
        bh_bounds_mT=[(5., 100.)],
    )
    settings.update(overrides)
    return settings


class TestDcdEgli(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = load_engine()

    def test_gaussian_median_equals_mode(self):
        n = self.engine
        for field in (12., 30., 90.):
            sigma, mode_z, peak = n["egli_geometry"](0.25, 1.)
            self.assertAlmostEqual(mode_z, 0., places=12)
            self.assertAlmostEqual(10 ** (np.log10(field) + sigma * mode_z), field, places=8)
            self.assertAlmostEqual(peak, 1., places=12)
            self.assertAlmostEqual(n["component_survival"](np.log10(field), np.log10(field), .25, 1.), .5, places=12)

    def test_asymmetric_median_vs_peak(self):
        n = self.engine
        bh, dp, S = 35., .28, .75
        sigma, mode_z, _ = n["egli_geometry"](dp, S)
        peak_field = 10 ** (np.log10(bh) + sigma * mode_z)
        self.assertGreater(peak_field, bh)
        self.assertAlmostEqual(n["component_survival"](np.log10(bh), np.log10(bh), dp, S), .5, places=10)
        xx = np.linspace(np.log10(5), np.log10(150), 20001)
        density = n["component_curve"](xx, np.log10(bh), dp, 1., 1., S)
        numeric_peak = 10 ** xx[np.argmax(density)]
        self.assertAlmostEqual(numeric_peak / peak_field, 1., delta=1e-3)

    def test_synthetic_asymmetric_fit(self):
        n = self.engine
        bh, dp, S = 35., .28, .75
        fields = np.r_[0., np.geomspace(.05, 400, 160)]
        moments = np.r_[1., n["component_survival"](np.log10(fields[1:]), np.log10(bh), dp, S)]
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "synthetic_DCD.csv"
            pd.DataFrame({"Field_mT": fields, "Moment_Am2": moments}).to_csv(path, index=False)
            settings = config()
            fit = n["fit_samples"]([n["read_dcd"](path, settings)], settings, progress=None)[0]
        params = fit["table"].iloc[0]
        self.assertTrue(fit["metrics"]["Optimizer_success"])
        self.assertAlmostEqual(params.Bh_mT, bh, delta=.1)
        self.assertAlmostEqual(params.DP, dp, delta=.01)
        self.assertAlmostEqual(params.S, S, delta=.01)
        self.assertLess(fit["metrics"]["RMSE_DCD_normalized"], 1e-5)

    def test_ta04_05_real_dcd_regression(self):
        n = self.engine
        self.assertTrue(REAL_DCD.is_file(), "Shared TA04-05 example is missing")
        settings = config(n_components=3, bh_bounds_mT=[(2., 18.), (18., 80.), (80., 250.)], n_starts=6)
        fit = n["fit_samples"]([n["read_dcd"](REAL_DCD, settings)], settings, progress=None)[0]
        rows = fit["table"].sort_values("Component")
        self.assertTrue(fit["metrics"]["Optimizer_success"])
        self.assertLess(fit["metrics"]["RMSE_DCD_normalized"], .001)
        # Loose tolerances: detect a broken model, not harmless optimizer differences.
        self.assertAlmostEqual(rows.iloc[0].Bh_mT, 10.58, delta=2.)
        self.assertAlmostEqual(rows.iloc[1].Bh_mT, 23.60, delta=1.)
        self.assertGreater(rows.iloc[1].Bh_mode_mT, rows.iloc[1].Bh_mT)


if __name__ == "__main__":
    unittest.main()
