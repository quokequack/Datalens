import pandas as pd

from app.analyzer import DataAnalyzer
from app.reader import CSVReader
from app.service import AnalysisService

reader = CSVReader()
analyzer = DataAnalyzer()

service = AnalysisService(reader, analyzer)

result = service.analyze_file("data/funcionarios.csv")

print(result)

