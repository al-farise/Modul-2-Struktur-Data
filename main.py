class ArrayList:
    def __init__(self, value):
        self.array = value
        self.length = 0

    def __len__(self):
        return self.length

    def __getItem__(self, index):
        if index >= self.length:
            raise IndexError("Index out of range")
        return self.array[index]
    
    def __setItem__(self, index, value):
        if index >= self.length:
            raise IndexError("Index out of range")
        self.array [index] = value

    def append(self, value):
        self.array.append(value)
        self.length += 1

    def insert(self, index, value):
        if index > self. length:
            raise IndexError("Index out Of range")
        self.array.insert(index, value)
        self.length += 1

    def remove(self, value):
        self.array.remove(value)
        self.length -= 1
        return value

    def pop(self, index = -1):
        value = self.array.pop(index)
        self.length
        return value

    def index(self, value):
        return self.array. index(value)
    
    def clear(self):
        self.array.clear()
        self.length = 0
    
    def print(self):
        return self.array
    

animal = ArrayList(["Sapi", "Kelinci", "Kambing", "Unta", "Domba"])
animal_delete = []

print("Hewan:", animal.print())

animal_delete.append(animal.remove("Kelinci"))
animal_delete.append(animal.remove("Kambing"))
animal_delete.append(animal.remove("Unta"))

print("Hewan yang dihapus:", animal_delete)
print("Output hewan:", animal.print())