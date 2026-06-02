import pandas as pd


class RankOrdering:

    @staticmethod
    def create_deciles(
            scoring_df
    ):

        scoring_df["decile"] = pd.qcut(

            scoring_df["pd_score"],

            10,

            labels=False,

            duplicates="drop"
        )

        result = (

            scoring_df

            .groupby("decile")

            .agg(

                accounts=
                (
                    "customer_id",
                    "count"
                ),

                bad_rate=
                (
                    "bad_flag",
                    "mean"
                )
            )

            .reset_index()
        )

        return result