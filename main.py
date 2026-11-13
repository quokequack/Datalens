import pandas as pd
from analyzer import analisar_dataframe
from pprint import pprint

dataFrame = pd.read_csv("data/funcionarios.csv")
resultado = analisar_dataframe(dataFrame)

pprint(resultado)
