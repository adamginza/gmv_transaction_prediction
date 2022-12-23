import yaml
import numpy as np
import pandas as pd

from math import sin, cos, sqrt, atan2, radians

def load_yaml(yaml_path):
    """
    Function to load yaml file.
    Params:
    :yaml_path: str
    
    Return:
    :configs: dict
    """
    with open(yaml_path, "r") as f:
        configs = yaml.safe_load(f)
    
    return configs

def iqr(df, col):
    """Function to add a new column with the Upper Bound or Lower Bound of the input column
    Params:
    :df: Pandas DataFrame
    :col: input column - float
    """
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    S = 1.5*IQR
    LB = Q1 - S
    UB = Q3 + S
    df[f'{col}_ub'] = np.where(
        df[col] > UB,
        UB,
        df[col]
    )
    df[f'{col}_lb'] = np.where(
        df[col] < LB,
        LB,
        df[col]
    )
    
def get_distance_lat_lon(lat_from, lon_from, lat_to, lon_to):
    """ Function to get distance based on 2 latitude longitude points
    Params
    :lat_from: Latitude of Source
    :lon_from: Longitude of Source
    :lat_to: Latitude of Destination
    :lon_to: Longitude of Destination
    
    Return
    :distance: float
    """
    if lat_from is None or lon_from is None or lat_to is None or lon_to is None:
        return 0
    
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat_from)
    lon1 = radians(lon_from)
    lat2 = radians(lat_to)
    lon2 = radians(lon_to)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    
    return distance