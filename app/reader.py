from io import BytesIO
from pathlib import Path

import pandas as pd

class CSVReader:
    def read(self, file_path: str | Path) -> pd.DataFrame:
        return pd.read_csv(
            file_path, encoding="utf-8-sig"
        )
    def read_bytes(self, content: bytes) -> pd.DataFrame:
        return pd.read_csv(
            BytesIO(content),
            encoding="utf-8-sig"
        )