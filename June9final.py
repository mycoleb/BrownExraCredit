import pandas as pd
import numpy as np
import re

# I read the CSV file
df = pd.read_csv('cells.csv')

# I replace invalid or missing values with null
df['oem'] = df['oem'].apply(lambda x: np.nan if pd.isnull(x) or x == '' else x)
df['model'] = df['model'].apply(lambda x: np.nan if pd.isnull(x) or x == '' else x)
df['body_dimensions'] = df['body_dimensions'].apply(lambda x: np.nan if pd.isnull(x) or x == '' else x)
df['body_sim'] = df['body_sim'].apply(lambda x: np.nan if pd.isnull(x) or x == 'No' else x)
df['display_type'] = df['display_type'].apply(lambda x: np.nan if pd.isnull(x) or x == '' else x)
df['display_resolution'] = df['display_resolution'].apply(lambda x: np.nan if pd.isnull(x) or x == '' else x)
df['features_sensors'] = df['features_sensors'].apply(lambda x: np.nan if pd.isnull(x) or x == '' else x)

# I transform launch_announced to integer year
df['launch_announced'] = df['launch_announced'].apply(lambda x: int(re.findall(r'\d{4}', str(x))[0]) if re.findall(r'\d{4}', str(x)) else np.nan)

# I transform launch_status to integer year or leave as is if 'Discontinued' or 'Cancelled'
def transform_launch_status(x):
    if pd.isnull(x) or x == '':
        return np.nan
    elif x == 'Discontinued' or x == 'Cancelled':
        return x
    else:
        return int(re.findall(r'\d{4}', str(x))[0]) if re.findall(r'\d{4}', str(x)) else np.nan

df['launch_status'] = df['launch_status'].apply(transform_launch_status)

# I transform body_weight to float
df['body_weight'] = df['body_weight'].apply(lambda x: float(re.findall(r'\d+\.?\d*', str(x))[0]) if re.findall(r'\d+\.?\d*', str(x)) else np.nan)

# I transform display_size to float
df['display_size'] = df['display_size'].apply(lambda x: float(re.findall(r'\d+\.?\d*', str(x))[0]) if re.findall(r'\d+\.?\d*', str(x)) else np.nan)

# I shorten platform_os to the name
def shorten_platform_os(x):
    if pd.isnull(x) or x == '':
        return np.nan
    else:
        return re.split(r',', str(x))[0]

df['platform_os'] = df['platform_os'].apply(shorten_platform_os)

# I save the transformed DataFrame to a new CSV file
df.to_csv('cells_transformed.csv', index=False)