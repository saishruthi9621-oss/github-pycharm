import pandas as pd


class Benchmark:

    @staticmethod
    def compare_metrics(
            dev_metrics,
            val_metrics
    ):

        comparison = pd.DataFrame({

            "Metric":

                ["AUC",
                 "KS",
                 "GINI"],

            "Development":

                [
                    dev_metrics["AUC"],
                    dev_metrics["KS"],
                    dev_metrics["GINI"]
                ],

            "Validation":

                [
                    val_metrics["AUC"],
                    val_metrics["KS"],
                    val_metrics["GINI"]
                ]
        })

        return comparison