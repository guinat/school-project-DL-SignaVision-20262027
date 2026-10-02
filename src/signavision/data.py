from pathlib import Path

import pandas as pd

from .config import DATA_DIR, KAGGLE_DATASET


def get_data_dir() -> Path:
    if DATA_DIR.exists():
        return DATA_DIR
    import kagglehub

    return Path(kagglehub.dataset_download(KAGGLE_DATASET))


def load_metadata(data_dir: Path | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    data_dir = data_dir or get_data_dir()
    train = pd.read_csv(data_dir / "Train.csv")
    test = pd.read_csv(data_dir / "Test.csv")
    train["track"] = train["Path"].str.extract(r"/(\d{5}_\d{5})_")[0]
    return train, test
