# from model.cpu import Persona


# Docente
class memoria_volatile:

    def __init__(self, id, nome, img, descrizione, rumorosita, compatibilita_socket, flusso_daria, size_radiatore, TDP, TDP_sopportabili):
        super().__init__(id, nome, descrizione, img, rumorosita, compatibilita_socket, flusso_daria, size_radiatore, TDP, TDP_sopportabili)
        self.rumorosita = rumorosita
        self.compatibilita_socket = compatibilita_socket
        self.flusso_daria = flusso_daria
        self.size_radiatore = size_radiatore
        self.TDP = TDP
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.img = img

    # base perchè è classe che eredita da Persona e quindi parte già da una base
    def to_dict(self):
        base = super().to_dict()
        base["rumorosita"] = self.rumorosita
        base["compatibilita_socket"] = self.compatibilita_socket
        base["flusso_daria"] = self.flusso_daria
        base["size_radiatore"] = self.size_radiatore
        base["TDP"] = self.TDP
        base["img"] = self.img
        base["descrizione"] = self.descrizione
        base["nome"] = self.nome
        base["id"] = self.id


        return base
