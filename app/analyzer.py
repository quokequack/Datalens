import math
import pandas as pd

class DataAnalyzer:
    def analyze(self, df: pd.DataFrame) -> dict:
        return {
            "total_registros": len(df),
            "total_colunas": len(df.columns),
            "nulos_por_coluna": self._count_nulls(df),
            "duplicados": self._count_duplicates(df),
            "estatisticas": self._numeric_statistics(df)
        }

    def _count_nulls(self, df: pd.DataFrame) -> dict:
        counts = df.isna().sum()
        return {
            str(column): int(value)
            for column, value in counts.items()
        }

    def _count_duplicates(self, df: pd.DataFrame) -> int:
        return int(df.duplicated().sum())

    def _numeric_statistics(self, df: pd.DataFrame) -> dict:
        numeric_df = df.select_dtypes(include="number")

        if numeric_df.empty:
            return {}

        summary = numeric_df.describe()
        statistics = {}

        for column in summary.columns:
            statistics[str(column)] = {}

            for metric, value in summary[column].items():
                number = float(value)

                statistics[str(column)][metric] = (
                    number if math.isfinite(number) else None
                )
        return statistics