# main.py

"""
Entry point for the Data Cleaning & Report Generator tool.

Current capabilities:
- Load a dataset from CSV/Excel.
- Clean it (duplicates, missing values, types, dates).
- Generate in-memory summary statistics.
- Build a PDF report summarizing the results.
- Save the cleaned dataset to a new CSV file.
- Expose a simple CLI interface via argparse.

Usage examples:

    python3 main.py --input sample_large_dataset.csv

    python3 main.py \
        --input sample_large_dataset.csv \
        --output sample_large_dataset_cleaned.csv \
        --report sample_large_report.pdf
"""

import argparse
from pathlib import Path

from data_loader import load_dataset
from cleaning_engine import clean_dataset
from summary_stats import generate_summary
from report_template import build_pdf_report
from export_utils import save_cleaned_dataset


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Data Cleaning & Report Generator",
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input CSV/Excel file.",
    )

    parser.add_argument(
        "--output",
        help=(
            "Path to the cleaned output CSV file. "
            "If not provided, a name will be derived from the input file."
        ),
    )

    parser.add_argument(
        "--report",
        help=(
            "Path to the PDF report file. "
            "If not provided, a name will be derived from the input file."
        ),
    )

    return parser.parse_args()


def derive_default_report_path(input_path: str) -> str:
    """
    Derive a default report filename from the input path.

    Example:
        'data.csv' -> 'data_report.pdf'
    """
    path = Path(input_path)
    return str(path.with_name(f"{path.stem}_report.pdf"))


def main() -> None:
    args = parse_args()

    input_path = args.input

    # Decide on report path
    if args.report:
        output_report = args.report
    else:
        output_report = derive_default_report_path(input_path)

    print(f"Loading dataset from: {input_path}")
    df = load_dataset(input_path)

    print("Running cleaning engine...")
    cleaned_df, cleaning_summary = clean_dataset(df)

    print("Generating summary statistics...")
    summary_data = generate_summary(cleaned_df, cleaning_summary)

    print(f"Building PDF report: {output_report}")
    pdf_path = build_pdf_report(summary_data, output_path=output_report)

    print("Saving cleaned dataset to CSV...")
    cleaned_csv_path = save_cleaned_dataset(
        cleaned_df,
        original_input_path=input_path,
        output_path=args.output,  # may be None → function will derive name
    )

    print("\n=== Done ===")
    print(f"Report written to: {pdf_path}")
    print(f"Cleaned CSV written to: {cleaned_csv_path}")
    print(f"Original shape: {df.shape}")
    print(f"Cleaned shape:  {cleaned_df.shape}")


if __name__ == "__main__":
    main()








