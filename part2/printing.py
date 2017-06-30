from pprint import pprint
import reports


def print_function(message, function, file_name):
    print(message)
    pprint(function(file_name))


def main(file_name):
    # What is the title of the most played (top-seller) game?
    print_function("\nThe most played game is: ", reports.get_most_played, file_name)

    # How many copies have been sold in total?
    print_function("\nNumber of copies sold in total (M): ", reports.sum_sold, file_name)

    # How many games are sold on average?
    print_function("\nLength of longest title: ", reports.get_selling_avg, file_name)

    # How many characters long is the longest title?
    print_function("\nLength of longest title: ", reports.count_longest_title, file_name)

    # What is the average of the release dates?
    print_function("\nThe average of release dates is: ", reports.get_date_avg, file_name)

    # What details are there of the game?
    try:
        print_function("\nGame details:", reports.get_game, file_name)
    except ValueError:
        print("Game not found!")

    # bonus: How many games are there in the different genres?
    print_function("\nThe following number of games are per genre: ", reports.count_grouped_by_genre, file_name)

    # bonus: What is the date ordered list of the games?
    print_function("\nList of titles sorted by year of release: ", reports.get_date_ordered, file_name)


main("game_stat.txt")
