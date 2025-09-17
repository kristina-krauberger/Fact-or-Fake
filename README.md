Fact or Fake Wiki-Game - Ergebnis eines Hackathons
Ein textbasiertes Spiel, bei dem Spieler zwischen echten und gefälschten Wikipedia-Artikeln unterscheiden müssen. Teste dein Wissen und deine Fähigkeit, Fake-News zu erkennen!

Spielbeschreibung
Das "Fact or Fake" Wiki-Game ist ein unterhaltsames Bildungsspiel, bei dem Spieler ihre Faktenprüfungs-Fähigkeiten unter Beweis stellen müssen. In jeder Runde werden zwei Aussagen präsentiert - eine ist wahr (Fact), die andere ist falsch (Fake). Die Spieler müssen erraten, welche Aussage gefälscht ist.

Features
Mehrspieler-Modus: Bis zu 5 Spieler können gegeneinander antreten
Drei Schwierigkeitsstufen: Einfach, Mittel und Schwer
Echtzeit-Wikipedia-Daten: Alle Fakten stammen aus echten Wikipedia-Artikeln
Farbiges Konsolen-Interface: Ansprechende visuelle Darstellung
Punktesystem: Verfolge deinen Fortschritt und vergleiche dich mit anderen Spielern

Voraussetzungen
Python 3.6 oder höher
Installierte Python-Pakete:
wikipedia
beautifulsoup4
requests

Installation

Repository klonen:

git clone https://github.com/dein-username/fact-or-fake-wiki-game.git 
cd fact-or-fake-wiki-game
Virtuelle Umgebung erstellen (optional aber empfohlen):
bash

python -m venv venv
source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows

Abhängigkeiten installieren:
pip install wikipedia beautifulsoup4 requests

Spiel starten
python main.py

Spielregeln
Spieleranzahl: 1-5 Spieler
Spielablauf:
Jede Runde werden zwei Aussagen präsentiert
Eine Aussage ist wahr (Fact), eine ist falsch (Fake)
Spieler müssen die gefälschte Aussage identifizieren
Bei richtiger Antwort gibt es einen Punkt
Bei falscher Antwort ist der nächste Spieler an der Reihe

Schwierigkeitsstufen:
Einfach: Bekannte Persönlichkeiten
Mittel: Historische und kulturelle Persönlichkeiten
Schwer: Spezialisierte historische Figuren

Spielende: Nach 2 Runden wird der Gewinner ermittelt

Projektstruktur

fact-or-fake-wiki-game/

│

├── main.py # Hauptprogramm und Spiellogik

├── controller/

│ └── question_generator.py # Generierung von Fragen und Artikel-Paaren

├── view/

│ └── game_gui.py # Benutzeroberfläche und Konsolen-Anzeige

└── README.md # Diese Datei





