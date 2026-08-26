
import pandas as pd


def load(path: str) -> pd.DataFrame:
    assert type(path) is str, "path not string."
    df = pd.read_csv(path)
    print("Loading dataset of dimensions", df.shape)
    return df
