# cleaning_engine.py

from dataclasses import dataclass, field
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd


@dataclass
class CleaningSummary:
    """
    Simple container for information about what happened during cleaning.
    """
    rows_before: int
    rows_after: int
    duplicates_removed: int
    missing_values_before: int
    missing_values_after: int
    column_notes: Dict[str, str] = field(default_factory=dict)

    def as_dict(self) -> Dict[str, object]:
        """
        Convert the summary to a plain dict (useful later for reports).
        """
        return {
            "rows_before": self.rows_before,
            "rows_after": self.rows_after,
            "duplicates_removed": self.duplicates_removed,
            "missing_values_before": self.missing_values_before,
            "missing_values_after": self.missing_values_after,
            "column_notes": self.column_notes,
        }


def _count_missing(df: pd.DataFrame) -> int:
    """
    Count total missing values in the DataFrame.
    """
    return int(df.isna().sum().sum())


def _standardize_dates(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, str]]:
    """
    Try to standardize date columns.

    Strategy:
    - Any column whose name contains 'date' (case-insensitive) is a candidate.
    - We call pandas.to_datetime on those columns with errors='ignore'.

    Returns:
        (updated_df, notes)
    """
    df = df.copy()
    notes: Dict[str, str] = {}

    for col in df.columns:
        if "date" in col.lower():
            # Try to convert to datetime; if it fails, pandas leaves it unchanged.
            before_dtype = str(df[col].dtype)
            df[col] = pd.to_datetime(df[col], errors="ignore")
            after_dtype = str(df[col].dtype)

            if before_dtype != after_dtype:
                notes[col] = f"Converted to datetime (from {before_dtype} to {after_dtype})."
            else:
                notes[col] = "Left as-is (conversion not necessary or not possible)."

    return df, notes


def _normalize_numeric_types(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, str]]:
    """
    Try to turn object columns that look like numbers into numeric dtype.

    Strategy:
    - For each 'object' column, attempt pd.to_numeric with errors='ignore'.
    - If dtype changes, we record a note.
    """
    df = df.copy()
    notes: Dict[str, str] = {}

    for col in df.columns:
        if df[col].dtype == "object":
            before_dtype = str(df[col].dtype)
            converted = pd.to_numeric(df[col], errors="ignore")
            after_dtype = str(converted.dtype)

            if before_dtype != after_dtype:
                df[col] = converted
                notes[col] = f"Converted to numeric (from {before_dtype} to {after_dtype})."

    return df, notes


def _fill_missing_values(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, str]]:
    """
    Fill missing values using a simple, transparent strategy:

    - Numeric columns: fill with median.
    - Boolean columns: fill with False.
    - Datetime columns: leave missing values as-is.
    - Object/string columns: leave missing values as-is.

    Returns:
        (updated_df, notes_per_column)
    """
    df = df.copy()
    notes: Dict[str, str] = {}

    for col in df.columns:
        series = df[col]
        dtype = series.dtype

        # Numeric
        if np.issubdtype(dtype, np.number):
            median_value = series.median()
            df[col] = series.fillna(median_value)
            notes[col] = f"Filled numeric missing values with median ({median_value})."

        # Boolean
        elif dtype == bool:
            df[col] = series.fillna(False)
            notes[col] = "Filled boolean missing values with False."

        # Datetime => leave missing
        elif np.issubdtype(dtype, np.datetime64):
            notes[col] = "Left datetime missing values as-is."

        # Object/string => leave missing
        else:
            notes[col] = "Left missing values as-is (object/string)."

    return df, notes


def clean_dataset(df: pd.DataFrame) -> Tuple[pd.DataFrame, CleaningSummary]:
    """
    High-level function to clean a dataset.

    Steps:
    - Record initial stats.
    - Remove duplicate rows.
    - Standardize date columns.
    - Normalize numeric types where possible.
    - Fill missing values for numeric and boolean columns.
    - Build and return a CleaningSummary.

    Returns:
        (cleaned_df, summary)
    """
    rows_before = len(df)
    missing_before = _count_missing(df)

    # 1) Remove duplicates
    df_no_dupes = df.drop_duplicates()
    rows_after_dupes = len(df_no_dupes)
    duplicates_removed = rows_before - rows_after_dupes

    # 2) Standardize date columns
    df_dates, date_notes = _standardize_dates(df_no_dupes)

    # 3) Normalize numeric types
    df_numeric, numeric_notes = _normalize_numeric_types(df_dates)

    # 4) Fill missing values
    df_filled, fill_notes = _fill_missing_values(df_numeric)

    missing_after = _count_missing(df_filled)

    # Merge notes
    column_notes: Dict[str, str] = {}
    for notes_dict in (date_notes, numeric_notes, fill_notes):
        for key, value in notes_dict.items():
            # If there are multiple notes for same column, join them.
            if key in column_notes:
                column_notes[key] += " | " + value
            else:
                column_notes[key] = value

    summary = CleaningSummary(
        rows_before=rows_before,
        rows_after=len(df_filled),
        duplicates_removed=duplicates_removed,
        missing_values_before=missing_before,
        missing_values_after=missing_after,
        column_notes=column_notes,
    )

    return df_filled, summary

