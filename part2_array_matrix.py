class Array:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        return None

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return None