import numpy as np


class PSIValidator:

    @staticmethod
    def calculate_psi(
            expected,
            actual,
            bins=10
    ):

        expected_pct = (

            np.histogram(
                expected,
                bins
            )[0]

            /
            len(expected)
        )

        actual_pct = (

            np.histogram(
                actual,
                bins
            )[0]

            /
            len(actual)
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

            (
                actual_pct
                -
                expected_pct
            )

            *

            np.log(

                actual_pct
                /
                expected_pct
            )
        )

        return round(
            psi,
            4
        )