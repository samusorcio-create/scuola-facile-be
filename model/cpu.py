# Classe base per Student e Teacher (che ereditano)
class cpu:

    def __init__(self, id, descrizione, nome, marcha, img, core, ghz, TDP, CACHE, socket):
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.marcha = marcha
        self.img = img
        self.core = core
        self.ghz = ghz
        self.TDP = TDP
        self.CACHE = CACHE
        self.socket = socket

    def __str__(self):
        return f"{self.__class__.__name__}: {self.id} {self.nome} {self.descrizione} {self.img} {self.core} {self.ghz} {self.TDP} {self.CACHE} {self.socket}"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.id == other.id

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descrizione": self.descrizione,
            "img": self.img,
            "core": self.core,
            "ghz": self.ghz,
            "TDP": self.TDP,
            "CACHE": self.CACHE,
            "socket": self.socket,
        }
