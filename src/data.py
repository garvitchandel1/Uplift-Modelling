import pandas as pd
from sklearn.model_selection import train_test_split

import pandas as pd

def load_data(path, sample_size=None, random_state=42):
    
    dtype_dict = {f"f{i}": "float32" for i in range(12)}
    dtype_dict["treatment"] = "int8"
    dtype_dict["conversion"] = "int8"
    dtype_dict["visit"] = "int8"
    dtype_dict["exposure"] = "int8"

    df = pd.read_csv(path, dtype=dtype_dict)

    if sample_size:
        df = df.sample(n=sample_size, random_state=random_state)

    return df

def train_test_split_uplift(df, test_size=0.3, random_state=42):
    
    X = df.drop(columns=['conversion'])
    y = df['conversion']
    
    return train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=df[['treatment', 'conversion']]
    )