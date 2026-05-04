#Utwórz klasę Deduplicator z metodą transform. Konstruktor klasy przyjmuje listę pól na bazie, których odbywa się deduplikacja. transform nie posiada parametrów.

class Deduplicator:
    def __init__(self, data, columns = ['Imię','Nazwisko']):
        self.data = data
        self.columns = columns

    def transform(self):
        if self.data is None:
         return None
        return self.data.drop_duplicates(subset=self.columns, keep='first') 