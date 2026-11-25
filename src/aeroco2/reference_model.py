import pandas as pd

def load_flight_data(filepath):
    """
    Load flight data from a CSV file.

    Args:
        filepath (path) : path to the csv file

    Returns:
        DataFrame: Loaded flight data.
    """
    df = pd.read_csv(filepath, parse_dates=["timestamp"], dtype={"icao24": str},)
    df = df.assign(d_ts=lambda d: d.timestamp.diff().dt.total_seconds().bfill())
    return df