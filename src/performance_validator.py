import pandas as pd

from sklearn.metrics import (
    roc_auc_score
)


class PerformanceValidator:

    @staticmethod
    def calculate_auc(
            y_true,
            pd_score
    ):

        return roc_auc_score(
            y_true,
            pd_score
        )

    @staticmethod
    def calculate_gini(
            auc
    ):

        return (
            2 * auc
        ) - 1

    @staticmethod
    def calculate_ks(
            y_true,
            pd_score
    ):

        df = pd.DataFrame({

            "target": y_true,

            "score": pd_score
        })

        df = df.sort_values(
            "score",
            ascending=False
        )

        df["good"] = (
            1 - df["target"]
        )

        df["cum_bad"] = (

            df["target"]
            .cumsum()
            /
            df["target"].sum()
        )

        df["cum_good"] = (

            df["good"]
            .cumsum()
            /
            df["good"].sum()
        )

        ks = max(
            abs(
                df["cum_bad"]
                -
                df["cum_good"]
            )
        )

        return ks