class Jachta:
    def __init__(self, nazev, kapacita, cena):
        self.nazev = nazev
        self.kapacita = kapacita
        self.cena = cena
        self.rezervovana = False

class RezervacniSystem:
    def __init__(self):
        self.jachty = []

    def pridat_jachtu(self, jachta):
        self.jachty.append(jachta)

    def vyhledat_jachty(self, kapacita, cena_max):
        volne_jachty = []
        for jachta in self.jachty:
            if not jachta.rezervovana and jachta.kapacita >= kapacita and jachta.cena <= cena_max:
                volne_jachty.append(jachta)
        return volne_jachty

    def rezervovat_jachtu(self, jachta):
        if not jachta.rezervovana:
            jachta.rezervovana = True
            print(f"Jachta {jachta.nazev} byla úspěšně rezervována.")
        else:
            print("Omlouváme se, ale tato jachta je již rezervována.")

# Vytvoření rezervačního systému
rezervacni_system = RezervacniSystem()

# Přidání jachet
rezervacni_system.pridat_jachtu(Jachta("Jachta 1", 4, 100))
rezervacni_system.pridat_jachtu(Jachta("Jachta 2", 6, 150))
rezervacni_system.pridat_jachtu(Jachta("Jachta 3", 8, 200))

# Vyhledání dostupných jachet
volne_jachty = rezervacni_system.vyhledat_jachty(6, 160)
for jachta in volne_jachty:
    print(f"Dostupná jachta: {jachta.nazev}, kapacita: {jachta.kapacita}, cena: {jachta.cena}")

# Rezervace jachty
jachta = volne_jachty[0]
rezervacni_system.rezervovat_jachtu(jachta)
