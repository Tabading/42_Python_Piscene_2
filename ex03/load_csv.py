
import pandas as pd


def load(path: str) -> pd.DataFrame:
    ''' Load a csv file and return it as a Dataset. '''
    assert type(path) is str, "path not string."
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except Exception:
        pass
    return None
