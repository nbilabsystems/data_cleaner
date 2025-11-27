# export_utils.py

from pathlib import Path

import pandas as pd


def make_cleaned_filename(original_path: str) -> str:
    """
    Given an original input file path, build a safe output filename.

    Example:
        'sample_large_dataset.csv' -> 'sample_large_dataset_cleaned.csv'
    """
    path = Path(original_path)
    new_name = f"{path.stem}_cleaned{path.suffix}"
    return str(path.with_name(new_name))


def save_cleaned_dataset(
    cleaned_df: pd.DataFrame,
    original_input_path: str,
    output_path: str | None = None,
) -> str:
    """
    Save the cleaned DataFrame to CSV.

    - If output_path is None, derive it from original_input_path.
    - Uses UTF-8 encoding and includes header.

    Returns:
        The path to the saved file.
    """
    if output_path is None:
        output_path = make_cleaned_filename(original_input_path)

    cleaned_df.to_csv(output_path, index=False, encoding="utf-8")
    return output_path

