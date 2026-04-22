class Studente:

    def __init__(self, nome, cognome, eta, matricola):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.voti = []

    def presentati(self):
        print(
            f"Buongiorno! Sono {self.nome} {self.cognome}, ho {self.eta} anni e il mio numero di matricola è {self.matricola}"
        )

    def aggiungi_voto(self, voto):
        if 18 <= voto <= 30:
            self.voti.append(voto)
            print(f"Esame superato: il voto {voto} è stato registrato")
        else:
            print(f"Esame non superato: il voto {voto} non è valido")

    def calcola_media(self):
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)

    def studia(self, ore):
        print(f"Lo studente {self.nome} {self.cognome} studia per {ore} ore")


# Creazione di due oggetti studente
studente1 = Studente("Angelica", "Carrieri", 23, "20082559")
studente2 = Studente("Mario", "Rossi", 25, "20076170")

# Operazioni sullo studente1
studente1.presentati()
studente1.studia(10)
studente1.aggiungi_voto(28)
studente1.aggiungi_voto(16)
studente1.aggiungi_voto(30)
studente1.aggiungi_voto(29)

studente1.calcola_media()
print(f"La media di {studente1.nome} {studente1.cognome} è {studente1.calcola_media()}")

# Operazioni sullo studente2
studente2.presentati()
studente2.studia(7)
studente2.aggiungi_voto(20)
studente2.aggiungi_voto(18)
studente2.aggiungi_voto(22)
studente2.aggiungi_voto(24)

studente2.calcola_media()
print(f"La media di {studente2.nome} {studente2.cognome} è {studente2.calcola_media()}")
