class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rivers = []
        self.grasslands = []
        self.swamps = []
        self.coastlines = []
        self.forests = []
        self.mountains = []

    def get_list(self, list):
        source_list = getattr(self, list)
        return source_list
        
