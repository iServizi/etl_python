#Utwórz klasę CsvExtractor z metodą extract. Parametry metody extract: path.
import pandas as pd

class CsvExtractor():
    def extract(self,path):
        return pd.read_csv(path, encoding='utf-8')