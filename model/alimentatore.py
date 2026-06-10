# from model.cpu import Persona


# Docente
class alimentatore:

    def __init__(self, id, nome, img, marcha, descrizione, potenza, certificazione, modularita, sistemi_di_protezione):
        super().__init__(id, nome, descrizione, img, potenza, certificazione, modularita, sistemi_di_protezione)
        self.marcha = marcha
        self.potenza = potenza
        self.certificazione = certificazione
        self.modularita = modularita
        self.sistemi_di_protezione = sistemi_di_protezione
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.img = img

    # base perchè è classe che eredita da Persona e quindi parte già da una base
    def to_dict(self):
        base = super().to_dict()
        base["potenza"] = self.potenza
        base["certificazione"] = self.certificazione
        base["modularita"] = self.modularita
        base["sistemi_di_protezione"] = self.sistemi_di_protezione
        base["img"] = self.img
        base["descrizione"] = self.descrizione
        base["nome"] = self.nome
        base["id"] = self.id


        return base
