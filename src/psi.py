import numpy as np
import pandas as pd

class PSIValidator:

    @staticmethod
    def calculate_psi(
        expected,
        actual,
        bins=10
    ):

        bin_edges = pd.qcut(
            expected,
            bins,
            retbins=True,
            duplicates="drop"
        )[1]

        expected_bins = pd.cut(
            expected,
            bins=bin_edges,
            include_lowest=True
        )

        actual_bins = pd.cut(
            actual,
            bins=bin_edges,
            include_lowest=True
        )

        expected_pct = (
            expected_bins
            .value_counts(normalize=True)
            .sort_index()
        )

        actual_pct = (
            actual_bins
            .value_counts(normalize=True)
            .sort_index()
        )

        expected_pct = np.where(
            expected_pct == 0,
            0.0001,
            expected_pct
        )

        actual_pct = np.where(
            actual_pct == 0,
            0.0001,
            actual_pct
        )

        psi = np.sum(
            (actual_pct - expected_pct)
            *
            np.log(
                actual_pct / expected_pct
            )
        )

        return round(
            psi,
            4
        )