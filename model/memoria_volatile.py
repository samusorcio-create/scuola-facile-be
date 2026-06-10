# from model.cpu import Persona


# Docente
class memoria_volatile:

    def __init__(self, id, nome, img, marcha, descrizione, tipo, capacita, velocita, TDP):
        super().__init__(id, nome, descrizione, img, tipo, capacita, velocita, TDP)
        self.marcha = marcha
        self.tipo = tipo
        self.capacita = capacita
        self.velocita = velocita
        self.TDP = TDP
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.img = img

    # base perchè è classe che eredita da Persona e quindi parte già da una base
    def to_dict(self):
        base = super().to_dict()
        base["tipo"] = self.tipo
        base["capacita"] = self.capacita
        base["velocita"] = self.velocita
        base["TDP"] = self.TDP
        base["img"] = self.img
        base["descrizione"] = self.descrizione
        base["nome"] = self.nome
        base["id"] = self.id


        return base
