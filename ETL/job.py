#Utwórz klasę Job. Parametry konstruktora: input_path, output_path oraz obiekty typu: CsvExtractor, Deduplicator, JsonLoader. Metoda run nie posiada parametrów, ale odpowiada za uruchomienie job'a.
import pandas as pd

class Job():
    def __init__(self, input_path, output_path, extractor, deduplicator, jsonloader):
        self.input_path = input_path
        self.output_path = output_path
        self.extractor = extractor
        self.deduplicator = deduplicator
        self.jsonloader = jsonloader
        
    def run(self):
        extract_data = self.extractor.extract(self.input_path)
        deduplicator_obj = self.deduplicator(data=extract_data)
        transform_data = deduplicator_obj.transform()
        load_data_obj = self.jsonloader(data=transform_data, orient='records', index=False, lines=True)
        load_data_obj.load(self.output_path)
