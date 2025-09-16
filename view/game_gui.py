import textwrap
import os

# ANSI Escape Codes für Farben: \033 heißt Textfarbe
COLOR_CYAN = "\033[96m"  # Heller Cyan
COLOR_YELLOW = "\033[93m"  # Helles Gelb
COLOR_RED = "\033[91m"  # Helles Rot
COLOR_RESET = "\033[0m"  # Setzt die Farbe auf Standard zurück
COLOR_GREEN = "\033[92m"  # Helles Grün
COLOR_LIGHT = "\033[37m"
TEXT_BOLD = "\033[1m"
CONSOLE_WIDTH = 80
CONSOLE_WIDTH_HALF = (CONSOLE_WIDTH - 3) // 2


# === Menü & Anleitung ===


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def show_welcome():
    clear_console()
    generate_interaction_text(f" 🎮 Willkommen zu: {TEXT_BOLD} FACT OR FAKE {COLOR_RESET} ")
    show_rules()


def show_rules():
    print(
        f"""    
{TEXT_BOLD}Ziel:{COLOR_RESET}
Finde heraus, welche Aussage Fake ist!

{TEXT_BOLD}Spielablauf:{COLOR_RESET}
- 1–5 Spieler:innen
- Zwei Aussagen pro Runde (je 1 Fact, 1 Fake)
- Finde die Fake Aussage
- Bei falscher Antwort ist der nächste Spieler an der Reihe
- 2 Runden werden gespielt

{TEXT_BOLD}Schwierigkeit:{COLOR_RESET}
- Einfach
- Mittel
- Schwer

{TEXT_BOLD}Viel Spaß! 🧠{COLOR_RESET}
"""
    )
    input(f"{COLOR_LIGHT}Drücke [Enter], um fortzufahren...{COLOR_RESET}")


def show_round_info(round_number, max_rounds, player_name):
    clear_console()
    print("=" * CONSOLE_WIDTH)
    print(f"{COLOR_CYAN}🎯 Runde {round_number} von {max_rounds}{COLOR_RESET}".center(CONSOLE_WIDTH))
    print(f"{COLOR_GREEN}👤 Spieler: {player_name}{COLOR_RESET}".center(CONSOLE_WIDTH))
    print("=" * CONSOLE_WIDTH)
    print()


