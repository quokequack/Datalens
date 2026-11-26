import pandas as pd 

from app.analyzer import DataAnalyzer

class TestDataAnalyzer:
    def setup_method(self):
        self.analyzer = DataAnalyzer()

    def test_total_records(self):
        df = pd.DataFrame({
            "name": ["Ana", "Bruno", "Carla"]
        })

        result = self.analyzer.analyze(df)

        assert result["total_registros"] == 3

    def test_null_values(self):
        df = pd.DataFrame({
            "name": ["Ana", None, "Carla"]
        })

        result = self.analyzer.analyze(df)

        assert result["nulos_por_coluna"]["name"] == 1

    def test_duplicates(self):
        df = pd.DataFrame({
            "name": ["Ana", "Carla", "Ana"]
        })

        result = self.analyzer.analyze(df)

        assert result["duplicados"] == 1

    def test_numeric_average(self):
        df = pd.DataFrame({
            "age": [20, 20, 30]
        })

        result = self.analyzer.analyze(df)

        assert result["estatisticas"]["age"]["mean"] == 30
        
