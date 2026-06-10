# from model.cpu import Persona


# Campi in italiano per via del FE, andrebbero rimappati in inglese
class motherboard:

    def __init__(
        self, descrizione, id, nome, marca, chipset, TDP, formato, img, slot_espansione_gpu, slot_espansione_ssd, velocita_scheda
    ):
        super().__init__(id, nome, TDP, formato, img, slot_espansione_gpu, slot_espansione_ssd, velocita_scheda)
        self.marca = marca
        self.chipset = chipset
        self.img = img
        self.slot_espansione_gpu = slot_espansione_gpu
        self.slot_espansione_ssd = slot_espansione_ssd
        self.velocita_scheda = velocita_scheda
        self.descrizione = descrizione
    
    # def __str__(self):
    #     return f"COURSE: {self.id} {self.nome}"

    # def __eq__(self, other):
    #     if not isinstance(other, Course):
    #         return False

    # to_dict per la conversione che serve al metodo jsonify
    def to_dict(self):

        # base perchè è classe che eredita da Persona e quindi parte già da una base
        base = super().to_dict()
        base["id"] = self.id
        base["marca"] = self.marca
        base["chipset"] = self.chipset
        base["img"] = self.img
        base["slot_espansione_gpu"] = self.slot_espansione_gpu
        base["slot_espansione_ssd"] = self.slot_espansione_ssd
        base["velocita_scheda"] = self.velocita_scheda
        base["descrizione"] = self.descrizione
        return base