def main_menu():
    clear_console()
    generate_interaction_text(f" 📚 WIKIPEDIA {TEXT_BOLD} FACT OR FAKE {COLOR_RESET}– HAUPTMENÜ ")
    # print("\n" + "=" * CONSOLE_WIDTH)
    # print(" " * 11 + f" 📚 WIKIPEDIA {TEXT_BOLD} FACT OR FAKE {COLOR_RESET}– HAUPTMENÜ ")
    # print("=" * CONSOLE_WIDTH + "\n")
    print(f"{TEXT_BOLD} 1. {COLOR_RESET} Spiel starten")
    print(f"{TEXT_BOLD} 2. {COLOR_RESET} Anleitung anzeigen")
    print(f"{TEXT_BOLD} 3. {COLOR_RESET} Spiel beenden")

    while True:
        print()
        choice = input("Deine Wahl (1–3): ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print(f"⚠️  {COLOR_RED}   Ungültige Eingabe. Bitte 1, 2 oder 3 eingeben.{COLOR_RESET}")

    # Code Block Marie & Kristina


def get_difficulty_level():
    """
    1. Get a level of difficulty in a range of 1-3.
    2. Checks invalid input (str & float) and asks until valid input is given.
    :return: Number of difficulty levels as int
    """
    while True:
        print()
        try:
            difficulty_level = int(
                input(
                    f"Welches {TEXT_BOLD}Schwierigkeitslevel{COLOR_RESET} möchtest du spielen? Tippe die jeweilige Zahl ein.\n"
                    "Einfach 1 | Mittel 2 | Schwer 3: "
                )
            )
            if 1 <= difficulty_level <= 3:
                return difficulty_level
            else:
                print(f"⚠️ {COLOR_RED}Falsche Eingabe, bitte gebe ein Schwierigkeitslevel ein 1 - 3. {COLOR_RESET}")
        except ValueError:
            print(f"⚠️ {COLOR_RED}Falsche Eingabe, bitte gebe ein Schwierigkeitslevel ein 1 - 3. {COLOR_RESET}")


def get_number_players():
    """
    1. Gets number of players in a range of 1-5.
    2. Checks invalid input (str & float) and asks until valid input is given.
    :return: Number of players as int
    """
    while True:
        print()
        try:
            number_players = int(
                input(f"Tippe die {TEXT_BOLD}Anzahl{COLOR_RESET} der Spieler ein (1 - 5): ")
            )
            if 1 <= number_players <= 5:
                return number_players
            else:
                print(f"⚠️ {COLOR_RED}Falsche Eingabe, bitte gebe die Spieleranzahl ein 1 - 5.{COLOR_RESET}")
        except ValueError:
            print(f"⚠️ {COLOR_RED}Falsche Eingabe, bitte gebe die Spieleranzahl ein  1 - 5.{COLOR_RESET}")


def get_name_players(number_players):
    """
    1. Gets names of players according to the number of players.
    2. Check invalid input ('space' or no entry) and keep asking for valid input.
    3. Saves names in a list and initiates score as 0 points
    :return:  dict of names and scores initiated with zero points
    """
    dict_names_score = {}  # Empty dictionary initiated

    print()
    for i in range(number_players):
        while True:
            try:
                name_player = input(
                    f"Tippe den {TEXT_BOLD}Namen des {i + 1}. Spielers{COLOR_RESET} ein: "
                )
                if name_player == " " or name_player == "":
                    print(f"⚠️ {COLOR_RED}Falsche Eingabe, bitte füge einen Namen ein.{COLOR_RESET}")
                else:
                    dict_names_score[name_player] = (
                        0  # Appending empty dictionary with name and score initiated as 0 points
                    )
                    break
            except ValueError:
                print(f"⚠️ {COLOR_RED}Falsche Eingabe, bitte füge einen Namen ein.{COLOR_RESET}")

    return dict_names_score


def generate_interaction_text(text):
    # --- Header ---
    print("=" * CONSOLE_WIDTH)
    header_text = f"{text}"
    print(header_text.center(CONSOLE_WIDTH))
    print("=" * CONSOLE_WIDTH + "\n")


def announce_winner(players):
    """Announce the winner of the game and display the final rankings.

    Sorts players by their scores, displays the final ranking, and
    announces the winner with special handling for single-player games.

    Args:
        players (dict): A dictionary containing player names as keys and
        their scores as values.

    Example:
        >>> players_list = {"Player1": 10, "Player2": 5}
        >>> announce_winner(players_list)
         FINALE RANKING:
        Player1 - 10 Punkte.
        Player2 - 5 Punkte.
        🎉 🎉 🎉 Player1 HAT GEWONNEN 🎉 🎉 🎉

    Note:
        The function uses os.system("clear") to clear the console before
        displaying results.

    Returns:
        None
    """
    ranking = dict(sorted(players.items(), key=lambda item: item[1], reverse=True))
    winners = list(
        {
            name: score
            for name, score in ranking.items()
            if score >= ranking[list(ranking)[0]]
        }
    )

    if len(winners) == 1:
        print(f"{COLOR_LIGHT}In einem Single Player Spiel gibt es nur einen Gewinner...{COLOR_RESET}\n")
        generate_interaction_text(f"🎉 🎉 🎉 {TEXT_BOLD}{COLOR_GREEN}{winners[0]} HAT GEWONNEN 🎉 🎉 🎉{COLOR_RESET}")
    elif len(winners) > 1:
        winner_names = ", ".join(winners)
        generate_interaction_text(
            f"🎉 🎉 🎉 {TEXT_BOLD} DIE GEWINNER SIND: {COLOR_GREEN}{winner_names} 🎉 🎉 🎉{COLOR_RESET}")
    print()
    print(f"🏆 {TEXT_BOLD}FINALES RANKING 🏆{COLOR_RESET}")
    print(f"   {COLOR_LIGHT}--------------- {COLOR_RESET}")

    counter = 1
    for player_name, player_score in ranking.items():
        print(f"{counter}. Platz: {player_name} - {player_score} Punkte")
        counter += 1

    print()
    wait_for_enter()


def show_article_pair(question1: str, question2: str):
    """This function shows question in console
    :var question1 Text 1 for Fake-Comparison
    :var question2 Text 2 for Fake-Comparison
    """
    clear_console()
    generate_interaction_text(f"✨ {TEXT_BOLD}FACT OR FAKE ✨{COLOR_RESET}")

    # --- Body ---
    wrapped_question1 = textwrap.wrap(question1, CONSOLE_WIDTH_HALF)
    wrapped_question2 = textwrap.wrap(question2, CONSOLE_WIDTH_HALF)

    max_lines = max(len(wrapped_question1), len(wrapped_question2))
    # --- title ---

    print(
        f"{COLOR_CYAN}{'Option A'.center(CONSOLE_WIDTH_HALF)}{COLOR_RESET}"  # Geändert
        f" {COLOR_RED}|{COLOR_RESET} "
        f"{COLOR_YELLOW}{'Option B'.center(CONSOLE_WIDTH_HALF)}{COLOR_RESET}"
    )  # Geändert
    print(
        f"{COLOR_CYAN}-" * CONSOLE_WIDTH_HALF
        + f"{COLOR_RED} | "
        + f"{COLOR_YELLOW}-" * CONSOLE_WIDTH_HALF
    )

    # --- booth article/questions ---
    for i in range(max_lines):
        line1 = wrapped_question1[i] if i < len(wrapped_question1) else ""
        line2 = wrapped_question2[i] if i < len(wrapped_question2) else ""

        print(
            f"{COLOR_CYAN}{line1:<{CONSOLE_WIDTH_HALF}}{COLOR_RESET}"
            f" {COLOR_RED}|{COLOR_RESET} "
            f"{COLOR_YELLOW}{line2:<{CONSOLE_WIDTH_HALF}}{COLOR_RESET}"
        )


def get_user_choice():
    """
    This function asks user for answer (fake)
    :return: choice of user ('1' for A or '2' for B).
    """

    while True:

        choice = (
            input(
                f"\nWelche Option ist der Fake? ({COLOR_CYAN}A{COLOR_RESET} oder {COLOR_YELLOW}B{COLOR_RESET}): ").strip().upper()
        )
        if choice in ["A", "B"]:  # only A or B allowed (case-insensitive)
            if choice.upper() == "A":
                return 0
            else:
                return 1
        else:
            print(
                f"{COLOR_RED}Ungültige Eingabe. Bitte gib 'A' oder 'B' ein.{COLOR_RESET}"
            )


def wait_for_enter():
    input(f"{COLOR_LIGHT}Drücke [Enter], um fortzufahren...{COLOR_RESET}")
