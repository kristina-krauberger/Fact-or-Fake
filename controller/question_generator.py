import wikipedia
import random
import re
from datetime import datetime

from view.game_gui import COLOR_LIGHT, COLOR_RESET

personen_dict = {
    "einfach": [
        "Angela Merkel", "Albert Einstein", "Napoleon Bonaparte", "Wolfgang Amadeus Mozart",
        "Ludwig van Beethoven", "Leonardo da Vinci", "Barack Obama", "Donald Trump",
        "Elvis Presley", "Pablo Picasso", "Vincent van Gogh",
        "Johann Wolfgang von Goethe", "Marie Curie", "Galileo Galilei", "Isaac Newton",
        "Charles Darwin", "Sigmund Freud", "Karl Marx",
        "John F. Kennedy", "Nelson Mandela", "Mahatma Gandhi"
    ],
    "mittel": [
        "Konrad Adenauer", "Willy Brandt", "Helmut Kohl", "Friedrich Schiller", "Thomas Mann",
        "Bertolt Brecht", "Franz Kafka", "Johann Sebastian Bach", "Richard Wagner", "Immanuel Kant",
        "Friedrich Nietzsche", "Max Planck", "Werner Heisenberg", "Robert Koch", "Rudolf Virchow",
        "Otto von Bismarck", "Kaiser Wilhelm II", "Friedrich der Große", "Martin Luther",
        "Johannes Gutenberg", "Carl Benz", "Werner von Braun", "Marlene Dietrich", "Romy Schneider",
        "Stefan Zweig"
    ],
    "schwer": [
        "Gustav Stresemann", "Rosa Luxemburg", "Walter Ulbricht", "Erich Honecker", "Erwin Rommel",
        "Claus von Stauffenberg", "Sophie Scholl", "Dietrich Bonhoeffer", "Carl Friedrich Gauß",
        "Gottfried Wilhelm Leibniz", "Alexander von Humboldt", "Heinrich Heine", "Theodor Fontane",
        "Arthur Schopenhauer", "Edmund Husserl", "Martin Heidegger", "Max Weber", "Georg Simmel",
        "Karl Jaspers", "Hannah Arendt", "Edith Stein", "Käthe Kollwitz", "Paula Modersohn-Becker",
        "Wilhelm Röntgen", "Emil von Behring"
    ]
}

wikipedia.set_lang("de")


def get_full_wikipedia_text(person_name):
    try:
        page = wikipedia.page(person_name, auto_suggest=False)
        return page.content
    except Exception:
        return ""


def format_occupation(text):
    text = text.replace("us-", "US-")  # Sonderfall
    ausnahmen = {"der", "die", "das", "und", "oder", "von", "zu", "mit", "für", "des", "im", "am", "an", "auf", "als",
                 "in"}
    return ' '.join([w if w in ausnahmen else w.capitalize() for w in text.split()])


def extract_facts_from_text(text):
    facts = {}

    birth = re.search(r'\* *(\d{1,2}\. *[A-Za-zäöüÄÖÜ]+ *\d{4})', text)
    birth_year = re.search(r'\*.*?(\d{4})', text)
    death = re.search(r'† *(\d{1,2}\. *[A-Za-zäöüÄÖÜ]+ *\d{4})', text)
    death_year = re.search(r'†.*?(\d{4})', text)

    if birth:
        facts['birth_date'] = birth.group(1)
    if birth_year:
        facts['birth_year'] = int(birth_year.group(1))
    if death:
        facts['death_date'] = death.group(1)
    if death_year:
        facts['death_year'] = int(death_year.group(1))
        facts['is_alive'] = False

    if 'is_alive' not in facts:
        if 'birth_year' in facts:
            facts['is_alive'] = datetime.now().year - facts['birth_year'] < 120
        else:
            facts['is_alive'] = True

    beruf = re.search(r'(?:war|ist)\s+(?:ein|eine)\s+([^,.]+)', text)
    if beruf:
        beschreibung = beruf.group(1).strip()
        if beschreibung and len(beschreibung.split()) <= 8:
            #if beschreibung.endswith('E') or beschreibung.endswith('e'):
            #    beschreibung = beschreibung[:-1].strip()
            #if beschreibung.endswith('Er') or beschreibung.endswith('er'):
            #    beschreibung = beschreibung[:-2].strip()
            facts['occupation'] = format_occupation(beschreibung)

    geburtsort = re.search(
        r'geboren\s+(?:am\s+\d{1,2}\.\s+[A-Za-zäöüÄÖÜ]+\s+\d{4}\s+)?in\s+([A-ZÄÖÜ][\wäöüß\- ]+?)[.,;\n]', text)
    if geburtsort:
        ort = geburtsort.group(1).strip()
        if len(ort.split()) <= 5:
            facts['birth_place'] = ort

    return facts


