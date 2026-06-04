from pathlib import Path
import pandas as pd

from src.config import (
    VALIDATION_FILE,
    DEVELOPMENT_FILE,
    DEVELOPMENT_RESULTS_FILE,
    MODEL_FILE,
    OUTPUT_DIR,
    REPORT_DIR
)

from src.data_loader import DataLoader
from src.model_loader import ModelLoader
from src.score_generator import ScoreGenerator
from src.performance_validator import PerformanceValidator
from src.rank_ordering import RankOrdering
from src.calibration import Calibration
from src.psi import PSIValidator
from src.benchmark import Benchmark
from src.report_generator import ReportGenerator



def main():

    # ----------------------------------
    # Create Output Folders
    # ----------------------------------

    Path(OUTPUT_DIR).mkdir(
        exist_ok=True
    )

    Path(REPORT_DIR).mkdir(
        exist_ok=True
    )

    print("Folders Checked")

    # ----------------------------------
    # Load Validation Data
    # ----------------------------------

    df = DataLoader.load_csv(
        VALIDATION_FILE
    )

    print(
        f"Validation Data Loaded: {df.shape}"
    )

    dev_df = DataLoader.load_csv(
        DEVELOPMENT_FILE
    )

    # ----------------------------------
    # Load Model
    # ----------------------------------

    model = ModelLoader.load_model(
        MODEL_FILE
    )

    print(
        "Model Loaded Successfully"
    )

    # ----------------------------------
    # Generate Scores
    # ----------------------------------

    scoring_df = (
        ScoreGenerator
        .generate_scores(
            model,
            df
        )
    )

    scoring_df.to_csv(
        OUTPUT_DIR /
        "scoring_output.csv",
        index=False
    )

    print(
        "Scoring Output Generated"
    )

    dev_scoring_df = (
        ScoreGenerator
        .generate_scores(
            model,
            dev_df
        )
    )

    # ----------------------------------
    # Calculate Metrics
    # ----------------------------------

    auc = (
        PerformanceValidator
        .calculate_auc(
            scoring_df["bad_flag"],
            scoring_df["pd_score"]
        )
    )

    gini = (
        PerformanceValidator
        .calculate_gini(
            auc
        )
    )

    ks = (
        PerformanceValidator
        .calculate_ks(
            scoring_df["bad_flag"],
            scoring_df["pd_score"]
        )
    )

    print(
        f"AUC  : {auc:.4f}"
    )

    print(
        f"GINI : {gini:.4f}"
    )

    print(
        f"KS   : {ks:.4f}"
    )

    # ----------------------------------
    # Rank Ordering
    # ----------------------------------

    rank_table = (
        RankOrdering
        .create_deciles(
            scoring_df
        )
    )

    rank_table.to_excel(
        OUTPUT_DIR /
        "rank_ordering.xlsx",
        index=False
    )

    print(
        "Rank Ordering Completed"
    )

    # ----------------------------------
    # Calibration
    # ----------------------------------

    calibration_table = (
        Calibration
        .generate_table(
            scoring_df
        )
    )

    calibration_table.to_excel(
        OUTPUT_DIR /
        "calibration.xlsx",
        index=False
    )

    print(
        "Calibration Completed"
    )

    # ----------------------------------
    # PSI
    # ----------------------------------

    psi_value = PSIValidator.calculate_psi(
        dev_scoring_df["pd_score"],
        scoring_df["pd_score"]
    )

    print(
        f"PSI : {psi_value}"
    )

    # ----------------------------------
    # Benchmark Comparison
    # ----------------------------------

    dev_metrics = pd.read_excel(
        DEVELOPMENT_RESULTS_FILE
    )

    validation_metrics = {

        "AUC": auc,
        "KS": ks,
        "GINI": gini
    }

    comparison = (
        Benchmark
        .compare_metrics(
            {
                "AUC":
                dev_metrics.loc[
                    0,
                    "AUC"
                ],

                "KS":
                dev_metrics.loc[
                    0,
                    "KS"
                ],

                "GINI":
                dev_metrics.loc[
                    0,
                    "GINI"
                ]
            },

            validation_metrics
        )
    )

    comparison.to_excel(
        OUTPUT_DIR /
        "validation_summary.xlsx",
        index=False
    )

    print(
        "Benchmark Comparison Completed"
    )

    # ----------------------------------
    # Generate Report
    # ----------------------------------

    ReportGenerator.create_report(

        auc=auc,

        ks=ks,

        gini=gini,

        psi=psi_value,

        report_path=
        REPORT_DIR /
        "validation_report.docx"
    )

    print(
        "Validation Report Generated"
    )

    print(
        "\nValidation Completed Successfully"
    )


if __name__ == "__main__":
    main()