## Struktura Projektu

```text
etl_python/
├── data/                   #Dane input/output
│   ├── pracownicy.csv           
│   └── output.json        
├── ETL/                    #Klasy
│   ├── __init__.py         
│   ├── extractor.py        
│   ├── duplicator.py
│   ├── json_loader.py
│   └── job.py
├── main.py                 #Main
└── README.md
