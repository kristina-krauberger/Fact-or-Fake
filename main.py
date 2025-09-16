"""Fact or Fake wiki-game.

A text-based game where players identify fake articles from a pair of
Wikipedia articles. One real, one fake.

The game flow is managed through a main menu system that allows players
to choose:
    - Start a new game
    - View rules
    - Exit the program

Functions:
    announce_winner(players): Displays final rankings and declares the winner
    game_loop(players): Manages the main game mechanics and scoring
    main(): Entry point, handles a menu system and game initialization

Dependencies:
    - sys: For program exit
    - view.game_gui: For user interface elements
    - controller.question_generator: For article pair generation

    To run the game (depending on your environment):
        $ python main.py
    or:
        $ python3 main.py
"""

import sys
import view.game_gui as gui
from controller.question_generator import generate_article_pair


def game_loop(players, difficulty):
    """

    This function Manage the game loop for the Fact or Fake game.

    Controls the flow of the game, handling multiple rounds and players.
    Generates article pairs, presents them to the players, processes
    their answers, and keeps track of scores.

    Args:
        players (dict): A dictionary with player names as keys and their scores
        as values.
        difficulty (str): Difficulty level.

    Returns:
        None

    Notes:
        - The game runs for a fixed number of rounds (max_rounds)
        - Each player gets a fixed number of attempts per round
            (max_rounds_per_player)
        - Players score points for correctly identifying fake articles
        - If a player makes a mistake it's the other players turn
        - The game ends when all rounds are completed
    """
    max_rounds = 2
    max_rounds_per_player = 2
    article_pair_counter = 0
    article_pairs = []
    article_pairs_needed = max_rounds * max_rounds_per_player * len(players)

    for _ in range(article_pairs_needed):
        articles, fake_article_index = generate_article_pair(difficulty)
        article_pair = {
            "answer": fake_article_index,
            "text1": articles[0],
            "text2": articles[1],
        }
        article_pairs.append(article_pair)

    for game_round in range(max_rounds):
        game_round += 1
        for player_name in players:
            print()
            gui.show_round_info(game_round, max_rounds, player_name)
            gui.wait_for_enter()

            for _ in range(max_rounds_per_player):
                article_pair = article_pairs[article_pair_counter]
                # print(article_pair)

                gui.show_article_pair(
                    article_pair["text1"],
                    article_pair["text2"],
                )

                print()
                answer = gui.get_user_choice()

                if answer == article_pair["answer"]:
                    players[player_name] += 1  # 1 point more
                    article_pair_counter += 1  # next pair
                    print()
                    gui.generate_interaction_text(f"\033[92mRichtige Antwort!\033[0m Weiter geht's!")
                    print()
                    gui.wait_for_enter()
                    continue

                gui.generate_interaction_text(
                    f"\033[91mFalsche Antwort!\033[0m Der nächste Spieler ist an der Reihe.")
                print()
                gui.wait_for_enter()
                article_pair_counter += 1
                break
    gui.clear_console()
   #  gui.generate_interaction_text(f" 📚 WIKIPEDIA {TEXT_BOLD} FACT OR FAKE {COLOR_RESET}– SPIELENDE ")
   # gui.generate_interaction_text()
    gui.announce_winner(players)


def main():
    gui.show_welcome()

    while True:
        player_choice = gui.main_menu()

        if player_choice == "1":
            number_players = gui.get_number_players()
            players = gui.get_name_players(number_players)
            difficulty = gui.get_difficulty_level()

            if difficulty == 1:
                difficulty = "einfach"
            elif difficulty == 2:
                difficulty = "mittel"
            elif difficulty == 3:
                difficulty = "schwer"

            #  print(difficulty)

            game_loop(players, difficulty)
        elif player_choice == "2":
            gui.clear_console()
            gui.generate_interaction_text(f" 📚 WIKIPEDIA {gui.TEXT_BOLD} FACT OR FAKE {gui.COLOR_RESET}– SPIELREGELN ")
            gui.show_rules()
        elif player_choice == "3":
            sys.exit()


if __name__ == "__main__":
    main()