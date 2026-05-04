#Utwórz plik main.py, który tworzy instancję Job i uruchamia metodę run.
from ETL.job import Job
from ETL.csv_extractor import CsvExtractor
from ETL.duplicator import Deduplicator
from ETL.json_loader import JsonLoader
from ETL.job import Job


def main():
    extractor = CsvExtractor()

    etl_job = Job(input_path="data/pracownicy.csv", output_path="data/output.json", extractor=extractor, deduplicator=Deduplicator, jsonloader=JsonLoader)
    etl_job.run()

if __name__ == "__main__":
    main()