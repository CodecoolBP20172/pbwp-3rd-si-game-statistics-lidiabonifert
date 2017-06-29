from pprint import pprint
import reports

# How many games are in the file?
print("\nNumber of games in the file:")
pprint(reports.count_games("game_stat.txt"))

# bonus: What is the abc ordered list of titles?
print("\nThese are the names of said games: ")
pprint(reports.sort_abc("game_stat.txt"))

# Which is the latest game?
print("\nThe latest game in the file is:")
pprint(reports.get_latest("game_stat.txt"))

# What is the line number of the given title?
game_name_input = input("\nWhich game's line number would you like to know? ")
try:
    print("The game's line number is: ")
    pprint(reports.get_line_number_by_title("game_stat.txt", game_name_input))
except ValueError:
    print("There's no game with that name in the file!")

# Is there a game from a given year?
year_input = str(input("\nWhat year would you like to examine? "))
print("There is at least one game from the given year:")
pprint(reports.decide("game_stat.txt", year_input))

# bonus: What are the genres?
print("\nThe following genres are in the file: ")
pprint(reports.get_genres("game_stat.txt"))

# How many games do we have by genre?
genre_input = input("\nWhich genre are you interested in? ")
print("Number of games in genre:")
pprint(reports.count_by_genre("game_stat.txt", genre_input))

# bonus: What is the release date of top sold fps shooter game?
print("\nThe highest-selling RPG from the list was released in: ")
pprint(reports.when_was_top_sold_fps("game_stat.txt"))
