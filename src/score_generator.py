import pandas as pd


class ScoreGenerator:

    @staticmethod
    def generate_scores(
            model,
            df
    ):

        X = df.drop(
            columns=[
                "customer_id",
                "snapshot_month",
                "bad_flag"
            ],
            errors="ignore"
        )
        print("Scoring Columns:")
        print(X.columns.tolist())

        scores = model.predict_proba(
            X
        )[:, 1]

        scoring_output = pd.DataFrame({

            "customer_id":
                df["customer_id"],

            "bad_flag":
                df["bad_flag"],

            "pd_score":
                scores
        })

        return scoring_output
