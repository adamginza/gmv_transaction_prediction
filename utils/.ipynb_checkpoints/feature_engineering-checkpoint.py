import pandas as pd


def create_features(df):
    """
    EXTRACT TIME BASED FEATURES
    """
    df = df.copy()
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['dayofyear'] = df.index.dayofyear
    df['weekofyear'] = df.index.isocalendar().week.astype(int)
    df['is_weekend'] = (df.index.weekday >= 5).astype(int)

    return df

def add_lags(df, target_col):
    """
    Adding Lag Features from current DataFrame
    """
    df = df.copy()
    target_map = df[target_col].to_dict()
    
    df['ft_lag_31'] = (df.index - pd.Timedelta('31 days')).map(target_map)
    df['ft_lag_62'] = (df.index - pd.Timedelta('62 days')).map(target_map)
    df['ft_lag_93'] = (df.index - pd.Timedelta('93 days')).map(target_map)
    df['ft_lag_124'] = (df.index - pd.Timedelta('124 days')).map(target_map)
    df['ft_lag_155'] = (df.index - pd.Timedelta('155 days')).map(target_map)
    df['ft_lag_186'] = (df.index - pd.Timedelta('186 days')).map(target_map)
    df['ft_lag_217'] = (df.index - pd.Timedelta('217 days')).map(target_map)
    df['ft_lag_248'] = (df.index - pd.Timedelta('248 days')).map(target_map)
    df['ft_lag_279'] = (df.index - pd.Timedelta('279 days')).map(target_map)
    df['ft_lag_310'] = (df.index - pd.Timedelta('310 days')).map(target_map)
    df['ft_lag_341'] = (df.index - pd.Timedelta('341 days')).map(target_map)
    df['ft_lag_372'] = (df.index - pd.Timedelta('372 days')).map(target_map)

    return df