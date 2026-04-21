import numpy as np
import pandas as pd
import os

def load_data(data_dir):
    df = pd.read_csv(os.path.join(data_dir, 'preprocessed.csv'))
    return df