def build_fact_sentences(person, facts):
    sentences = []

    if not facts:
        return [f"{person} ist eine bekannte Persönlichkeit, aber es konnten keine weiteren Fakten extrahiert werden."]

    if 'occupation' in facts:
        verb = "ist" if facts.get('is_alive', True) else "war"
        sentences.append(f"{person} {verb} {facts['occupation']}.")

    if 'birth_date' in facts and 'birth_place' in facts:
        sentences.append(f"{person} wurde am {facts['birth_date']} in {facts['birth_place']} geboren.")
    elif 'birth_date' in facts:
        sentences.append(f"{person} wurde am {facts['birth_date']} geboren.")
    elif 'birth_year' in facts:
        sentences.append(f"{person} wurde im Jahr {facts['birth_year']} geboren.")

    if 'death_date' in facts:
        sentences.append(f"{person} starb am {facts['death_date']}.")
    elif 'death_year' in facts:
        sentences.append(f"{person} starb im Jahr {facts['death_year']}.")
    elif facts.get('is_alive'):
        sentences.append(f"{person} lebt noch.")

    return sentences


def build_false_fact_sentence(person, facts, schwierigkeit="einfach"):
    false_sentences = []

    # todo: alles auf englisch!!!

    falsche_orte = [
        "Bad Salzuflen", "Gütersloh", "Kleinmachnow", "Buxtehude", "Oer-Erkenschwick", "Plauen",
        "Schwäbisch Hall", "Eisenhüttenstadt", "Garmisch-Partenkirchen", "Saalfeld", "Duderstadt",
        "Kandahar", "Irkutsk", "Qom", "Scranton", "Truelove", "Davao", "Ulan-Ude", "Surabaya", "Stralsund"
    ]

    falsche_berufe = [
        "Fußballspieler", "Astronaut", "Koch", "Sänger", "Mathematiker", "Fitness-Trainer",
        "Pilot", "Friseur", "Programmierer", "Lehrer", "Influencer", "Youtuber", "Gärtner",
        "Tänzer", "Autoverkäufer", "Grafikdesigner", "Model", "Zauberer", "Taxifahrer"
    ]

    if 'birth_year' in facts:
        jahr = facts['birth_year'] + random.choice([-10, +10, -5, +5])
    else:
        jahr = random.randint(1700, 2000)

    ort = random.choice(falsche_orte)

    if schwierigkeit == "einfach":
        false_sentences.append(f"{person} wurde im Jahr {jahr} in {ort} geboren.")
    elif schwierigkeit == "mittel":
        if random.choice([True, False]):
            false_sentences.append(f"{person} wurde im Jahr {jahr} geboren.")
        else:
            false_sentences.append(f"{person} wurde in {ort} geboren.")
    else:
        false_sentences.append(f"{person} wurde im Jahr {jahr} geboren.")

    if 'occupation' in facts:
        falscher_beruf = random.choice([b for b in falsche_berufe if b.lower() != facts['occupation'].lower()])
        false_sentences.append(f"{person} ist {falscher_beruf}.")

    return random.choice(false_sentences)


def generate_article_pair(schwierigkeit: str = "einfach"):
    print (f"{COLOR_LIGHT}Loading game...{COLOR_RESET}")
    return_sentences = []
    person_t = random.choice(personen_dict[schwierigkeit])
    person_f = random.choice(personen_dict[schwierigkeit])
    text = get_full_wikipedia_text(person_t)
    facts = extract_facts_from_text(text)
    sentences = build_fact_sentences(person_t, facts)  # 4 Sätze - birthdate, death date, birth place,
    false_sentence = build_false_fact_sentence(person_f, facts, schwierigkeit)
    true_sentence = random.choice(sentences)
    return_sentences.append(true_sentence)
    return_sentences.append(false_sentence)
    random.shuffle(return_sentences)
    if return_sentences[0] == false_sentence:
        fake_index = 0
    else:
        fake_index = 1

    return return_sentences, fake_index

