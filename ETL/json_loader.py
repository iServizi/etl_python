#Utwórz klasę JsonLoader z metodą load. Konstruktor przyjmuje parametry: orient, index, lines. Metoda load przyjmuje path.

class JsonLoader():
     def __init__(self, data, orient, index, lines):
        self.orient = orient
        self.index = index
        self.lines = lines
        self.data = data
    
     def load(self, path):
        return self.data.to_json(path, orient= self.orient, index=self.index, lines=self.lines, force_ascii=False)