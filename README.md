# ArbeitstageBerechner
Ein Python-Skript, welches die Anzahl der Arbeitstage in einem gegebenen Zeitraum berechnet.

Im nachfolgenden wird das Wort Feiertag für gesetzliche Feiertage verwendet. An diesen ist selbstveständlich kein Arbeitstag. Diese Feiertage variieren je nach Bundesland, aber auch nach einzelnen Gemeinden innerhalb von Bundesländern.

- Standardmäßig würde die Berechnung den `01.01.` bis zum `31.12.` des aktuellen Jahrs berechnen. Man kann aber sowohl das Jahr, als auch den Zeitraum innerhalb dieses Jahres beliebig ändern.
- Gibt man kein Bundesland an, werden alle gemeinsamen Feiertage abgezogen. Ansonsten hat man die Möglichkeiten entsprechende Parameter für das Bundesland anzugeben.
- In Bayern hat Augsburg zum Beispiel mehr Feiertage, man kann also einen Parameter angeben, ob man die Arbeitstage aus Augsburg will.
- In Bayern und im Saarland gibt es in streng katholischen Gemeinden den zusätzlichen Feiertag Mariä Himmelfahrt. Auch dies lässt sich per Parameter angeben.
- In Baden-Württemberg, Bayern, Hessen, Nordrhein-Westfalen, Rheinland-Pfalz und Saarland ist Fronleichnam automatisch auch ein Feiertag. In Sachsen und in Thüringen nur in manchen Gemeinden. In den restlichen Bundesländern ist Fronleichnam kein Feiertag.
- Standardmäßig sind die Urlaubstage auch `0`. Dies heißt, dass man von dem jeweiligen Bundesland (oder auch von Deutschland) alle Arbeitstage erhält. Dieser Parameter lässt sich jedoch anpassen.

## Wozu kann das Programm verwendet werden?

Das Programm kann verwendet werden, um

- in einem Zeitraum alle Arbeitstage zu bestimmen.
- die Arbeitstage verschiedener Bundesländer zu vergleichen.
- die Feiertage eines Bundeslands sich anzeigen zu lassen.
- die Arbeitstage abzüglich der Urlaubstage zu bestimmen.
- z.B. für die Steuererklärung zu berechnen, wie viele Arbeitstage man hatte.
- z.B. zum Berechnen wie viel man in einem Monat gearbeitet hat, falls es Unstimmigkeiten beim Arbeitszeitnachweis geben sollte.
- z.B. in einem erweiterten Use-Case zu berechnen, wie viele Fahrkilometer man zum Arbeitgeber hat unter der Voraussetzung, dass der Arbeitsweg immer gleich ist. Weiß man, wie viele Tage man arbeiten war und wie viele Kilometer die Strecke zum Arbeitgeber hat, kann man dies einfach multiplizieren. Nimmt man nun ein Mittelwert, was man an Benzin bzw. Diesel verbraucht hat und einen Mittelwert für den Benzin- bzw. Dieselpreis, kann man auch ermitteln, wie hoch die Tankkosten waren. Diese Summe könnte man zum Beispiel mit dem, was die Steuererklärung für die Fahrkostenpauschale beanschlagt vergleichen (wer längere Strecken zum Arbeitgeber pendelt, der wird merken, dass er weniger erstattet bekommt, als er tankt und wer kürzere Strecken vielleicht auch mit einem niedrigeren Verbrauch fährt, der macht hingegen Gewinn).

## Verwendung

Du kannst das Programm wie folgt ausführen:

```
python arbeitstage_berechner.py
```

## Individuelle Anpassungen:

Dies ist das Standard-Beispiel, um für jedes Bundesland und für Deutschland die Arbeitstage zu ermitteln:

```
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
```

Im Jahr 2024 ergibt sich damit:

```
Arbeitstage: 253
Arbeitstage Baden-Würrtemberg: 251
Arbeitstage Bayern: 251
Arbeitstage Berlin: 252
Arbeitstage Brandenburg: 252
Arbeitstage Bremen: 252
Arbeitstage Hamburg: 252
Arbeitstage Hessen: 252
Arbeitstage Mecklenburg-Vorpommern: 251
Arbeitstage Niedersachsen: 252
Arbeitstage Nordrhein-Westfalen: 251
Arbeitstage Rheinland-Pfalz: 251
Arbeitstage Saarland: 250
Arbeitstage Sachsen: 251
Arbeitstage Sachsen-Anhalt: 252
Arbeitstage Schleswig-Holstein: 252
Arbeitstage Thüringen: 251
```

