# A basic struct implementation

class Struct(dict):
    def __getattr__(self, key):
        if key in self.keys():
            return self[key]
        else:
            return None

    def __setattr__(self, key, value):
        self[key] = value
