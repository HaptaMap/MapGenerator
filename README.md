# MapGenerator
 
Haptische Karten aus dem 3D-Drucker

# Was ist das? / What is this?

Für blinde oder sehbehinderte Menschen ist es sehr schwierig, sich
selbstständig in einer unbekannten Umgebung zurechtzufinden, beispielsweise 
nach einem Umzug, auf Geschäftsreisen oder im Urlaub. Unsere automatisch aus
OpenStreetMaps generierten, 3D-gedruckten Landkarten ermöglichen es, sich
eine beliebige Umgebung tastend zu erschließen.

Unsere Karten...

* können verschiedene Objekttypen (Straßen, 
Orientierungshilfen/Querungshilfen/Leitlinien, Gebäude, Wasserwege etc) in
der von Nutzer\*innen gewünschten Höhe darstellen
* erlauben das Markieren bestimmter für Nutzer\*innen wichtiger Punkte
* können im Multi-Farb-Druck gedruckt werden (um beispielsweise durch hohen
Kontrast Informationen darzustellen)

---

For blind or visually-impaired people, traveling independently to new locations 
(for example, after a move, for work, or on vacation) is very challenging.
This project generates 3D-printable tactile maps based on OpenStreetMap data.

Our maps:
 
* Include different object types (such as streets, tactile/orientation 
features, buildings, waterways, etc) at various heights, as desired by the
user
* Allow users to mark important points or points of interest
* Can be printed in multiple colors (for example, in high contrast for
visually-impaired users)

![Einfarbig schwarze 3D-gedruckte Karte der Innenstadt von Stuttgart-Vaihingen auf dem Druckerbett eines Prusa-MK3S-Druckers. Die Karte ist annährend quadratisch und zeigt Straßen, Gebäude
und Querungshilfen in jeweils unterschiedlicher Höhe. A single-color black 3D-printed map of Vaihingen Center, Stuttgart on the bed of a Prusa MK3S printer. The map is rectangular and shows streets, buildings, and tactile features, each in its assigned height.](https://github.com/HaptaMap/MapGenerator/blob/main/images/VaihingenMitteMap.jpg)
![Einfarbig multifarbe 3D-gedruckte Karte der Innenstadt von Stuttgart-Vaihingen in die hande eines Benutzers. Die Karte ist annährend quadratisch und zeigt Straßen (schwartz), Gebäude (rosa)
und Querungshilfen (weiß) in jeweils unterschiedlicher Höhe. A multicolor 3D-printed map of Vaihingen Center, Stuttgart in a user's hands. The map is rectangular and shows streets, buildings, and tactile features, each in its assigned height.](https://github.com/HaptaMap/MapGenerator/blob/main/images/VaihingenMitteMapMulticolor.jpg)

# Wie installere ich es? / How do I install this?

(ausführliche Anleitung ist in Arbeit)

1. Installiere [OpenSCAD](https://openscad.org/downloads.html) 
2. Lade dir das Repository herunter.
3. Installiere die Python-dependencies

```shell
$ pip install -r requirements.txt
```

---

(Directions are still in progress...)

1. Install [OpenSCAD](https://openscad.org/downloads.html)
2. Download the repository
3. Install the python dependencies:

```shell
$ pip install -r requirements.txt
```

# Wie benutze ich es? / How do I use this?

(ausführliche Anleitung ist in Arbeit)

---

(Directions are still in progress...)

# Was kommt als nächstes? / What comes next?

Die nächste Version der Landkarte wird über eine Sprachausgabe zusätzliche 
Informationen wie Haltestellen- und Straßennamen zur Verfügung stellen. Dazu
verarbeiten wir leitfähiges Filament im Druck so, dass eine Berührung
bestimmter Punkte Signale an einen Microcontroller sendet, der dann wiederum
akustisch die gewünschten Informationen zur Verfügung stellt.

---

The next version of the maps will speak information on public transit stops,
street names, and other important locations. We are working on integrating
conductive filament so that touching points signals a microcontroller, which
then speaks the relevent information.