import pandas as pd


class Calibration:

    @staticmethod
    def generate_table(
            scoring_df
    ):

        scoring_df["bucket"] = pd.qcut(

            scoring_df["pd_score"],

            10,

            duplicates="drop"
        )

        result = (

            scoring_df

            .groupby("bucket")

            .agg(

                predicted_pd=
                (
                    "pd_score",
                    "mean"
                ),

                actual_bad_rate=
                (
                    "bad_flag",
                    "mean"
                )
            )

            .reset_index()
        )

        return result