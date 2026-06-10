# Corso: ha un docente e N studenti
class gpu:

    def __init__(self, id, descrizione, nome, marcha, core, memoria_VRAM, bandwhith, TDP, formato, img, MHz, tech_supportata):
        self.id = id
        self.nome = nome
        self.descrizione = descrizione
        self.marcha = marcha
        self.core = core
        self.memoria_VRAM = memoria_VRAM
        self.bandwhith = bandwhith
        self.TDP = TDP
        self.formato = formato
        self.img = img
        self.MHz = MHz
        self.tech_supportata = tech_supportata

    def __str__(self):
        return f"COURSE: {self.id} {self.nome}"

    def __eq__(self, other):
        if not isinstance(other, gpu):
            return False

        return self.id == other.id

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descrizione": self.descrizione,
            "core": self.core,
            "memoria_VRAM": self.memoria_VRAM,
            "bandwhith": self.bandwhith,
            "TDP": self.TDP,
            "formato": self.formato,
            "img": self.img,
            "MHz": self.MHz,
            "tech_supportata": self.tech_supportata,
        }
