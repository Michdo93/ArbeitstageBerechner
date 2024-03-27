import datetime

class ArbeitstageBerechner:
    def __init__(self, jahr=datetime.datetime.now().year, urlaubstage=0, bundesland=None, augsburg=False, maria_himmelfahrt=False, fronleichnam=False):
        if jahr is not None and isinstance(jahr, int):
            self.jahr = jahr
        else:
            self.jahr = datetime.datetime.now().year

        self.bundesland = None

        self.buendeslaender = {
            "Baden-Württemberg": "BW",
            "Bayern": "BY",
            "Berlin": "BE",
            "Brandenburg": "BB",
            "Bremen": "HB",
            "Hamburg": "HH",
            "Hessen": "HE",
            "Mecklenburg-Vorpommern": "MV",
            "Niedersachsen": "NI",
            "Nordrhein-Westfalen": "NW",
            "Rheinland-Pfalz": "RP",
            "Saarland": "SL",
            "Sachsen": "SN",
            "Sachsen-Anhalt": "ST",
            "Schleswig-Holstein": "SH",
            "Thüringen": "TH",
        }

        if bundesland is not None:
            for land, kuerzel in self.buendeslaender.items():
                if bundesland == land:
                    self.bundesland = bundesland
                elif bundesland == kuerzel:
                    self.bundesland = land

        if self.bundesland == "Bayern" and maria_himmelfahrt:
            self.maria_himmelfahrt = True
        elif self.bundesland == "Saarland":
            self.maria_himmelfahrt = True
        else:
            self.maria_himmelfahrt = False

        if self.bundesland == "Bayern" and augsburg:
            self.augsburg = True
            self.maria_himmelfahrt = True
        else:
            self.augsburg = False

        if self.bundesland in ["Sachsen", "Thüringen"]:
            if fronleichnam == True:
                self.fronleichnam = True
            else:
                self.fronleichnam = False
        elif self.bundesland in ["Baden-Württemberg", "Bayern", "Hessen", "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland"]:
            self.fronleichnam = True
        else:
            self.fronleichnam = False

        self.feiertage = {
            "Neujahr": datetime.date(self.jahr, 1, 1),
            "Karfreitag": self.__berechne_karfreitag(),
            "Ostermontag": self.__berechne_ostermontag(),
            "Tag der Arbeit": datetime.date(self.jahr, 5, 1),
            "Christi Himmelfahrt": self.__berechne_christi_himmelfahrt(),
            "Pfingstmontag": self.__berechne_pfingstmontag(),
            "Tag der Deutschen Einheit": datetime.date(self.jahr, 10, 3),
            "1. Weihnachtstag": datetime.date(self.jahr, 12, 25),
            "2. Weihnachtstag": datetime.date(self.jahr, 12, 26),
        } # 9 gemeinsame Feiertage

        if self.bundesland is not None:
            if self.bundesland == "Baden-Württemberg":
                self.feiertage["Heilige Drei Könige"] = datetime.date(self.jahr, 1, 6)

                if self.fronleichnam:
                    self.feiertage["Fronleichnam"] = self.__berechne_fronleichnam()

                self.feiertage["Allerheiligen"] = datetime.date(self.jahr, 11, 1)
            elif self.bundesland == "Bayern":
                self.feiertage["Heilige Drei Könige"] = datetime.date(self.jahr, 1, 6)
                
                if self.fronleichnam:
                    self.feiertage["Fronleichnam"] = self.__berechne_fronleichnam()

                self.feiertage["Allerheiligen"] = datetime.date(self.jahr, 11, 1)

                if self.maria_himmelfahrt:
                    self.feiertage["Mariä Himmelfahrt"] = datetime.date(self.jahr, 8, 15)

                if self.augsburg:
                    self.feiertage["Augsburger Friedensfest"] = datetime.date(self.jahr, 8, 8)
            elif self.bundesland == "Berlin":
                self.feiertage["Internationaler Frauentag"] = datetime.date(self.jahr, 3, 8)
            elif self.bundesland == "Brandenburg":
                self.feiertage["Pfingstsonntag"] = self.__berechne_pfingstsonntag()
                self.feiertage["Reformationstag"] = datetime.date(self.jahr, 10, 31)
            elif self.bundesland == "Bremen":
                self.feiertage["Reformationstag"] = datetime.date(self.jahr, 10, 31)
            elif self.bundesland == "Hamburg":
                self.feiertage["Reformationstag"] = datetime.date(self.jahr, 10, 31)
            elif self.bundesland == "Hessen":
                if self.fronleichnam:
                    self.feiertage["Fronleichnam"] = self.__berechne_fronleichnam()
            elif self.bundesland == "Mecklenburg-Vorpommern":
                self.feiertage["Internationaler Frauentag"] = datetime.date(self.jahr, 3, 8)
                self.feiertage["Reformationstag"] = datetime.date(self.jahr, 10, 31)
            elif self.bundesland == "Niedersachsen":
                self.feiertage["Reformationstag"] = datetime.date(self.jahr, 10, 31)
            elif self.bundesland == "Nordrhein-Westfalen":
                if self.fronleichnam:
                    self.feiertage["Fronleichnam"] = self.__berechne_fronleichnam()

                self.feiertage["Allerheiligen"] = datetime.date(self.jahr, 11, 1)
            elif self.bundesland == "Rheinland-Pfalz":
                if self.fronleichnam:
                    self.feiertage["Fronleichnam"] = self.__berechne_fronleichnam()

                self.feiertage["Allerheiligen"] = datetime.date(self.jahr, 11, 1)
            elif self.bundesland == "Saarland":
                if self.fronleichnam:
                    self.feiertage["Fronleichnam"] = self.__berechne_fronleichnam()

                self.feiertage["Allerheiligen"] = datetime.date(self.jahr, 11, 1)

                if self.maria_himmelfahrt:
                    self.feiertage["Mariä Himmelfahrt"] = datetime.date(self.jahr, 8, 15)
            elif self.bundesland == "Sachsen":
                if self.fronleichnam:
                    self.feiertage["Fronleichnam"] = self.__berechne_fronleichnam()

                self.feiertage["Reformationstag"] = datetime.date(self.jahr, 10, 31)
                self.feiertage["Buß- und Bettag"] = self.__berechne_buss_und_bettag()
            elif self.bundesland == "Sachsen-Anhalt":
                self.feiertage["Heilige Drei Könige"] = datetime.date(self.jahr, 1, 6)
                self.feiertage["Reformationstag"] = datetime.date(self.jahr, 10, 31)
            elif self.bundesland == "Schleswig-Holstein":
                self.feiertage["Reformationstag"] = datetime.date(self.jahr, 10, 31)
            elif self.bundesland == "Thüringen":
                if self.fronleichnam:
                    self.feiertage["Fronleichnam"] = self.__berechne_fronleichnam()
                
                self.feiertage["Weltkindertag"] = datetime.date(self.jahr, 9, 20)
                self.feiertage["Reformationstag"] = datetime.date(self.jahr, 10, 31)

        if isinstance(urlaubstage, int):
            self.urlaubstage = urlaubstage
        else:
            self.urlaubstage = 30

    def __berechne_ostersonntag(self):
        # Berechne das Osterdatum für das gegebene Jahr
        a = self.jahr % 19
        b = self.jahr // 100
        c = self.jahr % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        monat = (h + l - 7 * m + 114) // 31
        tag = ((h + l - 7 * m + 114) % 31) + 1

        # Das Osterdatum ist tag. monat.
        ostersonntag = datetime.date(self.jahr, monat, tag)
        return ostersonntag

    def __berechne_karfreitag(self):
        # Berechne den Ostersonntag für das gegebene Jahr
        ostersonntag = self.__berechne_ostersonntag()

        # Karfreitag ist zwei Tage vor dem Ostersonntag
        karfreitag = ostersonntag - datetime.timedelta(days=2)
        return karfreitag

    def __berechne_ostermontag(self):
        # Berechne den Ostersonntag für das gegebene Jahr
        ostersonntag = self.__berechne_ostersonntag()

        # Ostermontag ist einen Tag nach dem Ostersonntag
        ostermontag = ostersonntag + datetime.timedelta(days=1)
        return ostermontag

    def __berechne_pfingstsonntag(self):
        # Berechne Ostersonntag für das gegebene Jahr
        ostersonntag = self.__berechne_ostersonntag()

        # Pfingstsonntag ist 49 Tage nach Ostersonntag
        pfingstsonntag = ostersonntag + datetime.timedelta(days=49)
        return pfingstsonntag

    def __berechne_pfingstmontag(self):
        # Berechne Pfingstsonntag für das gegebene Jahr
        pfingstsonntag = self.__berechne_pfingstsonntag()

        # Pfingstmontag ist einen Tag nach Pfingstsonntag
        pfingstmontag = pfingstsonntag + datetime.timedelta(days=1)
        return pfingstmontag

    def __berechne_christi_himmelfahrt(self):
        # Berechne Ostersonntag für das gegebene Jahr
        ostersonntag = self.__berechne_ostersonntag()

        # Christi Himmelfahrt ist 39 Tage nach Ostersonntag
        christi_himmelfahrt = ostersonntag + datetime.timedelta(days=39)
        return christi_himmelfahrt
    
    def __berechne_buss_und_bettag(self):
        # Buß- und Bettag ist der Mittwoch vor dem 23. November
        start_datum = datetime.date(self.jahr, 11, 23)
        # Finde den Mittwoch vor dem 23. November
        while start_datum.weekday() != 2:  # 2 steht für Mittwoch (Montag = 0, Dienstag = 1, ..., Sonntag = 6)
            start_datum -= datetime.timedelta(days=1)
        return start_datum

    def __berechne_fronleichnam(self):
        # Fronleichnam ist 60 Tage nach Ostersonntag
        ostersonntag = self.__berechne_ostersonntag()
        fronleichnam = ostersonntag + datetime.timedelta(days=60)
        return fronleichnam

    def ist_arbeitstag(self, datum):
        wochentag = datum.weekday()

        if wochentag >= 5:  # Samstag (5) oder Sonntag (6)
            return False
        
        for feiertag in self.feiertage.values():
            if datum == feiertag:
                return False

        return True

    def berechne_arbeitstage(self, start_tag=1, start_monat=1, end_tag=31, end_monat=12):
        start_datum = datetime.date(self.jahr, start_monat, start_tag)
        end_datum = datetime.date(self.jahr, end_monat, end_tag)

        aktuelles_datum = start_datum
        arbeitstage = 0
        while aktuelles_datum <= end_datum:
            if self.ist_arbeitstag(aktuelles_datum):
                arbeitstage += 1
            aktuelles_datum += datetime.timedelta(days=1)

        return arbeitstage-self.urlaubstage

if __name__ == "__main__":
    berechner = ArbeitstageBerechner()
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Baden-Württemberg")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Baden-Würrtemberg:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Bayern")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Bayern:", arbeitstage)
    
    berechner = ArbeitstageBerechner(bundesland="Berlin")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Berlin:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Brandenburg")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Brandenburg:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Bremen")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Bremen:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Hamburg")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Hamburg:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Hessen")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Hessen:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Mecklenburg-Vorpommern")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Mecklenburg-Vorpommern:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Niedersachsen")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Niedersachsen:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Nordrhein-Westfalen")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Nordrhein-Westfalen:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Rheinland-Pfalz")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Rheinland-Pfalz:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Saarland")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Saarland:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Sachsen")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Sachsen:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Sachsen-Anhalt")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Sachsen-Anhalt:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Schleswig-Holstein")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Schleswig-Holstein:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Thüringen")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Thüringen:", arbeitstage)
