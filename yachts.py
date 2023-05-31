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

    def zobrazit_jachty(self):
        for jachta in self.jachty:
            print(f"Jachta: {jachta.nazev}, kapacita: {jachta.kapacita}, cena: {jachta.cena}, dostupnost: {'Volná' if not jachta.rezervovana else 'Obsazená'}")

    def odstranit_nevhodne_jachty(self, kapacita, cena_max):
        nevhodne_jachty = []
        for jachta in self.jachty:
            if jachta.rezervovana or jachta.kapacita < kapacita or jachta.cena > cena_max:          # ověřuji zde ty podmínky
                nevhodne_jachty.append(jachta)                                                      # přidám do seznamu nevhodných - v zadání je jen mazání... možno vynechat, dále s nimi nepracuji
        for jachta in nevhodne_jachty:                                                               
            self.jachty.remove(jachta)                                                              # zde mažu se seznamu
        print("Nevhodné jachty byly odstraněny.")                                                   # zobrazí se i v případě nesmazání žádné, nutno přidat podmínku případně

# Vytvoření rezervačního systému
rezervacni_system = RezervacniSystem()

# Přidání jachet
rezervacni_system.pridat_jachtu(Jachta("Boat-iful Disaster", 4, 100))
rezervacni_system.pridat_jachtu(Jachta("Boatzilla", 6, 150))
rezervacni_system.pridat_jachtu(Jachta("Ship Happens", 8, 200))

# Zobrazení všech jachet
rezervacni_system.zobrazit_jachty()

# Odstranění nevhodných jachet
rezervacni_system.odstranit_nevhodne_jachty(6, 160)                  # zde 

# Zobrazení aktualizovaného seznamu jachet
rezervacni_system.zobrazit_jachty()
