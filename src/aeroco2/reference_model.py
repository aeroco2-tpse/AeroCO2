def load_flight_data(filepath):
    """
    Load flight data from a CSV file.

    Args:
        filepath (path) : path to the csv file

    Returns:
        DataFrame: Loaded flight data.
    """
    return pd.read_csv(filepath, sep=";", decimal=",", encoding="utf-8")