Alle Bundesländer haben 9 gemeinsame Feiertage! Jedoch variiert dies je nach Bundesland und Gemeinde.

Für jedes Bundesland und für jedes Jahr müssen einzelne Objektinstanzen initiiert werden!

### Anpassen des Jahres:

Zum Beispiel für das Jahr `2025`:

```
if __name__ == "__main__":
    berechner = ArbeitstageBerechner(jahr=2025)
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage:", arbeitstage)
```

Im Konstruktor muss die Jahreszahl geändert werden. Wenn kein Parameter angegeben ist, wird die aktuelle Jahreszahl verwendet. Der Standardparameter ist:

```
jahr=datetime.datetime.now().year,
```

Dies bedeutet, dass vom aktuellen System wo das Python-Skript ausgeführt wird, die Jahreszahl generiert wird.

Die Jahreszahl muss im Konstruktor angelegt sein, weil sonst die Berechnung von Feiertagen wie Ostern nicht möglich ist. Dies verschiebt sich jährlich. Entsprechend gibt es noch Feiertage in Abhängigkeit zu Ostern, die sich ebenfalls verschieben. Der Buß- und Bettag ist immer der Mittwoch vor dem 23. November und ist nur in Sachsen ein gesetztlicher Feiertag. Auch hierfür wird eine Jahreszahl benötigt, um das genaue Datum zu ermitteln.

### Anpassen des Zeitraums innerhalb des Jahres:

Zum Beispiel vom `01. März` bis zum `31. März`:

```
if __name__ == "__main__":
    berechner = ArbeitstageBerechner(jahr=2025)
    arbeitstage = berechner.berechne_arbeitstage(1, 3, 31, 3)
    print("Arbeitstage:", arbeitstage)
```

Wie man sieht, muss hier in der `berechne_arbeitstage`-Methode der Zeitraum innerhalb des Jahres gesetzt werden.

Oder auch:

```
if __name__ == "__main__":
    berechner = ArbeitstageBerechner(jahr=2025)
    arbeitstage = berechner.berechne_arbeitstage(start_tag=1, start_monat=3, end_tag=31, end_monat=3)
    print("Arbeitstage:", arbeitstage)
```

Sollte kein Parameter gesetzt werden, wird automatisch der `01.01` bis zum `31.12.` genommen. Die Standardparameter lauten:

```
start_tag=1, start_monat=1, end_tag=31, end_monat=12
```

### Anpassen des Bundeslandes:

Im Standardbeispiele sieht man bereits, dass mit `bundesland=<Dein Bundesland>` dann im Konstruktor das Bundesland gewählt werden kann.

```
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
```

Anstelle von `"Baden-Württemberg"` oder `"Bayern"` kann man auch die bundeslandüblichen Kürzel `"BW"` und `"BY"` verwenden. Dies gilt auch für alle anderen Bundesländer.

### Abfrage des Bundeslandes

Du kannst z.B. folgendes machen, um abzufragen, welches Bundesland in der Objektinstanz hinterlegt ist:

```
if __name__ == "__main__":
    berechner = ArbeitstageBerechner(bundesland="Baden-Württemberg")
    print("Bundesland:", berechner.bundesland)

    berechner = ArbeitstageBerechner(bundesland="BW")
    print("Bundesland:", berechner.bundesland)
```

Du erhältst:

```
Bundesland: Baden-Württemberg
Bundesland: Baden-Württemberg
```

Also ein Kürzel gibt immer am Ende auch den ganzen Namen des Bundeslands zurück.

### Abfrage der Feiertage (eines Bundeslands):

Du kannst z.B. folgendes machen, um abzufragen, welche Feiertage in der Objektinstanz hinterlegt ist:

```
if __name__ == "__main__":
    berechner = ArbeitstageBerechner(bundesland="Baden-Württemberg")
    print("Feiertage Baden-Württemberg:", berechner.feiertage)
```

Man erhält:

```
Feiertage Baden-Württemberg: {'Neujahr': datetime.date(2024, 1, 1), 'Karfreitag': datetime.date(2024, 3, 29), 'Ostermontag': datetime.date(2024, 4, 1), 'Tag der Arbeit': datetime.date(2024, 5, 1), 'Christi Himmelfahrt': datetime.date(2024, 5, 9), 'Pfingstmontag': datetime.date(2024, 5, 20), 'Tag der Deutschen Einheit': datetime.date(2024, 10, 3), '1. Weihnachtstag': datetime.date(2024, 12, 25), '2. Weihnachtstag': datetime.date(2024, 12, 26), 'Heilige Drei Könige': datetime.date(2024, 1, 6), 'Fronleichnam': datetime.date(2024, 5, 30), 'Allerheiligen': datetime.date(2024, 11, 1)}
```

