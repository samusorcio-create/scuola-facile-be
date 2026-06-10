# from model.cpu import Persona


# Docente
class case:

    def __init__(self, id, nome, descrizione, materiali, formato, img):
        super().__init__(id, nome, descrizione, img, formato, materiali)
        self.materiali = materiali
        self.formato = formato
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.img = img

    # base perchè è classe che eredita da Persona e quindi parte già da una base
    def to_dict(self):
        base = super().to_dict()
        base["materiali"] = self.materiali
        base["formato"] = self.formato
        base["img"] = self.img
        base["descrizione"] = self.descrizione
        base["nome"] = self.nome
        base["id"] = self.id


        return base
