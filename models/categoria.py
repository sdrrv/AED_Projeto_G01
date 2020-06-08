from models.tad_categoria import Categoria
from aed_ds.dictionaries.hash_table import HashTable

class Categoria(Categoria):
    def __init__(self):
        self.members = HashTable()
    
    def get_members(self):
        return self.members
    
    def add_member(self, professional):
        self.members.insert(professional.get_name(),professional)