Wenn man alle gemeinsamen Feiertage will, dann lässt man die Angabe eines Bundeslands einfach weg:

```
if __name__ == "__main__":
    berechner = ArbeitstageBerechner()
    print("Feiertage:", berechner.feiertage)
```

Man erhält:

```
Feiertage: {'Neujahr': datetime.date(2024, 1, 1), 'Karfreitag': datetime.date(2024, 3, 29), 'Ostermontag': datetime.date(2024, 4, 1), 'Tag der Arbeit': datetime.date(2024, 5, 1), 'Christi Himmelfahrt': datetime.date(2024, 5, 9), 'Pfingstmontag': datetime.date(2024, 5, 20), 'Tag der Deutschen Einheit': datetime.date(2024, 10, 3), '1. Weihnachtstag': datetime.date(2024, 12, 25), '2. Weihnachtstag': datetime.date(2024, 12, 26)}
```

### Abfrage alle Bundesländer und derer Kürzel:

Du kannst z.B. folgendes machen, um alle Bundesländer inkl. ihrer Kürzel abzufragen:

```
if __name__ == "__main__":
    berechner = ArbeitstageBerechner()
    print("Bundesländer:", berechner.bundeslaender)
```

Man erhält:

```
Bundesländer: {'Baden-Württemberg': 'BW', 'Bayern': 'BY', 'Berlin': 'BE', 'Brandenburg': 'BB', 'Bremen': 'HB', 'Hamburg': 'HH', 'Hessen': 'HE', 'Mecklenburg-Vorpommern': 'MV', 'Niedersachsen': 'NI', 'Nordrhein-Westfalen': 'NW', 'Rheinland-Pfalz': 'RP', 'Saarland': 'SL', 'Sachsen': 'SN', 'Sachsen-Anhalt': 'ST', 'Schleswig-Holstein': 'SH', 'Thüringen': 'TH'}
```

### Weitere Parameter am Beispiel Bayern:

Es gibt folgende Standardparameter:

```
augsburg=False, maria_himmelfahrt=False, fronleichnam=False
```

In Bayern kann man all diese setzen:

```
if __name__ == "__main__":
    berechner = ArbeitstageBerechner(bundesland="Bayern")
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Bayern:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Bayern", augsburg=True)
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Bayern:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Bayern", augsburg=True, maria_himmelfahrt=True)
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Bayern:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Bayern", augsburg=True, maria_himmelfahrt=True, fronleichnam=True)
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Bayern:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Bayern", augsburg=False)
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Bayern:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Bayern", augsburg=False, maria_himmelfahrt=True)
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Bayern:", arbeitstage)

    berechner = ArbeitstageBerechner(bundesland="Bayern", augsburg=False, maria_himmelfahrt=True, fronleichnam=True)
    arbeitstage = berechner.berechne_arbeitstage()
    print("Arbeitstage Bayern:", arbeitstage)
```

Man erhält:

```
Arbeitstage Bayern: 251
Arbeitstage Bayern: 249
Arbeitstage Bayern: 249
Arbeitstage Bayern: 249
Arbeitstage Bayern: 251
Arbeitstage Bayern: 250
Arbeitstage Bayern: 250
```

Nicht nur in Bayern ist quasi drinnen, dass wenn diese Parameter entsprechend gesetzt werden, dass da nichts fälschlicherweise als Feiertag angsehen wird oder übersehen wird. In Augsburg ist nicht nur das Augsburger Friedensfest ein fester gesetzlicher Feiertag, sondern auch Fronleichnam. Würde ich den Parameter `fronleichnam` nicht auf `True` setzen, wird zwar zunächst der Standardparameter `fronleichnam=False` verwendet. Aber weil ja `augsburg=True` ist, wird dann `fronleichnam` auch `True`. Der Parameter `augsburg` wird von allen Bundesländern außer von Bayern ignoriert. In Bundesländern wie Baden-Württemberg usw. (oben bereits erläutert), ist Fronleichnam ebenfalls ein Feiertag, sodass hier ebenfalls der Parameter auf `True` gesetzt wird.

Ach, um es abzukürzen, der Konstruktor ist so geschrieben, dass kein Feiertag je nach Bundesland übersehen werden kann. Nur in manchen Bundesländern müssen zusätzliche Parameter zu Mariä Himmelfahrt und Fronleichnam gesetzt werden. Diese werden aber nur in den Bundesländern berücksichtigt, in denen diese optional wirklich je nach Gemeinde Feiertage sein können!
