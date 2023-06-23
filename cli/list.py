class List:
    def __init__(self, collection: list):
        self.collection = collection

    def append(self, elem):
        temp_collection = self.collection
        temp_collection.append(elem)
        return List(temp_collection)

    def get(self, i: int):
        return self.collection[i]

    def set(self, i, elem):
        temp_collection = self.collection
        temp_collection[i] = elem
        return List(temp_collection)
