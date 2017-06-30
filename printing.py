from pprint import pprint
import reports


def print_function(message, function):
    print(message)
    pprint(function)


def main(file_name):
    # How many games are in the file?
    print_function("\nNumber of games in the file:", reports.count_games(file_name))

    # bonus: What is the abc ordered list of titles?
    print_function("\nThese are the names of said games: ", reports.sort_abc(file_name))

    # Which is the latest game?
    print_function("\nThe latest game in the file is:", reports.get_latest(file_name))

    # What is the line number of the given title?
    try:
        print_function("The game's line number is: ", reports.get_line_number_by_title(file_name))
    except ValueError:
        print("There's no game with that name in the file!")

    # Is there a game from a given year?
    print_function("There is at least one game from the given year:", reports.decide(file_name))

    # bonus: What are the genres?
    print_function("\nThe following genres are in the file: ", reports.get_genres(file_name))

    # How many games do we have by genre?
    print_function("Number of games in genre:", reports.count_by_genre(file_name))

    # bonus: What is the release date of top sold fps shooter game?
    print_function("\nThe highest-selling RPG from the list was released in: ",
                   reports.when_was_top_sold_fps(file_name))


main("game_stat.txt")
