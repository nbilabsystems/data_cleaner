# summary_stats.py

from typing import Any, Dict, List

import numpy as np
import pandas as pd

from cleaning_engine import CleaningSummary


def _global_stats(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Compute high-level statistics about the dataset.
    """
    return {
        "num_rows": int(df.shape[0]),
        "num_columns": int(df.shape[1]),
        "total_missing_values": int(df.isna().sum().sum()),
        "columns": list(df.columns),
    }


def _numeric_column_stats(series: pd.Series) -> Dict[str, Any]:
    """
    Stats for numeric columns.
    """
    desc = series.describe()  # count, mean, std, min, 25%, 50%, 75%, max

    return {
        "dtype": str(series.dtype),
        "non_null_count": int(desc["count"]),
        "missing_count": int(series.isna().sum()),
        "mean": float(desc["mean"]) if not np.isnan(desc["mean"]) else None,
        "std": float(desc["std"]) if not np.isnan(desc["std"]) else None,
        "min": float(desc["min"]) if not np.isnan(desc["min"]) else None,
        "max": float(desc["max"]) if not np.isnan(desc["max"]) else None,
        "median": float(series.median()) if not np.isnan(series.median()) else None,
    }


def _non_numeric_column_stats(series: pd.Series) -> Dict[str, Any]:
    """
    Stats for non-numeric columns (strings, booleans, datetimes, etc.).
    """
    return {
        "dtype": str(series.dtype),
        "non_null_count": int(series.notna().sum()),
        "missing_count": int(series.isna().sum()),
        "num_unique_values": int(series.nunique(dropna=True)),
        "sample_values": [str(v) for v in series.dropna().unique()[:5]],
    }


def _per_column_stats(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """
    Build a list of per-column statistics.
    """
    results: List[Dict[str, Any]] = []

    for col in df.columns:
        series = df[col]

        if np.issubdtype(series.dtype, np.number):
            stats = _numeric_column_stats(series)
        else:
            stats = _non_numeric_column_stats(series)

        stats["column_name"] = col
        results.append(stats)

    return results


def generate_summary(
    cleaned_df: pd.DataFrame,
    cleaning_summary: CleaningSummary,
) -> Dict[str, Any]:
    """
    Combine:
    - cleaning summary
    - global dataset stats
    - per-column stats

    into a single structured dict that can be used later by the PDF builder.
    """
    global_stats = _global_stats(cleaned_df)
    column_stats = _per_column_stats(cleaned_df)

    return {
        "cleaning_summary": cleaning_summary.as_dict(),
        "global_stats": global_stats,
        "columns": column_stats,
    }


