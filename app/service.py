from app.analyzer import DataAnalyzer
from app.reader import CSVReader

class AnalysisService:
    def __init__(self, reader: CSVReader, analyzer: DataAnalyzer):
        self.reader = reader
        self.analyzer = analyzer

    def analyze_file(self, file_path: str) -> dict:
        dataframe = self.reader.read(file_path)
        return dataframe

    def analyze_bytes(self, content: bytes) -> dict:
        dataframe = self.reader.read_bytes(content)
        return self.analyzer.analyze(dataframe)