# data_loader.py

from pathlib import Path

import pandas as pd


def normalize_column_name(name: str) -> str:
    """
    Normalize a single column name:
    - strip leading/trailing spaces
    - convert to lowercase
    - replace internal spaces with underscores
    """
    if not isinstance(name, str):
        name = str(name)

    name = name.strip()              # remove spaces at the start and end
    name = name.lower()              # make everything lowercase
    name = name.replace(" ", "_")    # spaces → underscores

    return name


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply normalize_column_name() to every column in the DataFrame.
    """
    df = df.copy()
    df.columns = [normalize_column_name(col) for col in df.columns]
    return df


def load_dataset(path_str: str) -> pd.DataFrame:
    """
    Load a dataset from CSV or Excel and normalize column names.

    - Accepts: .csv, .xls, .xlsx
    - Raises clear errors if file not found or extension unsupported.
    """
    path = Path(path_str)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    ext = path.suffix.lower()

    try:
        if ext == ".csv":
            df = pd.read_csv(path)
        elif ext in (".xls", ".xlsx"):
            df = pd.read_excel(path)
        else:
            raise ValueError(
                f"Unsupported file extension '{ext}'. "
                "Supported: .csv, .xls, .xlsx"
            )
    except Exception as exc:  # any pandas-related error
        raise RuntimeError(f"Failed to load dataset: {exc}") from exc

    # Normalize column names
    df = normalize_columns(df)

    return df

