import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def remove_outliers_iqr(df, column, factor=1.5):
    """
    Removes outliers from a column using the IQR method.

    Parameters:
    - df (pd.DataFrame): DataFrame to process
    - column (str): Target column
    - factor (float): IQR multiplier

    Returns:
    - pd.DataFrame: Cleaned DataFrame
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - factor * IQR
    upper = Q3 + factor * IQR
    mask = (df[column] >= lower) & (df[column] <= upper)
    print(f"🔍 Removed {len(df) - mask.sum()} outliers from '{column}' using IQR")
    return df[mask]

def remove_outliers_zscore(df, column, threshold=3.0):
    """
    Removes outliers based on Z-score.

    Parameters:
    - df (pd.DataFrame): DataFrame to process
    - column (str): Target column
    - threshold (float): Z-score threshold

    Returns:
    - pd.DataFrame: Cleaned DataFrame
    """
    z_scores = zscore(df[column].fillna(df[column].mean()))
    mask = np.abs(z_scores) < threshold
    print(f"📏 Removed {len(df) - mask.sum()} outliers from '{column}' using Z-score")
    return df[mask]

def log_transform(df, column):
    """
    Apply log transformation to a column.

    Parameters:
    - df (pd.DataFrame)
    - column (str)

    Returns:
    - pd.DataFrame
    """
    df = df.copy()
    df[column + "_log"] = np.log1p(df[column])
    print(f"🧮 Applied log transformation to '{column}' → '{column}_log'")
    return df

def min_max_scale(df, column):
    """
    Apply Min-Max scaling.

    Returns:
    - df with new column: column_scaled
    """
    scaler = MinMaxScaler()
    df = df.copy()
    df[column + '_scaled'] = scaler.fit_transform(df[[column]])
    print(f"📐 Min-Max scaled '{column}' → '{column}_scaled'")
    return df

def standardize(df, column):
    """
    Apply standard scaling.

    Returns:
    - df with new column: column_std
    """
    scaler = StandardScaler()
    df = df.copy()
    df[column + '_std'] = scaler.fit_transform(df[[column]])
    print(f"📊 Standardized '{column}' → '{column}_std'")
    return df
